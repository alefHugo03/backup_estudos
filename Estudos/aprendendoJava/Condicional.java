public class Condicional {
    public static void main(String[] args) {

        int anoDeLancamento = 2022;
        String nomeDoFilme = "Top Gun: Maverick";

        double media = 8.1 + 9.8 + 7.5;
        int classificacao = (int) (media / 3);

        boolean incluidoNoPlano = false;
        String tipoPlano = "plus";


        if (anoDeLancamento >= 2022) {
            System.out.println("Lançamentos Recentes");
        } else{
            System.out.println("Filmes Clássicos");
        }

        if (incluidoNoPlano == true && tipoPlano.equals("plus")) {
            System.out.println("Filme incluso no plano");
        } else if (incluidoNoPlano == true && tipoPlano.equals("basic")) {
            System.out.println("Filme incluso no plano básico com propagandas");
        } else {
            System.out.println("Filme não incluso no plano");

        }

 
    }
}
