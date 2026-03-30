package Polimorfismo;

public class Gerente extends Funcionario {
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

    @Override
    public void exibirInformacoes() {
        System.out.printf("Gerente: %s -- Salario: %.2f -- Bonus: %.2f\n",
            nome, salario, bonus);
    }

}
