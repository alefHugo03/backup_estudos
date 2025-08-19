import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os
import threading
import queue
import pandas as pd
from tkintermapview import TkinterMapView

# --- Importações dos seus módulos ---
# Certifique-se de que esses arquivos (mapa.py, grafrico.py, conversao.py)
# existam no mesmo diretório ou em um local acessível ao Python.
from mapa import converter_para_geodataframe
from grafrico import gerar_grafico_pessoas_por_estado
from conversao import dados_saida, PRE_RENDER_FOLDER # Importa também PRE_RENDER_FOLDER

# --- Cores Confortáveis e Legíveis (Paleta para a UI) ---
BG_COLOR = "#f0f0f0"  # Um cinza claro suave para o fundo principal
TEXT_COLOR = "#000000" # Texto preto para máxima legibilidade
BUTTON_BG = "#e0e0e0"  # Fundo de botão um pouco mais claro que o principal
BUTTON_ACTIVE_BG = "#c8c8c8" # Fundo do botão quando pressionado/ativo
FRAME_BG = "#f0f0f0" # Fundo para os frames internos, igual ao principal
DISPLAY_AREA_BG = "#ffffff" # Fundo branco para a área de exibição de conteúdo (mapa, gráfico, tabela)
FRAME_BORDER_COLOR = "#b0b0b0" # Cor da borda para os frames

# --- Definições dos Workers (Funções que rodam em threads separadas) e Filas ---
# Filas para comunicação segura entre a thread principal e as threads workers
data_queue = queue.Queue() # Para os dados processados (DataFrame, GeoDataFrame)
graph_image_queue = queue.Queue() # Para a imagem do gráfico gerada

# Define o nome do arquivo para o GeoDataFrame pré-renderizado
GEO_DATA_CACHE_FILE = os.path.join(PRE_RENDER_FOLDER, 'geocoded_data_cache.parquet')

def worker_carregar_dados_base():
    """
    Função worker para carregar e pré-processar os dados base em uma thread separada.
    Tenta carregar de cache primeiro; se não existir, processa e salva.
    """
    try:
        df_carregado = dados_saida() # Sempre lê os dados brutos para ter o DataFrame original

        if df_carregado is None or df_carregado.empty:
            raise ValueError("DataFrame carregado dos arquivos de origem está vazio.")

        # --- Lógica de cache ---
        if os.path.exists(GEO_DATA_CACHE_FILE):
            print(f"Tentando carregar GeoDataFrame do cache: {GEO_DATA_CACHE_FILE}")
            try:
                gdf_carregado = pd.read_parquet(GEO_DATA_CACHE_FILE)
                if 'geometry' not in gdf_carregado.columns:
                     raise ValueError("Arquivo de cache não contém a coluna 'geometry'. Recodificando.")
                if gdf_carregado.empty:
                    raise ValueError("Arquivo de cache GeoDataFrame está vazio. Recodificando.")
                print("GeoDataFrame carregado com sucesso do cache.")

            except Exception as e:
                print(f"Erro ao carregar GeoDataFrame do cache ({e}). Forçando nova geocodificação...")
                if 'cep' not in df_carregado.columns:
                    raise ValueError("DataFrame original não possui a coluna 'cep' para geocodificação.")
                gdf_carregado = converter_para_geodataframe(df_carregado)
                try:
                    os.makedirs(PRE_RENDER_FOLDER, exist_ok=True)
                    gdf_carregado.to_parquet(GEO_DATA_CACHE_FILE)
                    print(f"Novo GeoDataFrame geocodificado e salvo em cache: {GEO_DATA_CACHE_FILE}")
                except Exception as save_e:
                    print(f"AVISO: Não foi possível salvar o GeoDataFrame em cache: {save_e}")
        else:
            print(f"Arquivo de cache não encontrado: {GEO_DATA_CACHE_FILE}. Realizando geocodificação completa...")
            if 'cep' not in df_carregado.columns:
                raise ValueError("DataFrame original não possui a coluna 'cep' para geocodificação.")
            gdf_carregado = converter_para_geodataframe(df_carregado)
            try:
                os.makedirs(PRE_RENDER_FOLDER, exist_ok=True)
                gdf_carregado.to_parquet(GEO_DATA_CACHE_FILE)
                print(f"GeoDataFrame geocodificado e salvo em cache: {GEO_DATA_CACHE_FILE}")
            except Exception as save_e:
                print(f"AVISO: Não foi possível salvar o GeoDataFrame em cache: {save_e}")

        data_queue.put({"df": df_carregado, "gdf": gdf_carregado})

    except Exception as e:
        data_queue.put({"error": f"Erro no worker_carregar_dados_base: {e}"})
        print(f"ERRO (worker_carregar_dados_base): {e}")

