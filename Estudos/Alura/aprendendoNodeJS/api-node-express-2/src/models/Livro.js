// Importação para o projeto
import mongoose from "mongoose";

// Construção do modelo de Autor para como vai ser seu corpo e regras de escrita
const livroSchema = new mongoose.Schema(
  {
    id: {type: String},
    titulo: {type: String, required: [true, "O titulo do livro é obrigatório"]},
    autor: {type: mongoose.Schema.Types.ObjectId, ref: "autores", required: [true, "O ID do autor é obrigatório"]},
    editora: {type: String, required: [true, "O nome da editora é obrigatório"]},
    numeroPaginas: {type: Number},
  },
);

// Referenciar o modelo com a entidade do MongoDB
const livros= mongoose.model("livros", livroSchema);

// Exportar para utilidade
export default livros;