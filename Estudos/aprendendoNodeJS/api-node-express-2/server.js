// Importar para aplicação
import "dotenv/config";
import app from "./src/app.js";

// Preparação para porta onde vai conversar
const port = process.env.PORT || 3000;

// Preparar para ouvir tudo que vier da porta
app.listen(port, () => {
  console.log(`Servidor escutando em http://localhost:${port}`);
});