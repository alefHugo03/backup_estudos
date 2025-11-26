public class Testando_atividades {
    public static void main (String[] args) {
    /* Calculando média */
        double nota1 =  7.5;
        double nota2 = 8.0;
        double nota3 = 9.0;

        double media = (nota1 + nota2 + nota3)/3;

        System.out.println(media);

    /* Conversão de celcius para Fahrenheit  */
    int celcius = 20;
    double fahrenheit = (celcius * 9/5) + 32;
    System.out.println("Sua temperatura em Fahrenheit é: " + fahrenheit);

    /* Escrevendo banco de livros */
 
    String titulo = "O Pequeno Príncipe";
    String autor = "Antoine de Saint-Exupéry";
    int paginas = 96;
    double preco = 39.90;
    char categoria = 'F';

    String categoriaDescricao;

    if (categoria == 'F') {
        categoriaDescricao = "Ficção";
    } else if (categoria == 'N') {
        categoriaDescricao = "Não-ficção";
    } else if (categoria == 'T') {
        categoriaDescricao = "Tecnologia";
    } else if (categoria == 'H') {
        categoriaDescricao = "História";
    } else {
        categoriaDescricao = "Categoria inválida";
    }

    System.out.println("Livro cadastrado: \"" + titulo + "\", de " + autor + ". Ele possui " + paginas + " páginas, custa R$" + preco + " e pertence à categoria " + categoriaDescricao + ".");
    }
}
