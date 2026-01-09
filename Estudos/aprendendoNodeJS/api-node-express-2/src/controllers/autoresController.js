// Importações para o projeto
import NaoEncontrado from "../erros/NaoEncontrado.js";
import autores from "../models/Autor.js";

// Classe para utilidade do autor
class AutorController {

  static listarAutores = async(req, res, next) => {
    try {
      const autoresResultado = await autores.find();

      if (!autoresResultado) {
        next(new NaoEncontrado("Id do Autor não localizado."));
      }
      else {
        res.status(200).json(autoresResultado);
      }
    } catch (erro) {
      next(erro);
    }
  };

  static listarAutorPorId = async (req, res, next) => {
    
    try {
      const id = req.params.id;
  
      const autorResultado = await autores.findById(id);

      if (autorResultado !== null) {
        res.status(200).send(autorResultado);
      } else {
        next(new NaoEncontrado("Id do Autor não localizado."));
      }
    } catch (erro) {
      next(erro);
    }
  };
  
  
  static cadastrarAutor = async (req, res, next) => {
    try {
      const autor = new autores(req.body);
  
      const autorResultado = await autor.save();
  
      res.status(201).send(autorResultado.toJSON());
    } catch (erro) {
      next(erro);
    }
  };
  

  static atualizarAutor = async (req, res, next) => {
    try {
      const id = req.params.id;
  
      const updateAutor = await autores.findByIdAndUpdate(id, {$set: req.body});

      if (!updateAutor) {
        next(new NaoEncontrado("Id do Autor não localizado."));
      }
      else {
        res.status(200).send({message: "Autor atualizado com sucesso"});
      }
    } catch (erro) {
      next(erro);
    }
  };
  
  static excluirAutor = async (req, res, next) => {
    try {
      const id = req.params.id;
  
      const deletarAutor = await autores.findByIdAndDelete(id);

      if (!deletarAutor) {
        next(new NaoEncontrado("Id do Autor não localizado."));
      }
      else {
        res.status(200).send({message: "Autor removido com sucesso"});
      }
    } catch (erro) {
      next(erro);
    }
  };
  

}

// Exportar para aplicação
export default AutorController;