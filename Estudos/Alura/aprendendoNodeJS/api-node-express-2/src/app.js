// Importações para o projeto
import express from "express";
import db from "./config/dbConnect.js";
import routes from "./routes/index.js";
import manipularErros from "./middlewares/manipuladorDeErros.js";
import manipulador404 from "./middlewares/manipulador404.js";

// Teste da conexão com o MongoDB Atlas
db.on("error", console.log.bind(console, "Erro de conexão"));
db.once("open", () => {
  console.log("conexão com o banco feita com sucesso");
});

// Configurar as rotas geradas como o express 
const app = express();
app.use(express.json());
routes(app);

// Após o carregamento do servidor, preparar as mensagens de erro 
app.use(manipulador404);

app.use(manipularErros);

// Exportar a aplicação para usar no server.js
export default app;