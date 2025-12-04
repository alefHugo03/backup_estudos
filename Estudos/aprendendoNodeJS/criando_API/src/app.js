import express from 'express';
import conectaNaDataBase from './config/db_conect.js';
import livro from './models/livro.js';

const conexao = await conectaNaDataBase();

conexao.on('error', (erro) => {
    console.error('Erro de Conexão', erro)
});

conexao.once('open', () => {
    console.log('COnexão com o banco feita com sucesso')
})

const app = express();
app.use(express.json());



app.get('/', (req, res) => {
    res.status(200).send('Curso Node.js')
})

app.get('/livros',async (req, res) => {
    try {
        const listaLivros = await livro.find({});
        res.status(200).json(listaLivros);
    } catch (erro) {
        res.status(500).json({ message: `${erro.message} - falha na requisição` });
    }
})

app.get('/livros/:id', (req, res) =>{
    const index = buscaLivro(req.params.id);
    res.status(200).json(livros[index])
})



app.post('/livros', (req, res) => {
    livros.push(req.body);
    res.status(201).send('Livro cadastrado com sucesso;');

})

app.put('/livros/:id', (req, res) => {
    const index = buscaLivro(req.params.id);
    livros[index].titulo = req.body.titulo;
    res.status(200).json(livros);
});

app.delete('/livros/:id', (req, res) => {
    const index = buscaLivro(req.params.id);
    livros.splice(index, 1);
    res.status(200).send('livro removido com sucesso');
})


export default app;