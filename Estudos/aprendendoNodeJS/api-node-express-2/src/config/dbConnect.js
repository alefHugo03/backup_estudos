// IMportação para o projeto
import mongoose from "mongoose";

// Conectar a aplicação com o mongoDB com uma conexão
mongoose.connect(process.env.DB_CONECT_MONGO);

const db = mongoose.connection;

// Exportar essa conexão
export default db;