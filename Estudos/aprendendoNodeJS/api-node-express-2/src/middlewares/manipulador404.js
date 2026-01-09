// Importação do projeto
import NaoEncontrado from "../erros/NaoEncontrado.js";

// Preparação para a apresentação da mensagem de erro
function manipulador404 (req, res, next) {
  const erro404 = new NaoEncontrado();
  next(erro404);
}

// Exportar para aplicação
export default manipulador404;