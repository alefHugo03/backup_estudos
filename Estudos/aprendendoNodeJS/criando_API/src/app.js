import express from 'express';
import conectaNaDataBase from './config/db_conect.js';
import routes from './routes/index.js'

const conexao = await conectaNaDataBase();

conexao.on('error', (erro) => {
    console.error('Erro de Conexão', erro)
});

conexao.once('open', () => {
    console.log('COnexão com o banco feita com sucesso')
})

const app = express();

routes(app);


export default app;