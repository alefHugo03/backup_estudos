import express  from 'express'
import AutorControler from '../controlers/autorControler.js'

const routes = express.Router();

routes.get('/autores', AutorControler.listarAutores)
routes.get('/autores/:id', AutorControler.listarAutorPorId)

routes.post('/autores', AutorControler.cadastrarAutor)
routes.put('/autores/:id', AutorControler.atualizarAutor)
routes.delete('/autores/:id', AutorControler.deletarAutor)

export default routes;