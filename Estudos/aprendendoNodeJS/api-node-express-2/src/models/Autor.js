// Importação para o projeto
import mongoose from "mongoose";

// Construção do modelo de Autor para como vai ser seu corpo e regras de escrita
const autorSchema = new mongoose.Schema(
  {
    id: {type: String},
    nome: {type: String, required: [true, "O nome do(a) autor(a) é obrigatório"]},
    nacionalidade: {type: String},
  },
  {
    versionKey: false,
  },
);

// Referenciar o modelo com a entidade do MongoDB
const autores = mongoose.model("autores", autorSchema);

// Exportar para utilidade
export default autores;