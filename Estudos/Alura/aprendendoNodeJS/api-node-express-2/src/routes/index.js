//Importações do projeto
import express from "express";
import livros from "./livrosRoutes.js";
import autores from "./autoresRoutes.js";

// Pré carregar pagina padrão e retornar respostas das outras rotas
const routes = (app) => {
  app.route("/").get((req, res) => {
    res.status(200).send({titulo: "Curso de node"});
  });

  app.use(
    express.json(),
    livros,
    autores,
  );
};

// Exportar essa aplicação para o app.js
export default routes;