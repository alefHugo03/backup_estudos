import NaoEncontrado from "../erros/NaoEncontrado.js";
import livros from "../models/Livro.js";

class LivroController {

  static listarLivros = async (req, res, next) => {
    try {
      const livrosResultado = await livros.find()
        .populate("autor")
        .exec();

      if (!livrosResultado) {
        next(new NaoEncontrado("Id do Livro não localizado."));
      }
      else {
        res.status(200).json(livrosResultado);
      }
      
    } catch (erro) {
      next(erro);
    }
  };

  static listarLivroPorId = async (req, res, next) => {
    try {
      const id = req.params.id;

      const livroResultados = await livros.findById(id)
        .populate("autor", "nome")
        .exec();

      if (!livroResultados) {
        next(new NaoEncontrado("Id do Livro não localizado."));
      }
      else {
        res.status(200).send(livroResultados);
      }
      
    } catch (erro) {
      next(erro);
    }
  };

  static cadastrarLivro = async (req, res, next) => {
    try {
      const livro = new livros(req.body);

      const livroResultado = await livro.save();

      res.status(201).send(livroResultado.toJSON());
    } catch (erro) {
      next(erro);
    }
  };

  static atualizarLivro = async (req, res, next) => {
    try {
      const id = req.params.id;

      const updateId = await livros.findByIdAndUpdate(id, {$set: req.body});

      if (!updateId) {
        next(new NaoEncontrado("Id do Livro não localizado."));
      }
      else {
        res.status(200).send({message: "Livro atualizado com sucesso"});
      }
    } catch (erro) {
      next(erro);
    }
  };

  static excluirLivro = async (req, res, next) => {
    try {
      const id = req.params.id;

      const excluirLivro = await livros.findByIdAndDelete(id);

      if (!excluirLivro) {
        next(new NaoEncontrado("Id do Livro não localizado."));
      }
      else {
        res.status(200).send({message: "Livro removido com sucesso"});
      }
    } catch (erro) {
      next(erro);
    }
  };

  static listarLivroPorEditora = async (req, res, next) => {
    try {
      const editora = req.query.editora;

      const livrosResultado = await livros.find({"editora": editora});

      if (!livrosResultado) {
        res.status(200).send({message: "Livro removido com sucesso"});
      }
      else {
        res.status(200).send(livrosResultado);
      }
    } catch (erro) {
      next(erro);
    }
  };
}

export default LivroController;