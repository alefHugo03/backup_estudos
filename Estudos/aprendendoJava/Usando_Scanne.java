import java.util.Scanner;

public class Usando_Scanne {
    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in); 
        int numero = scanner.nextInt(); 
        scanner.close();
        System.out.println("Você Digitou: " + numero);
    }
}