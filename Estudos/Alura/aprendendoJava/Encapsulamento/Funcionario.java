package Encapsulamento;

public class Funcionario {
    // Atributos privados
    private final String nome;
    private String cargo;
    private double salario;
    private int controleReajuste = 0;
    
    //  Criando os Getters e Setter para encapsular valores privados

    public String getNome() {
        return nome;
    }

    public double getSalario() {
        return salario;
    }

    public String getCargo() {
        return cargo;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    
    // Exibir informações gerais
    

    public void exibirInformacoes() {
        System.out.printf("Funcionario: %s  --  Cargo: %s -- Salario: %.2f\n", nome, cargo, salario);
    }

    // Corrigir salário de forma segura
    public void ajustarSalario(double percentual) {
        if(controleReajuste >=1) {
            System.out.println("\nNão pode mais fazer reajustes");
        }
        else {
        salario += salario * (percentual / 100);
        System.out.printf("\nNovo Salário de %s é %.2f\n", nome, salario);
        }

        controleReajuste++;
    }

    // Construtor para encapsular
    public Funcionario(String nome, double salario) {
        this.nome = nome;
        this.salario = salario;
    }
}
