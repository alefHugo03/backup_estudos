package POO;

public class Pratica {
    public static void main(String[] args) {
        Funcionario funcionario1 = new Funcionario();
        funcionario1.nome = "Ana";
        funcionario1.cargo = "Gerente de Projeto";
        funcionario1.salario = 2000.0;

        funcionario1.exibirInformacoes();

    }
}
