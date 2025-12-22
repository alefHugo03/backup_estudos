// Importação do projeto
import ErroBase from "./ErroBase.js";

// Classe de repetição para mensagem de erro não encontrado
class NaoEncontrado extends ErroBase {
  constructor(mensagem = "Pagina não encontrada") {
    super(mensagem, 404);
  }
}

// Exportar para aplicação
export default NaoEncontrado;