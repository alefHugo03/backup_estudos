from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from bson.objectid import ObjectId
import datetime
import os

# Inicialização do Flask
app = Flask(__name__)
app.secret_key = "sua_chave_secreta_muito_segura_aqui" # MUDE ISSO EM PRODUÇÃO!
# Configuração dos caminhos para upload de arquivos (dentro da pasta 'static')
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'profile_pics')
app.config['POST_PICS_UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'post_pics')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['MIN_PASSWORD_LENGTH'] = 8

# Cria as pastas de upload se não existirem
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
if not os.path.exists(app.config['POST_PICS_UPLOAD_FOLDER']):
    os.makedirs(app.config['POST_PICS_UPLOAD_FOLDER'])

# Configuração do MongoDB
try:
    client = MongoClient('mongodb://localhost:27017') # Endereço padrão do MongoDB local
    client.admin.command('ping')
    db = client['cadastros']
    users_collection = db['cadastro_cliente']
    profiles_collection = db['profiles']
    notifications_collection = db['notifications']
    posts_collection = db['posts']
    print("MongoDB conectado com sucesso! Coleções prontas.")
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")

def allowed_file(filename):
    """Verifica se a extensão do arquivo é permitida."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.context_processor

def inject_layout_extras():
    """Injeta variáveis globais nos templates."""
    year = datetime.datetime.now().year
    user_is_logged_in = 'user_id' in session
    theme = session.get('user_theme', 'light') if user_is_logged_in else 'light'
    user_type_in_session = session.get('user_type')
    user_email_in_session = session.get('user_email')

    profile_image_url = url_for('static', filename='profile_pics/default_avatar.png') # Default
    if user_is_logged_in:
        user_profile = get_current_user_profile()
        if user_profile and user_profile.get('profile_image_filename'):
            profile_image_url = url_for('static', filename=f"profile_pics/{user_profile.get('profile_image_filename')}")

    unread_notifications_count = 0
    if user_is_logged_in:
        try:
            current_user_id = ObjectId(session['user_id'])
            unread_notifications_count = notifications_collection.count_documents(
                {'recipient_user_id': current_user_id, 'read': False}
            )
        except Exception: # Lida com ObjectId inválido na sessão, se ocorrer
            pass


    return {
        'current_year': year,
        'current_theme': theme,
        'user_is_logged_in': user_is_logged_in,
        'user_type_in_session': user_type_in_session,
        'user_email_in_session': user_email_in_session,
        'profile_image_url_layout': profile_image_url,
        'unread_notifications_count': unread_notifications_count
    }

# --- ROTA PRINCIPAL ---
@app.route('/')
def home():
    all_posts = list(posts_collection.find().sort('created_at', -1))
    for post in all_posts:
        if post.get('image_filename'):
            # Gera URL para imagem do post
            post['display_image_url'] = url_for('static', filename=f"post_pics/{post.get('image_filename')}")
        if post.get('user_profile_pic'):
            # Gera URL para foto de perfil do autor do post
            post['user_profile_pic_url'] = url_for('static', filename=f"profile_pics/{post.get('user_profile_pic')}")
        else:
            post['user_profile_pic_url'] = url_for('static', filename='profile_pics/default_avatar.png')

    if 'user_id' in session:
        try:
            user_db = users_collection.find_one({'_id': ObjectId(session['user_id'])})
            if not user_db:
                session.clear()
                flash('Sua sessão é inválida. Faça login novamente.', 'error')
                return redirect(url_for('login'))
            return render_template('home_logged_in.html', user_email=user_db.get('email'), posts=all_posts)
        except Exception: # ObjectId inválido
            session.clear()
            flash('Sua sessão é inválida. Faça login novamente.', 'error')
            return redirect(url_for('login'))


    # Renderiza a home para usuários deslogados, também com posts
    return render_template('home_logged_out.html', posts=all_posts)


# --- ROTAS DE AUTENTICAÇÃO ---
@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        user_type = request.form.get('user_type')

        if not all([email, password, confirm_password, user_type]):
            flash('Todos os campos são obrigatórios!', 'error')
            return redirect(url_for('register'))

        if len(password) < app.config['MIN_PASSWORD_LENGTH']:
            flash(f'A senha deve ter pelo menos {app.config["MIN_PASSWORD_LENGTH"]} caracteres.', 'error')
            return redirect(url_for('register'))

        if password != confirm_password:
            flash('As senhas não coincidem!', 'error')
            return redirect(url_for('register'))

        if "@" not in email or "." not in email.split('@')[-1]: # Validação simples de email
            flash('Formato de e-mail inválido.', 'error')
            return redirect(url_for('register'))

        existing_user = users_collection.find_one({'email': email})
        if existing_user:
            flash('Este e-mail já está cadastrado!', 'error')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)
        user_data = {
            'email': email,
            'password': hashed_password,
            'user_type': user_type,
            'created_at': datetime.datetime.now(datetime.timezone.utc),
            'theme_preference': 'light', # Default theme
            'email_verified': True, # Simulação de email verificado
        }
        try:
            users_collection.insert_one(user_data)
            flash('Cadastro realizado com sucesso! Você já pode fazer login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'Erro ao cadastrar usuário: {e}', 'error')
            return redirect(url_for('register'))

    return render_template('registration.html', min_password_length=app.config['MIN_PASSWORD_LENGTH'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash('E-mail e senha são obrigatórios.', 'error')
            return redirect(url_for('login'))

        user = users_collection.find_one({'email': email})

        if user and check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            session['user_type'] = user['user_type']
            session['user_email'] = user['email']
            session['user_theme'] = user.get('theme_preference', 'light')
            flash('Login bem-sucedido!', 'success')

            profile = profiles_collection.find_one({'user_id': user['_id']})
            if not profile: # Se não tem perfil, redireciona para criar
                flash('Complete seu perfil para continuar.', 'info')
                return redirect(url_for('create_edit_profile'))
            return redirect(url_for('home'))
        else:
            flash('E-mail ou senha inválidos.', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)      # Remove user_id from session
    session.pop('user_email', None)   # Remove user_email from session
    session.pop('user_type', None)    # Remove user_type from session
    # You might have other session variables to clear, e.g., 'profile_image_url_layout'
    session.pop('profile_image_url_layout', None) # Clear profile image URL from session if stored

    flash('Você foi desconectado com sucesso!', 'success') # Show a success message
    return redirect(url_for('home')) # Redirect to the home page (or login page)

# --- ROTAS DE PERFIL ---
def get_current_user_profile():
    """Busca o perfil do usuário logado no MongoDB."""
    if 'user_id' in session:
        try:
            user_id_obj = ObjectId(session['user_id'])
            profile = profiles_collection.find_one({'user_id': user_id_obj})
            return profile
        except Exception: # ObjectId inválido ou outro erro
            return None
    return None

@app.route('/profile/create', methods=['GET', 'POST'])
@app.route('/profile/edit', methods=['GET', 'POST']) # Mesma rota para criar e editar
def create_edit_profile():
    if 'user_id' not in session:
        flash('Faça login para acessar esta página.', 'warning')
        return redirect(url_for('login'))

    try:
        user_id_obj = ObjectId(session['user_id'])
    except Exception:
        session.clear()
        flash('Sessão inválida, faça login novamente.', 'error')
        return redirect(url_for('login'))

    user_type = session.get('user_type')
    existing_profile = profiles_collection.find_one({'user_id': user_id_obj})

    if request.method == 'POST':
        profile_data = {'user_id': user_id_obj, 'profile_type': user_type}
        profile_data['contato_email'] = request.form.get('contato_email', session.get('user_email'))
        profile_data['contato_telefone'] = request.form.get('contato_telefone')

        # Lógica para upload da imagem de perfil
        current_profile_image_filename = existing_profile.get('profile_image_filename') if existing_profile else None
        if 'profile_image' in request.files:
            file = request.files['profile_image']
            if file and file.filename != '' and allowed_file(file.filename):
                # Define um nome de arquivo seguro e único (ou sobrescreve o existente para o usuário)
                filename_base = secure_filename(f"user_{str(user_id_obj)}")
                filename_ext = file.filename.rsplit('.', 1)[1].lower()
                new_filename = f"{filename_base}.{filename_ext}"

                # Se havia uma imagem antiga com nome diferente, remove
                if current_profile_image_filename and current_profile_image_filename != new_filename:
                    old_path = os.path.join(app.config['UPLOAD_FOLDER'], current_profile_image_filename)
                    if os.path.exists(old_path):
                        try:
                            os.remove(old_path)
                        except OSError as e:
                            print(f"Erro ao deletar imagem de perfil antiga: {e}") # Log

                file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
                file.save(file_path)
                profile_data['profile_image_filename'] = new_filename
            elif file.filename != '': # Se um arquivo foi enviado mas não é permitido
                    flash('Tipo de arquivo de imagem inválido. Use png, jpg, jpeg ou gif.', 'warning')

        # Campos específicos para cada tipo de usuário
        if user_type == 'empreendedor':
            profile_data['nome_negocio'] = request.form.get('nome_negocio')
            profile_data['descricao_negocio'] = request.form.get('descricao_negocio')
            # ... (outros campos de empreendedor)
        elif user_type == 'sponsor':
            profile_data['nome_sponsor'] = request.form.get('nome_sponsor')
            # ... (outros campos de sponsor)
        
        profile_data['last_updated'] = datetime.datetime.now(datetime.timezone.utc)
        
        update_payload = {'$set': profile_data}
        # Garante que a imagem de perfil seja mantida se nenhuma nova for enviada
        if 'profile_image_filename' not in profile_data and current_profile_image_filename:
            update_payload['$set']['profile_image_filename'] = current_profile_image_filename


        if existing_profile:
            profiles_collection.update_one({'_id': existing_profile['_id']}, update_payload)
            flash('Perfil atualizado com sucesso!', 'success')
        else:
            profile_data['created_at'] = datetime.datetime.now(datetime.timezone.utc)
            if 'profile_image_filename' not in profile_data: # Se está criando e não enviou imagem
                 profile_data['profile_image_filename'] = None
            profiles_collection.insert_one(profile_data)
            flash('Perfil criado com sucesso!', 'success')
        return redirect(url_for('home')) # Ou para url_for('my_profile_view')

    # Para GET request, prepara dados para o formulário
    render_data = existing_profile if existing_profile else {}
    if not existing_profile: # Defaults para criação
        render_data['contato_email'] = session.get('user_email', '')
        if user_type == 'sponsor':
            render_data['nichos_interesse'] = [] # Evita erro no join do template se não existir
        render_data['profile_image_filename'] = None


    current_profile_image_url = url_for('static', filename='profile_pics/default_avatar.png')
    if render_data and render_data.get('profile_image_filename'):
        current_profile_image_url = url_for('static', filename=f"profile_pics/{render_data.get('profile_image_filename')}")
    
    return render_template('profile_form.html', user_type=user_type, profile=render_data, current_profile_image_url=current_profile_image_url)


@app.route('/profile/<profile_id_str>')
def view_profile(profile_id_str):
    try:
        profile_obj_id = ObjectId(profile_id_str)
    except Exception:
        flash('ID de perfil inválido.', 'error')
        return redirect(url_for('home'))

    profile_to_view = profiles_collection.find_one({'_id': profile_obj_id})
    if not profile_to_view:
        flash('Perfil não encontrado.', 'error')
        return redirect(url_for('home'))

    is_own_profile = False
    if 'user_id' in session:
        try:
            if profile_to_view.get('user_id') == ObjectId(session['user_id']):
                is_own_profile = True
        except Exception: # ObjectId inválido na sessão
            pass


    # URL da imagem de perfil
    if profile_to_view.get('profile_image_filename'):
        profile_to_view['display_image_url'] = url_for('static', filename=f"profile_pics/{profile_to_view.get('profile_image_filename')}")
    else:
        profile_to_view['display_image_url'] = url_for('static', filename='profile_pics/default_avatar.png')

    # Busca posts do usuário do perfil visualizado
    user_posts = list(posts_collection.find({'user_id': profile_to_view['user_id']}).sort('created_at', -1))
    for post in user_posts:
        if post.get('image_filename'):
            post['display_image_url'] = url_for('static', filename=f"post_pics/{post.get('image_filename')}")
        # A foto de perfil do autor já está em `post.user_profile_pic_url` (se foi adicionada ao criar post)
        # ou pode ser obtida de `profile_to_view.display_image_url`

    return render_template('view_profile.html', profile=profile_to_view, is_own_profile=is_own_profile, user_posts=user_posts)


@app.route('/my-profile')
def my_profile_view():
    if 'user_id' not in session:
        flash('Faça login para acessar seu perfil.', 'warning')
        return redirect(url_for('login'))

    profile = get_current_user_profile()
    if not profile:
        flash('Você ainda não criou um perfil. Crie um agora!', 'info')
        return redirect(url_for('create_edit_profile'))
    # Redireciona para a rota de visualização de perfil com o ID do perfil do usuário logado
    return redirect(url_for('view_profile', profile_id_str=str(profile['_id'])))


# --- ROTAS DE FEED (EMPREENDEDOR/SPONSOR) ---
# (feed_sponsors e feed_lojas permanecem como antes, focados nos perfis, não nos posts gerais)
@app.route('/feed/sponsors')
def feed_sponsors():
    if 'user_id' not in session or session.get('user_type') != 'empreendedor':
        flash('Acesso não autorizado.', 'warning')
        return redirect(url_for('login'))
    # ... (lógica existente do feed_sponsors)
    # Esta rota é para o feed de perfis de sponsors, não de posts.
    # A home page agora lida com o feed de posts.
    current_user_profile = get_current_user_profile()
    if not current_user_profile:
        flash('Por favor, crie seu perfil de empreendedor para ver os sponsors.', 'info')
        return redirect(url_for('create_edit_profile'))

    sponsors_cursor = profiles_collection.find({'profile_type': 'sponsor'})
    sponsors = []
    for sponsor in sponsors_cursor:
        if sponsor.get('profile_image_filename'):
            sponsor['display_image_url'] = url_for('static', filename=f"profile_pics/{sponsor.get('profile_image_filename')}")
        else:
            sponsor['display_image_url'] = url_for('static', filename='profile_pics/default_avatar.png')
        sponsors.append(sponsor)
    return render_template('feed_sponsors.html', sponsors=sponsors, user_profile=current_user_profile)


@app.route('/feed/lojas')
def feed_lojas():
    if 'user_id' not in session or session.get('user_type') != 'sponsor':
        flash('Acesso não autorizado.', 'warning')
        return redirect(url_for('login'))
    # ... (lógica existente do feed_lojas)
    current_user_profile = get_current_user_profile()
    if not current_user_profile:
        flash('Por favor, crie seu perfil de sponsor para ver as lojas/negócios.', 'info')
        return redirect(url_for('create_edit_profile'))

    lojas_cursor = profiles_collection.find({'profile_type': 'empreendedor'})
    lojas = []
    for loja in lojas_cursor:
        if loja.get('profile_image_filename'):
            loja['display_image_url'] = url_for('static', filename=f"profile_pics/{loja.get('profile_image_filename')}")
        else:
            loja['display_image_url'] = url_for('static', filename='profile_pics/default_avatar.png')
        lojas.append(loja)
    return render_template('feed_lojas.html', lojas=lojas, user_profile=current_user_profile)


# --- ROTAS DE POSTS ---
@app.route('/post/create', methods=['GET', 'POST'])
def create_post():
    if 'user_id' not in session:
        flash('Faça login para criar um post.', 'warning')
        return redirect(url_for('login'))

    try:
        user_id_obj = ObjectId(session['user_id'])
    except Exception:
        session.clear()
        flash('Sessão inválida, faça login novamente.', 'error')
        return redirect(url_for('login'))
        
    user_profile = get_current_user_profile()
    if not user_profile:
        flash('Complete seu perfil antes de criar posts.', 'info')
        return redirect(url_for('create_edit_profile'))

    if request.method == 'POST':
        text_content = request.form.get('text_content')
        post_image_file = request.files.get('post_image')

        if not text_content and not (post_image_file and post_image_file.filename != ''):
            flash('O post precisa ter um texto ou uma imagem.', 'error')
            return redirect(url_for('create_post')) # Volta para o formulário de criação

        user_display_name = session.get('user_email', 'Usuário Anônimo') # Fallback
        if user_profile.get('profile_type') == 'empreendedor':
            user_display_name = user_profile.get('nome_negocio', user_display_name)
        elif user_profile.get('profile_type') == 'sponsor':
            user_display_name = user_profile.get('nome_sponsor', user_display_name)

        post_data = {
            'user_id': user_id_obj,
            'user_name': user_display_name,
            'user_profile_pic': user_profile.get('profile_image_filename'), # Salva nome da foto de perfil atual
            'text_content': text_content,
            'image_filename': None, # Default
            'created_at': datetime.datetime.now(datetime.timezone.utc)
        }

        if post_image_file and post_image_file.filename != '' and allowed_file(post_image_file.filename):
            # Nome de arquivo único para imagem do post
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            filename_base = secure_filename(f"post_{str(user_id_obj)}_{timestamp}")
            filename_ext = post_image_file.filename.rsplit('.', 1)[1].lower()
            new_filename = f"{filename_base}.{filename_ext}"
            
            file_path = os.path.join(app.config['POST_PICS_UPLOAD_FOLDER'], new_filename)
            post_image_file.save(file_path)
            post_data['image_filename'] = new_filename
        elif post_image_file and post_image_file.filename != '': # Arquivo enviado mas inválido
            flash('Tipo de arquivo de imagem inválido para o post. Use png, jpg, jpeg ou gif.', 'warning')
            # Permite criar post sem imagem se houver texto

        try:
            posts_collection.insert_one(post_data)
            flash('Post criado com sucesso!', 'success')
            return redirect(url_for('home'))
        except Exception as e:
            flash(f'Erro ao criar post: {e}', 'error')
            return redirect(url_for('create_post'))

    return render_template('create_post.html') # Para GET request


@app.route('/post/delete/<post_id_str>', methods=['POST'])
def delete_post(post_id_str):
    if 'user_id' not in session:
        flash('Faça login para deletar posts.', 'warning')
        return redirect(url_for('login'))

    try:
        post_obj_id = ObjectId(post_id_str)
        user_id_obj = ObjectId(session['user_id'])
    except Exception:
        flash('ID de post ou usuário inválido.', 'error')
        return redirect(request.referrer or url_for('home'))

    post_to_delete = posts_collection.find_one({'_id': post_obj_id, 'user_id': user_id_obj})

    if not post_to_delete:
        flash('Post não encontrado ou você não tem permissão para deletá-lo.', 'error')
        return redirect(request.referrer or url_for('home'))

    # Deleta a imagem do post do sistema de arquivos, se existir
    if post_to_delete.get('image_filename'):
        image_path = os.path.join(app.config['POST_PICS_UPLOAD_FOLDER'], post_to_delete['image_filename'])
        if os.path.exists(image_path):
            try:
                os.remove(image_path)
            except OSError as e:
                print(f"Erro ao deletar arquivo de imagem do post: {e}") # Log do erro

    try:
        posts_collection.delete_one({'_id': post_obj_id})
        flash('Post deletado com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao deletar post do banco de dados: {e}', 'error')

    # Redireciona para a página anterior (provavelmente o perfil do usuário)
    return redirect(request.referrer or url_for('my_profile_view'))


# --- ROTA DE EXPRESSAR INTERESSE E NOTIFICAÇÕES ---
# (express_interest e view_notifications permanecem como antes)
@app.route('/express_interest/<empreendedor_profile_id>', methods=['POST'])
def express_interest(empreendedor_profile_id):
    if 'user_id' not in session or session.get('user_type') != 'sponsor':
        flash('Você precisa ser um patrocinador para expressar interesse.', 'error')
        return redirect(url_for('login'))
    # ... (lógica existente)
    try:
        empreendedor_profile_obj_id = ObjectId(empreendedor_profile_id)
    except Exception:
        flash('Perfil de empreendedor inválido.', 'error')
        return redirect(url_for('home'))

    empreendedor_profile = profiles_collection.find_one({'_id': empreendedor_profile_obj_id})
    if not empreendedor_profile or empreendedor_profile.get('profile_type') != 'empreendedor':
        flash('Empreendedor não encontrado ou perfil inválido.', 'error')
        return redirect(url_for('feed_lojas'))

    sponsor_profile = profiles_collection.find_one({'user_id': ObjectId(session['user_id'])})
    if not sponsor_profile:
        flash('Por favor, complete seu perfil de patrocinador antes de expressar interesse.', 'warning')
        return redirect(url_for('create_edit_profile'))

    existing_notification = notifications_collection.find_one({
        'sender_user_id': ObjectId(session['user_id']),
        'recipient_user_id': empreendedor_profile['user_id'],
        'type': 'interest',
        'related_profile_id': empreendedor_profile_obj_id
    })

    if existing_notification:
        flash('Você já expressou interesse neste negócio.', 'info')
        return redirect(url_for('view_profile', profile_id_str=empreendedor_profile_id))

    notification_data = {
        'sender_user_id': ObjectId(session['user_id']),
        'sender_profile_id': sponsor_profile['_id'],
        'sender_name': sponsor_profile.get('nome_sponsor', session.get('user_email')),
        'recipient_user_id': empreendedor_profile['user_id'],
        'type': 'interest',
        'message': f"{sponsor_profile.get('nome_sponsor', 'Um patrocinador')} expressou interesse em seu negócio '{empreendedor_profile.get('nome_negocio', 'Sem Nome')}'!",
        'related_profile_id': empreendedor_profile_obj_id,
        'created_at': datetime.datetime.now(datetime.timezone.utc),
        'read': False
    }
    try:
        notifications_collection.insert_one(notification_data)
        flash('Seu interesse foi enviado ao empreendedor!', 'success')
    except Exception as e:
        flash(f'Erro ao registrar interesse: {e}', 'error')
    return redirect(url_for('view_profile', profile_id_str=empreendedor_profile_id))


@app.route('/notifications')
def view_notifications():
    if 'user_id' not in session:
        flash('Faça login para ver suas notificações.', 'warning')
        return redirect(url_for('login'))
    # ... (lógica existente)
    try:
        current_user_id = ObjectId(session['user_id'])
        notifications = list(notifications_collection.find({'recipient_user_id': current_user_id}).sort('created_at', -1))
        # Marca como lidas ao visualizar
        notifications_collection.update_many(
            {'recipient_user_id': current_user_id, 'read': False},
            {'$set': {'read': True}}
        )
        return render_template('notifications.html', notifications=notifications)
    except Exception:
        session.clear()
        flash('Sessão inválida, faça login novamente.', 'error')
        return redirect(url_for('login'))


# --- ROTA DE CONFIGURAÇÕES ---
# (settings permanece como antes)
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if 'user_id' not in session:
        flash('Faça login para acessar esta página.', 'warning')
        return redirect(url_for('login'))
    # ... (lógica existente)
    try:
        user_id_obj = ObjectId(session['user_id'])
        user = users_collection.find_one({'_id': user_id_obj})
    except Exception:
        session.clear()
        flash('Sessão inválida, faça login novamente.', 'error')
        return redirect(url_for('login'))

    if not user:
        session.clear()
        flash('Erro ao carregar dados do usuário.', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'change_theme':
            theme = request.form.get('theme_preference')
            if theme in ['light', 'dark']:
                users_collection.update_one(
                    {'_id': user_id_obj},
                    {'$set': {'theme_preference': theme}}
                )
                session['user_theme'] = theme
                flash('Preferências de tema atualizadas com sucesso!', 'success')
            else:
                flash('Opção de tema inválida.', 'error')

        elif action == 'change_password':
            current_password = request.form.get('current_password')
            new_password = request.form.get('new_password')
            confirm_new_password = request.form.get('confirm_new_password')

            if not all([current_password, new_password, confirm_new_password]):
                flash('Todos os campos de senha são obrigatórios.', 'error')
            elif not check_password_hash(user['password'], current_password):
                flash('Senha atual incorreta.', 'error')
            elif len(new_password) < app.config['MIN_PASSWORD_LENGTH']:
                flash(f'A nova senha deve ter pelo menos {app.config["MIN_PASSWORD_LENGTH"]} caracteres.', 'error')
            elif new_password != confirm_new_password:
                flash('As novas senhas não coincidem.', 'error')
            else:
                hashed_new_password = generate_password_hash(new_password)
                users_collection.update_one(
                    {'_id': user_id_obj},
                    {'$set': {'password': hashed_new_password}}
                )
                flash('Senha alterada com sucesso!', 'success')
        return redirect(url_for('settings'))

    selected_theme = user.get('theme_preference', 'light')
    return render_template('settings.html',
                            selected_theme=selected_theme,
                            user_email=user.get('email'),
                            min_password_length=app.config['MIN_PASSWORD_LENGTH'])

# --- PONTO DE PARTIDA DA APLICAÇÃO ---
if __name__ == '__main__':
    app.run(debug=True) # debug=True é para desenvolvimento, mude para False em produção