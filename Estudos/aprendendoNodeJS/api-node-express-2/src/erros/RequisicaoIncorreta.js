// Importação do projeto
import ErroBase from "./ErroBase.js";

// Classe de repetição para mensagem de erro de requisição incorreta
class RequisicaoIncorreta extends ErroBase {
  constructor(mensagem = "Um ou mais dados fornecidos estão incorretos") {
    super(mensagem, 400);
  }
}

export default RequisicaoIncorreta;