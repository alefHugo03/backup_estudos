// Importações para o projeto
import RequisicaoIncorreta from "./RequisicaoIncorreta.js";

// Classe de repetição para mensagem de erro de validação
class ErroValidacao extends RequisicaoIncorreta {
  constructor(erro) {
    const messageError = Object.values(erro.errors)
      .map(erro => erro.message)
      .join("; ");
    super(`Os seguintes erros foram encontrados: ${messageError}`);
  }
}

// Exportar para aplicação
export default ErroValidacao;