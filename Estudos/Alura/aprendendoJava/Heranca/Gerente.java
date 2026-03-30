package Heranca;

import Encapsulamento.Funcionario;

public class Gerente extends  Funcionario {
    private double bonus;

    public double getBonus() {
        return bonus;
    }
    public void setBonus(double bonus) {
        this.bonus = bonus;
    }

    // Super construtor
    public Gerente (String nome, double salario) {
        super(nome, salario);
    }
}
