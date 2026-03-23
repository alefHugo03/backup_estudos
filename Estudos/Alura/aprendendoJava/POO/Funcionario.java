package POO;

public class Funcionario {
    String nome;
    String cargo;
    double salario;

    public void exibirInformacoes() {
        System.out.printf("Funcionario: %s  --  Cargo: %s -- Salario: %.2f", nome, cargo, salario);
    }

    public void ajustarSalario(double percentual) {
        salario += salario * (percentual / 100);
        System.out.printf("\nNovo Salário de %s é %.2f", nome, salario);
    }
}