def worker_gerar_grafico(dataframe_para_grafico):
    """
    Função worker para gerar a imagem do gráfico em uma thread separada.
    Coloca a imagem PIL resultante na graph_image_queue.
    """
    try:
        if dataframe_para_grafico is None or dataframe_para_grafico.empty:
            graph_image_queue.put({"error": "DataFrame vazio ou inválido para gerar o gráfico."})
            return

        pil_image = gerar_grafico_pessoas_por_estado(dataframe_para_grafico)
        graph_image_queue.put(pil_image)
    except Exception as e:
        graph_image_queue.put({"error": f"Erro no worker_gerar_grafico: {e}"})
        print(f"ERRO (worker_gerar_grafico): {e}")



class LoginApp:
    def __init__(self, master_tk):
        self.master = master_tk
        self.master.title("Login / Cadastro")
        self.master.geometry("380x280")
        self.master.resizable(False, False)
        self.master.config(bg=BG_COLOR)

        self.users = {"admin": "1", "teste": "1"}

        self._configurar_estilos_login()
        self._configurar_ui_login()

    def _configurar_estilos_login(self):
        style = ttk.Style(self.master)
        style.configure("Login.TFrame", background=BG_COLOR)
        style.configure("Login.TLabel", background=BG_COLOR, foreground=TEXT_COLOR, font=('Arial', 11))
        style.configure("Login.TEntry", fieldbackground="white", foreground=TEXT_COLOR)
        style.configure("Login.TButton", padding=5, font=('Arial', 10), foreground=TEXT_COLOR,
                        background=BUTTON_BG)
        style.map("Login.TButton", background=[('active', BUTTON_ACTIVE_BG)])

    def _limpar_frame(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def _configurar_ui_login(self):
        self._limpar_frame()

        self.login_frame = ttk.Frame(self.master, style="Login.TFrame", padding="20")
        self.login_frame.pack(expand=True)

        lbl_username = ttk.Label(self.login_frame, text="Usuário:", style="Login.TLabel")
        lbl_username.grid(row=0, column=0, pady=5, padx=5, sticky="w")
        self.entry_login_username = ttk.Entry(self.login_frame, style="Login.TEntry", width=30)
        self.entry_login_username.grid(row=0, column=1, pady=5, padx=5)
        self.entry_login_username.focus_set()

        lbl_password = ttk.Label(self.login_frame, text="Senha:", style="Login.TLabel")
        lbl_password.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        self.entry_login_password = ttk.Entry(self.login_frame, style="Login.TEntry", show="*", width=30)
        self.entry_login_password.grid(row=1, column=1, pady=5, padx=5)
        self.entry_login_password.bind("<Return>", lambda event: self._check_login())

        btn_login = ttk.Button(self.login_frame, text="Entrar", command=self._check_login, style="Login.TButton")
        btn_login.grid(row=2, column=0, columnspan=2, pady=10)

        lbl_register_prompt = ttk.Label(self.login_frame, text="Não tem uma conta?", style="Login.TLabel")
        lbl_register_prompt.grid(row=3, column=0, columnspan=2, pady=(10, 0))

        btn_go_to_register = ttk.Button(self.login_frame, text="Criar Conta", command=self._configurar_ui_register, style="Login.TButton")
        btn_go_to_register.grid(row=4, column=0, columnspan=2, pady=5)

    def _configurar_ui_register(self):
        self._limpar_frame()

        self.register_frame = ttk.Frame(self.master, style="Login.TFrame", padding="20")
        self.register_frame.pack(expand=True)

        lbl_username = ttk.Label(self.register_frame, text="Novo Usuário:", style="Login.TLabel")
        lbl_username.grid(row=0, column=0, pady=5, padx=5, sticky="w")
        self.entry_register_username = ttk.Entry(self.register_frame, style="Login.TEntry", width=30)
        self.entry_register_username.grid(row=0, column=1, pady=5, padx=5)
        self.entry_register_username.focus_set()

        lbl_password = ttk.Label(self.register_frame, text="Senha:", style="Login.TLabel")
        lbl_password.grid(row=1, column=0, pady=5, padx=5, sticky="w")
        self.entry_register_password = ttk.Entry(self.register_frame, style="Login.TEntry", show="*", width=30)
        self.entry_register_password.grid(row=1, column=1, pady=5, padx=5)

        lbl_confirm_password = ttk.Label(self.register_frame, text="Confirmar Senha:", style="Login.TLabel")
        lbl_confirm_password.grid(row=2, column=0, pady=5, padx=5, sticky="w")
        self.entry_confirm_password = ttk.Entry(self.register_frame, style="Login.TEntry", show="*", width=30)
        self.entry_confirm_password.grid(row=2, column=1, pady=5, padx=5)
        self.entry_confirm_password.bind("<Return>", lambda event: self._register_user())

        btn_register = ttk.Button(self.register_frame, text="Registrar", command=self._register_user, style="Login.TButton")
        btn_register.grid(row=3, column=0, columnspan=2, pady=10)

        btn_back_to_login = ttk.Button(self.register_frame, text="Voltar ao Login", command=self._configurar_ui_login, style="Login.TButton")
        btn_back_to_login.grid(row=4, column=0, columnspan=2, pady=5)

    def _check_login(self):
        entered_username = self.entry_login_username.get()
        entered_password = self.entry_login_password.get()

        if entered_username in self.users and self.users[entered_username] == entered_password:
            self.master.destroy()
            root_main = tk.Tk()
            AplicativoVisualizadorDados(root_main)
            root_main.mainloop()
        else:
            messagebox.showerror("Erro de Login", "Usuário ou senha incorretos.")

    def _register_user(self):
        new_username = self.entry_register_username.get()
        new_password = self.entry_register_password.get()
        confirm_password = self.entry_confirm_password.get()

        if not new_username or not new_password or not confirm_password:
            messagebox.showwarning("Campos Vazios", "Todos os campos devem ser preenchidos.")
            return

        if new_password != confirm_password:
            messagebox.showerror("Erro de Senha", "As senhas não coincidem.")
            return

        if new_username in self.users:
            messagebox.showwarning("Usuário Existente", "Este nome de usuário já está em uso.")
            return

        self.users[new_username] = new_password
        messagebox.showinfo("Sucesso", f"Usuário '{new_username}' registrado com sucesso!")
        self._configurar_ui_login()



class AplicativoVisualizadorDados:
    def __init__(self, master_tk):
        self.master = master_tk
        self.master.title("Visualizador de Dados Interativos")
        self.master.geometry("1000x750")
        self.master.config(bg=BG_COLOR)

        self._image_references = {}
        self.dados_carregados = {
            "df": None,
            "gdf": None,
            "graph_pil_image": None,
            "mapa_widget": None
        }
        self.status_geracao = {
            "dados_base": "pendente",
            "grafico": "pendente"
        }

        self._configurar_estilos()
        self._configurar_ui()
        self._iniciar_pre_renderizacao()

    def _configurar_estilos(self):
        style = ttk.Style(self.master)

        style.configure("TButton", padding=10, font=('Arial', 12), borderwidth=1,
                        foreground=TEXT_COLOR)
        style.map("TButton",
                  background=[('active', BUTTON_ACTIVE_BG), ('!disabled', BUTTON_BG)],
                  foreground=[('!disabled', TEXT_COLOR)])

        style.configure("TLabel", background=FRAME_BG, foreground=TEXT_COLOR, font=('Arial', 11))
        style.configure("Status.TLabel", font=('Arial', 9), padding=3, background=BG_COLOR, foreground=TEXT_COLOR)
        style.configure("Header.TLabel", font=('Arial', 14, 'bold'), background=DISPLAY_AREA_BG, foreground=TEXT_COLOR)
        style.configure("Info.TLabel", font=('Arial', 12), background=DISPLAY_AREA_BG, foreground=TEXT_COLOR, anchor="center", justify="center")

        style.configure("TFrame", background=FRAME_BG)
        style.configure("Display.TFrame", background=DISPLAY_AREA_BG, relief="sunken", borderwidth=1)
        style.configure("ButtonFrame.TFrame", background=FRAME_BG, padding="15")

        style.configure("Treeview", background="white", foreground=TEXT_COLOR,
                        fieldbackground="white", font=('Arial', 10), rowheight=25)
        style.configure("Treeview.Heading", background=BUTTON_BG, foreground=TEXT_COLOR,
                        font=('Arial', 11, 'bold'), relief="raised", padding=(5,5))
        style.map("Treeview.Heading", relief=[('active','groove'),('!active','raised')])

    def _configurar_ui(self):
        self.frame_botoes = ttk.Frame(self.master, style="ButtonFrame.TFrame")
        self.frame_botoes.pack(side="top", fill="x")

        self.btn_mapa = ttk.Button(self.frame_botoes, text="Mapa (Carregando...)", command=self.mostrar_mapa, state="disabled")
        self.btn_grafico = ttk.Button(self.frame_botoes, text="Gráfico (Carregando...)", command=self.mostrar_grafico, state="disabled")
        self.btn_tabela = ttk.Button(self.frame_botoes, text="Tabela (Carregando...)", command=self.mostrar_tabela, state="disabled")
        self.btn_sair = ttk.Button(self.frame_botoes, text="Sair", command=self.sair)

        self.btn_mapa.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        self.btn_grafico.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.btn_tabela.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
        self.btn_sair.grid(row=0, column=3, padx=10, pady=10, sticky="ew")

        for i in range(4):
            self.frame_botoes.columnconfigure(i, weight=1)

        self.frame_display = ttk.Frame(self.master, style="Display.TFrame")
        self.frame_display.pack(side="top", fill="both", expand=True, padx=10, pady=(0,10))

        self.lbl_mensagem_inicial = ttk.Label(self.frame_display,
                                               text="Pré-renderizando dados, por favor aguarde...",
                                               style="Header.TLabel", anchor="center")
        self.lbl_mensagem_inicial.pack(fill="both", expand=True, padx=20, pady=20)

        self.lbl_status_bar = ttk.Label(self.master, text="Status: Inicializando...", style="Status.TLabel", relief="flat", anchor="w")
        self.lbl_status_bar.pack(side="bottom", fill="x", padx=2, pady=2)

    def _iniciar_pre_renderizacao(self):
        self.lbl_status_bar.config(text="Status: Carregando dados base...")
        self.status_geracao["dados_base"] = "carregando"
        threading.Thread(target=worker_carregar_dados_base, daemon=True).start()
        self.master.after(100, self._checar_fila_dados_base)

    def _checar_fila_dados_base(self):
        try:
            resultado = data_queue.get_nowait()
            if "error" in resultado:
                self.status_geracao["dados_base"] = "erro"
                self.lbl_status_bar.config(text=f"Status: Erro ao carregar dados base - {resultado['error']}")
                messagebox.showerror("Erro de Dados", resultado['error'])
                self._atualizar_botoes_erro_dados()
                self.lbl_mensagem_inicial.config(text="Falha ao carregar dados.\nVerifique os arquivos de origem ou o console.")
                return

            self.dados_carregados["df"] = resultado["df"]
            self.dados_carregados["gdf"] = resultado["gdf"]

            # --- Prints de depuração ---
            print("\n--- Verificação de Dados Carregados ---")
            if self.dados_carregados["df"] is not None:
                print(f"DataFrame (df) carregado. Primeiras 5 linhas:\n{self.dados_carregados['df'].head()}")
                print(f"DataFrame (df) tem {len(self.dados_carregados['df'])} linhas.")
                if 'cep' not in self.dados_carregados['df'].columns:
                    print("AVISO: Coluna 'cep' não encontrada no DataFrame original.")
            else:
                print("DataFrame (df) é None.")

            if self.dados_carregados["gdf"] is not None:
                print(f"GeoDataFrame (gdf) carregado. Primeiras 5 linhas:\n{self.dados_carregados['gdf'].head()}")
                print(f"GeoDataFrame (gdf) tem {len(self.dados_carregados['gdf'])} linhas.")
                if not self.dados_carregados["gdf"].empty:
                    invalid_geometries = self.dados_carregados["gdf"]['geometry'].apply(lambda x: x is None or x.is_empty).sum()
                    if invalid_geometries > 0:
                        print(f"AVISO: {invalid_geometries} geometrias inválidas/nulas no GeoDataFrame.")
                    print(f"Exemplo de geometria (primeira linha válida):")
                    first_valid_geo = self.dados_carregados['gdf']['geometry'].dropna().iloc[0] if not self.dados_carregados['gdf']['geometry'].dropna().empty else None
                    if first_valid_geo:
                        print(f"  Ponto: {first_valid_geo}")
                        print(f"  Latitude (y): {first_valid_geo.y}, Longitude (x): {first_valid_geo.x}")
                    else:
                        print("  Nenhuma geometria válida encontrada.")
                else:
                    print("GeoDataFrame (gdf) está vazio.")
            else:
                print("GeoDataFrame (gdf) é None.")
            print("--------------------------------------\n")
            # --- Fim dos prints de depuração ---

            self.status_geracao["dados_base"] = "pronto"
            self.lbl_status_bar.config(text="Status: Dados base carregados. Iniciando renderização do gráfico...")
            self.lbl_mensagem_inicial.config(text="Dados carregados. Pré-renderizando visualizações...")

            self.btn_tabela.config(text="Mostrar Tabela", state="normal")

            if self.dados_carregados["df"] is not None and not self.dados_carregados["df"].empty:
                self.status_geracao["grafico"] = "carregando"
                threading.Thread(target=worker_gerar_grafico, args=(self.dados_carregados["df"],), daemon=True).start()
            else:
                self._grafico_pronto(erro="DataFrame vazio ou inválido para o gráfico.")

            if self.dados_carregados["gdf"] is not None and not self.dados_carregados["gdf"].empty:
                self.btn_mapa.config(text="Mostrar Mapa", state="normal")
            else:
                self.btn_mapa.config(text="Mapa (Sem Dados Geo)", state="disabled")

            self.master.after(100, self._checar_fila_grafico)

        except queue.Empty:
            if self.status_geracao["dados_base"] not in ["pronto", "erro"]:
                self.master.after(200, self._checar_fila_dados_base)
        except Exception as e:
            self.lbl_status_bar.config(text=f"Status: Erro inesperado - {e}")
            print(f"Erro em _checar_fila_dados_base: {e}")
            self._atualizar_botoes_erro_dados()

    def _checar_fila_grafico(self):
        if self.status_geracao["grafico"] == "carregando":
            try:
                resultado_grafico = graph_image_queue.get_nowait()
                if isinstance(resultado_grafico, Image.Image):
                    self._grafico_pronto(imagem=resultado_grafico)
                elif isinstance(resultado_grafico, dict) and "error" in resultado_grafico:
                    self._grafico_pronto(erro=resultado_grafico["error"])
                elif resultado_grafico is None:
                    self._grafico_pronto(erro="Falha ao gerar imagem do gráfico (verifique console).")
                else:
                    self._grafico_pronto(erro="Resposta inválida do worker do gráfico.")
            except queue.Empty:
                self.master.after(200, self._checar_fila_grafico)
                return
            except Exception as e:
                self._grafico_pronto(erro=f"Erro ao processar fila do gráfico: {e}")

        if self.status_geracao["grafico"] != "carregando":
            self.lbl_status_bar.config(text="Status: Pronto.")
            if self.lbl_mensagem_inicial and self.lbl_mensagem_inicial.winfo_exists():
                self.lbl_mensagem_inicial.config(text="Pré-renderização concluída.\nSelecione uma opção para visualizar.")
                if self.status_geracao["dados_base"] == "pronto" and \
                   len(self.frame_display.winfo_children()) == 1 and \
                   self.frame_display.winfo_children()[0] == self.lbl_mensagem_inicial:
                    self.mostrar_tabela()

    def _grafico_pronto(self, imagem=None, erro=None):
        if erro:
            self.status_geracao["grafico"] = "erro"
            self.dados_carregados["graph_pil_image"] = None
            self.btn_grafico.config(text="Gráfico (Erro)", state="disabled")
            print(f"ERRO (Gráfico): {erro}")
        elif imagem is None:
            self.status_geracao["grafico"] = "erro"
            self.dados_carregados["graph_pil_image"] = None
            self.btn_grafico.config(text="Gráfico (Falha Gen.)", state="disabled")
            print("ERRO (Gráfico): Imagem do gráfico não pôde ser criada (None).")
        else:
            self.status_geracao["grafico"] = "pronto"
            self.dados_carregados["graph_pil_image"] = imagem
            self.btn_grafico.config(text="Mostrar Gráfico", state="normal")
            print("Gráfico pronto!")

    def _atualizar_botoes_erro_dados(self):
        self.btn_tabela.config(text="Tabela (Erro Dados)", state="disabled")
        self.btn_mapa.config(text="Mapa (Erro Dados)", state="disabled")
        self.btn_grafico.config(text="Gráfico (Erro Dados)", state="disabled")

    def _limpar_frame_display(self):
        if hasattr(self, 'mapa_view_widget') and self.mapa_view_widget is not None:
            if self.mapa_view_widget.winfo_exists():
                self.mapa_view_widget.destroy()
            self.mapa_view_widget = None
            self.dados_carregados["mapa_widget"] = None

        for widget in self.frame_display.winfo_children():
            widget.destroy()
        self._image_references.clear()

        self.lbl_mensagem_inicial = ttk.Label(self.frame_display,
                                               text="Selecione uma opção para visualizar.",
                                               style="Header.TLabel", anchor="center")
        self.lbl_mensagem_inicial.pack(fill="both", expand=True, padx=20, pady=20)

    def _exibir_imagem_pil_no_frame(self, pil_image, image_key="imagem_atual"):
        self.frame_display.update_idletasks()
        frame_width = self.frame_display.winfo_width()
        frame_height = self.frame_display.winfo_height()

        if frame_width <= 1 or frame_height <= 1:
            self.master.after(50, lambda: self._exibir_imagem_pil_no_frame(pil_image, image_key))
            return

        original_width, original_height = pil_image.size
        aspect_ratio = original_width / original_height

        new_width = frame_width
        new_height = int(new_width / aspect_ratio)

        if new_height > frame_height:
            new_height = frame_height
            new_width = int(new_height * aspect_ratio)

        new_width = max(1, int(new_width))
        new_height = max(1, int(new_height))

        try:
            resized_image = pil_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            tk_image = ImageTk.PhotoImage(resized_image)
        except Exception as e:
            print(f"Erro ao redimensionar ou criar PhotoImage: {e}")
            messagebox.showerror("Erro de Imagem", "Não foi possível processar a imagem para exibição.")
            self._limpar_frame_display()
            return

        lbl_imagem = ttk.Label(self.frame_display, image=tk_image, anchor="center")
        lbl_imagem.image = tk_image
        self._image_references.clear()
        self._image_references[image_key] = tk_image
        lbl_imagem.pack(fill="both", expand=True, padx=5, pady=5)

    def _marker_click_command(self, marker_info):
        """Função chamada ao clicar em um marcador, exibe informações."""
        messagebox.showinfo("Detalhes do Marcador", marker_info)

    def _criar_e_mostrar_mapa_interativo(self):
        """Cria e exibe o widget do mapa interativo com marcadores individuais para cada pessoa."""
        if self.dados_carregados["gdf"] is not None and not self.dados_carregados["gdf"].empty:
            if hasattr(self, 'mapa_view_widget') and self.mapa_view_widget is not None:
                if self.mapa_view_widget.winfo_exists():
                    self.mapa_view_widget.destroy()
                self.mapa_view_widget = None

            self.mapa_view_widget = TkinterMapView(self.frame_display, corner_radius=0)
            self.mapa_view_widget.pack(fill="both", expand=True, padx=5, pady=5)
            self.dados_carregados["mapa_widget"] = self.mapa_view_widget

            # --- Lógica para centralizar o mapa e definir o zoom inicial ---
            all_longitudes = self.dados_carregados["gdf"].geometry.x.tolist()
            all_latitudes = self.dados_carregados["gdf"].geometry.y.tolist()

            valid_longitudes = [lon for lon in all_longitudes if pd.notnull(lon) and isinstance(lon, (int, float))]
            valid_latitudes = [lat for lat in all_latitudes if pd.notnull(lat) and isinstance(lat, (int, float))]

            if valid_longitudes and valid_latitudes:
                # Calcula a posição central (centroide) para o mapa iniciar focado
                avg_lon = sum(valid_longitudes) / len(valid_longitudes)
                avg_lat = sum(valid_latitudes) / len(valid_latitudes)
                self.mapa_view_widget.set_position(avg_lat, avg_lon)

                # Ajusta o zoom com base na dispersão dos pontos
                if len(valid_latitudes) > 1:
                    lat_range = max(valid_latitudes) - min(valid_latitudes)
                    lon_range = max(valid_longitudes) - min(valid_longitudes)
                    
                    if max(lat_range, lon_range) > 60:
                        zoom_level = 3
                    elif max(lat_range, lon_range) > 30:
                        zoom_level = 4
                    elif max(lat_range, lon_range) > 10:
                        zoom_level = 6
                    elif max(lat_range, lon_range) > 3:
                        zoom_level = 8
                    elif max(lat_range, lon_range) > 0.5:
                        zoom_level = 10
                    else:
                        zoom_level = 12
                    self.mapa_view_widget.set_zoom(zoom_level)
                else:
                    self.mapa_view_widget.set_zoom(13) # Zoom mais próximo para um único ponto

                # --- Adiciona UM MARCADOR PARA CADA PESSOA ---
                for index, row in self.dados_carregados["gdf"].iterrows():
                    if row['geometry'] is not None and not row['geometry'].is_empty:
                        latitude = row['geometry'].y
                        longitude = row['geometry'].x
                        
                        nome = row.get('nome', 'N/A')
                        salario = row.get('salarios_minimos', 'N/A')
                        cep = row.get('cep', 'N/A')
                        
                        marker_info = f"Nome: {nome}\nSalários Mínimos: {salario}\nCEP: {cep}"

                        marker = self.mapa_view_widget.set_marker(
                            latitude,
                            longitude,
                            text=nome, # O texto do marcador será o nome da pessoa
                            command=lambda m_info=marker_info: self._marker_click_command(m_info)
                        )
                        marker.marker_info = marker_info # Armazena a informação completa
            else:
                self.mapa_view_widget.set_position(-15.7801, -47.9292)
                self.mapa_view_widget.set_zoom(4)
        else:
            lbl_sem_dados = ttk.Label(self.frame_display, text="Não há dados de localização para exibir no mapa.", style="Info.TLabel")
            lbl_sem_dados.pack(fill="both", expand=True, padx=10, pady=10)

    def mostrar_mapa(self):
        self._limpar_frame_display()
        if self.status_geracao["dados_base"] == "pronto":
            if self.dados_carregados["gdf"] is not None and not self.dados_carregados["gdf"].empty:
                self._criar_e_mostrar_mapa_interativo()
            else:
                lbl_aviso = ttk.Label(self.frame_display, text="Não há dados geográficos para o mapa.", style="Info.TLabel")
                lbl_aviso.pack(fill="both", expand=True, padx=10, pady=10)
        elif self.status_geracao["dados_base"] == "carregando":
            lbl_aguarde = ttk.Label(self.frame_display, text="Os dados base ainda estão carregando.\nTente novamente em breve.", style="Info.TLabel")
            lbl_aguarde.pack(fill="both", expand=True, padx=10, pady=10)
        else:
            lbl_erro = ttk.Label(self.frame_display, text="Erro ao carregar dados base.\nNão é possível mostrar o mapa.", style="Info.TLabel")
            lbl_erro.pack(fill="both", expand=True, padx=10, pady=10)

    def mostrar_grafico(self):
        self._limpar_frame_display()
        if self.status_geracao["grafico"] == "pronto" and self.dados_carregados["graph_pil_image"]:
            self._exibir_imagem_pil_no_frame(self.dados_carregados["graph_pil_image"], "grafico")
        elif self.status_geracao["grafico"] == "carregando":
            lbl_aguarde = ttk.Label(self.frame_display, text="O gráfico ainda está sendo gerado.\nPor favor, aguarde.", style="Info.TLabel")
            lbl_aguarde.pack(fill="both", expand=True, padx=10, pady=10)
        else:
            lbl_erro = ttk.Label(self.frame_display, text="Não foi possível exibir o gráfico.\nVerifique o status ou se houve erro na geração.", style="Info.TLabel")
            lbl_erro.pack(fill="both", expand=True, padx=10, pady=10)

    def mostrar_tabela(self):
        self._limpar_frame_display()
        if self.status_geracao["dados_base"] == "pronto" and self.dados_carregados["df"] is not None:
            df = self.dados_carregados["df"]
            if df.empty:
                lbl_info = ttk.Label(self.frame_display, text="Não há dados para exibir na tabela.", style="Info.TLabel")
                lbl_info.pack(fill="both", expand=True, padx=10, pady=10)
                return

            container_tabela = ttk.Frame(self.frame_display, style="TFrame")
            container_tabela.pack(fill="both", expand=True, padx=2, pady=2)

            tree = ttk.Treeview(container_tabela, columns=list(df.columns), show="headings", style="Treeview")

            vsb = ttk.Scrollbar(container_tabela, orient="vertical", command=tree.yview)
            hsb = ttk.Scrollbar(container_tabela, orient="horizontal", command=tree.xview)
            tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

            vsb.pack(side="right", fill="y")
            hsb.pack(side="bottom", fill="x")

            for col in df.columns:
                tree.heading(col, text=col, anchor='w')
                tree.column(col, width=120, minwidth=60, anchor='w')

            for _, row in df.iterrows():
                tree.insert("", tk.END, values=[str(v) if pd.notna(v) else "" for v in row])

            tree.pack(side="left", fill="both", expand=True)
        elif self.status_geracao["dados_base"] == "carregando":
            lbl_aguarde = ttk.Label(self.frame_display, text="Os dados para a tabela ainda estão carregando.\nPor favor, aguarde.", style="Info.TLabel")
            lbl_aguarde.pack(fill="both", expand=True, padx=10, pady=10)
        else:
            lbl_erro = ttk.Label(self.frame_display, text="Não foi possível carregar os dados para a tabela.", style="Info.TLabel")
            lbl_erro.pack(fill="both", expand=True, padx=10, pady=10)

    def sair(self):
        if messagebox.askokcancel("Sair", "Deseja sair do programa?"):
            self.master.destroy()



def main():
    root_login = tk.Tk()
    LoginApp(root_login)
    root_login.mainloop()

if __name__ == "__main__":
    main()