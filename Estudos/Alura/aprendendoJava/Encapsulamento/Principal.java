package Encapsulamento;

public class Principal {
    public static void main(String[] args) {
        Funcionario funcionario1 = new Funcionario("João", 8000.0);
        funcionario1.setCargo("Desenvolvedor");

        System.out.println("Nome do funcionario: " + funcionario1.getNome());
        System.out.println("\nFuncionario tem o cargo: " + funcionario1.getCargo());

        System.out.println("\nSalario do funcionario: " + funcionario1.getSalario());

        funcionario1.exibirInformacoes();

        funcionario1.ajustarSalario(5);

        funcionario1.ajustarSalario(5);

    }
}
