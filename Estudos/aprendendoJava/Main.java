public class Main {
    public static void main (String[] args) {
        /* Primeiras aplicações usadas do Java */

        // System.out.println("Esse é o Screen Match");
        // System.out.println("Filme:Top Gun: Maverick");

        // int anoDeLancamento = 2022;
        // System.out.println("Ano de Lançamento: " + anoDeLancamento);

        // boolean inclusoNoPlano = false;

        // double media = (8.1 + 9.8 + 7.5) / 3;
        // System.out.println(media);

        // String sinopse = """
        // Filme de aventura e ação
        // Ano de Lançamento: 2022
        // """;
        // System.out.println(sinopse);

        /* Inserindo variaveis dentro da conversa */

        int anoDeLancamento = 2022;

        String nomeDoFilme = "Top Gun: Maverick";

        double media = 8.1 + 9.8 + 7.5;
        int classificacao = (int) (media / 3);

        System.out.println(String.format("""

        O filme %s, lançado em %d

        Possui a nota de %d no meu site
        """,  
        nomeDoFilme, anoDeLancamento, classificacao));

        
    };
}