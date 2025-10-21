/*  Btn Pesquisa    */
const form = document.getElementById('pesquisar');
const inputPesquisa = document.getElementById('campoPesquisa');

form.addEventListener('submit', function(event) {
  event.preventDefault();
  const valorPesquisa = inputPesquisa.value;
  alert('Você pesquisou por: ' + valorPesquisa);
});





