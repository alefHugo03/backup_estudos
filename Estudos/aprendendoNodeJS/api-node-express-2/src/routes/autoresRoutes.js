// Importações para o projeto
import express from "express";
import AutorController from "../controllers/autoresController.js";

// Usar utilidade para preparar uma rota da URL
const router = express.Router();

// Todas as rotas após o localhost:3000 referente a funções de autores
router
  .get("/autores", AutorController.listarAutores)
  .get("/autores/:id", AutorController.listarAutorPorId)
  .post("/autores", AutorController.cadastrarAutor)
  .put("/autores/:id", AutorController.atualizarAutor)
  .delete("/autores/:id", AutorController.excluirAutor);


// Exportar a rota
export default router;   