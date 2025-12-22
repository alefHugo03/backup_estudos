// Importações para o projeto
import express from "express";
import LivroController from "../controllers/livrosController.js";

// Usar utilidade para preparar uma rota da URL
const router = express.Router();

// Todas as rotas após o localhost:3000 referente a funções de livros
router
  .get("/livros", LivroController.listarLivros)
  .get("/livros/busca", LivroController.listarLivroPorEditora)
  .get("/livros/:id", LivroController.listarLivroPorId)
  .post("/livros", LivroController.cadastrarLivro)
  .put("/livros/:id", LivroController.atualizarLivro)
  .delete("/livros/:id", LivroController.excluirLivro);

// Exportar a rota
export default router;   