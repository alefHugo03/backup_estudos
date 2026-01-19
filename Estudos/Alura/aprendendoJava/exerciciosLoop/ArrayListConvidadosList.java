package exerciciosLoop;

import java.util.ArrayList;
import java.util.Scanner;

public class ArrayListConvidadosList {
    public static void main(String[] args) {
        ArrayList<String> convidadosLista= new ArrayList<>();

        try (Scanner scanner = new Scanner(System.in)) {
            while (true) {
                System.out.println("\nBom dia! Bem vindo a festa");
                System.out.println("Digite 'ver' para ver a lista ou 'sair' para sair");

                String nome = scanner.nextLine().trim();

                if (!continuar(nome)) {
                    System.out.println("Saindo...");
                    break;
                }

                System.out.println("Lista da Festa:" + convidadosLista);

            }
        }
    }
    public static boolean continuar(String nome) {
        return !nome.equalsIgnoreCase("sair");
    }

}
