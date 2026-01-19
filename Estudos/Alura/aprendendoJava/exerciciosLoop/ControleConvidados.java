package exerciciosLoop;

import java.util.ArrayList;
import java.util.Scanner;

public class ControleConvidados {
    public static void main(String[] args) {
        boolean imprimeOutro = false;
        String[] convidados = new String[10];



        int quantidade = 0;
        try (Scanner convidadosScanner = new Scanner(System.in)){
            do {
                System.out.println("Bom dia! Bem vindo a festa, veja a nossa lista de convidados presentes:");
                forEach(convidados);
                

                System.out.println("Por favor, digite seu nome ou digite sair para sair");
                String nome = convidadosScanner.next();

                if (nome.equalsIgnoreCase("sair")) {
                    imprimeOutro = false;
                    break;
                }

                if (!naoExiste(nome, convidados)) {
                    System.out.println("**********************");
                    System.out.println("Esse nome já está na lista!!");
                    System.out.println("**********************");
                    continue;
                }
                if (quantidade < convidados.length) {
                    convidados[quantidade] = nome;
                    quantidade++;
                } else {
                    System.out.println("Lista de convidados cheia!");
                }

                System.out.println("**********************");
                System.out.println("Obrigado por participar!\n");
                System.out.println("**********************");
            
                imprimeOutro = true;
            

            } while (imprimeOutro);
        }
        scanner.close();
    }
    public static boolean naoExiste(String nome, String[] convidados){
        for (String convidado: convidados) {
            if (nome.equalsIgnoreCase(convidado)) {
                return false;
            }
        }
        return true;
    }

    public static void forEach(String[] convidados){
        for (String convidado : convidados){
            if (convidado != null) {
                System.out.println(convidado);
            }
        }
    }
}
