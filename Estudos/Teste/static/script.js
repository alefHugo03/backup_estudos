let allBooks = []; // Variável para armazenar todos os livros

// Função para renderizar os livros na tela
function renderBooks(books) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = ''; // Limpa os resultados anteriores

    if (books.length === 0) {
        resultsDiv.innerHTML = '<p>Nenhum livro encontrado.</p>';
        return;
    }

    books.forEach(book => {
        const bookElement = document.createElement('div');
        bookElement.classList.add('book-item');
        bookElement.innerHTML = `
            <a href="book.html?id=${book.id}"><h3>${book.titulo}</h3></a>
            <p>Autor: ${book.autor}</p>
        `;
        resultsDiv.appendChild(bookElement);
    });
}

// Função para buscar os livros na API
async function fetchBooks() {
    try {
        // A API está rodando na porta 5001
        const response = await fetch('http://127.0.0.1:5001/api/books');
        allBooks = await response.json();
        renderBooks(allBooks); // Exibe todos os livros ao carregar
    } catch (error) {
        console.error('Erro ao buscar os livros:', error);
        document.getElementById('results').innerHTML = '<p>Não foi possível carregar os livros. Verifique se a API está rodando.</p>';
    }
}

// Função de pesquisa chamada pelo botão
function searchBooks() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    const filteredBooks = allBooks.filter(book => 
        book.titulo.toLowerCase().includes(searchTerm) || 
        book.autor.toLowerCase().includes(searchTerm)
    );
    renderBooks(filteredBooks);
}

// Busca os livros assim que a página é carregada
document.addEventListener('DOMContentLoaded', fetchBooks);