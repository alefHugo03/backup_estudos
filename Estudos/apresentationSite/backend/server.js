const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

// =======================================================
// ▼▼▼ ADICIONE ESTA LINHA AQUI ▼▼▼
// Diz ao Express para servir os arquivos da pasta 'public'
// =======================================================
app.use(express.static('public'));

// ROTA DE LOGIN (continua igual)
app.post('/login', (req, res) => {
    const { email, senha } = req.body;
    console.log(`Requisição recebida! Email: ${email}, Senha: ${senha}`);

    if (!email || !senha) {
        return res.status(400).json({ mensagem: "Email e senha são obrigatórios!" });
    }
    
    res.status(200).json({ mensagem: `Login bem-sucedido para o email: ${email}` });
});

// INICIA O SERVIDOR (continua igual)
app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}. Acesse http://localhost:${PORT}`);
});