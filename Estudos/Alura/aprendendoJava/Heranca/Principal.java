package Heranca;

public class Principal {
    public static void main(String[] args) {
        Gerente gerente = new Gerente("Mario", 15000.0);
        gerente.exibirInformacoes();
        gerente.setBonus(1000.0);


        Desenvolvedor desenvolvedor = new Desenvolvedor("Carla", 12000, "Backend Java");
        desenvolvedor.exibirInformacoes();
    }
}
