import java.util.InputMismatchException;
import java.util.Scanner;

public class Loops {
    public static void main(String[] args) {
        // Sistema com for
        String[] vendedores = {"Alef", "Larissa", "Hevy"};
        double[] vendas = {4000.0, 2050.4, 657.2};

        for (int i = 0; i < vendedores.length; i++) {
            System.out.printf("Vendador(a) %s - comissão %.2f\n", vendedores[i],
                 calcularComissao(vendas[i]));

        }

        // Sistema com While
        int j = 0;
        boolean imprimeOutro = true;
        try (Scanner leitura = new Scanner(System.in)){
            while (imprimeOutro) { 
                System.out.printf("Vendador(a) %s - comissão %.2f\n", vendedores[j],
                    calcularComissao(vendas[j]));
                ++j;
                System.out.println("Deseja imprimir outro?");
                imprimeOutro = leitura.nextBoolean();
            }
            leitura.close();
        } 
        catch (InputMismatchException e) {
            System.out.println("Erro! Você deveria ter digitado true ou false.");
        } 
        catch(Exception e) {
            System.out.println("Ocorreu um erro inesperado: " + e.getMessage());
        } 
    }

    public static double calcularComissao(double totalVendas) {
        if (totalVendas <= 3000) {
            return totalVendas * 0.03;
        }
        else {
            return totalVendas * 0.06;
        }
    }
}