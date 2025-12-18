import mongoose from "mongoose";


function manipularErros(erro, _req, res, _next){
  if (erro instanceof mongoose.Error.CastError) {
    res.status(400).send({ message: "Um ou mais dados fornecidos estão incorretos"});
  } 
  else if (erro instanceof mongoose.Error.ValidationError) {
    const messageError = Object.values(erro.errors)
      .map(erro => erro.message)
      .join("; ");
    res.status(400).send({ message: `Os seguintes erros foram encontrados: ${messageError}`});
  } 
  else {
    res.status(500).send({message: "Erro interno de servidor" }); 
  };
}


export default manipularErros;