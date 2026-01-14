import express  from 'express'
import LivroControler from '../controlers/livroControler.js'

const routes = express.Router();

routes.get('/livros', LivroControler.listarLivros)
routes.get('/livros/busca', LivroControler.listarLivrosPorEditor)
routes.get('/livros/:id', LivroControler.listarLivroPorId)


routes.post('/livros', LivroControler.cadastrarLivro)
routes.put('/livros/:id', LivroControler.atualizarLivro)
routes.delete('/livros/:id', LivroControler.deletarLivro)

export default routes;