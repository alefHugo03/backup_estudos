package PraticaCinema;

import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        Filme meuFilme = new Filme("Roberto Carlos", "2 hrs", "Romance");
        
        Scanner scanner = new Scanner(System.in);
        
        while(true){
            System.out.println("\nBem vindo ao cinemation, qual das opções você deseja saber?");
            System.out.println("filme | avaliar | media | sair");
            String escolha = scanner.nextLine();

            if (escolha.equalsIgnoreCase("filme")) {
                System.out.printf("\nFilme: %s%n", meuFilme.getNomeFilme());
                System.out.printf("Gênero: %s%n", meuFilme.getGeneroFilme());
                System.out.printf("Duração: %s%n", meuFilme.getTempoFilme());

            } else if (escolha.equalsIgnoreCase("avaliar")) {
                System.out.println("Qual a sua avaliação para o filme (0 a 5)?");
                int numero = scanner.nextInt();
                scanner.nextLine();
                meuFilme.adicionarAvalicao(numero);

            } else if (escolha.equalsIgnoreCase("media")) {
                meuFilme.resultadoMedia();

            } else if (escolha.equalsIgnoreCase("sair")) {
                System.out.println("Saindo do programa...");
                break;

            } else {
                System.out.println("Opção inválida. Escolha apenas uma das opções informadas.");
            }
        }
        scanner.close();
    }
}
