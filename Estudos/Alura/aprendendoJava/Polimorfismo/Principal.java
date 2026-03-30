package Polimorfismo;

public class Principal {
    public static void main(String[] args) {
        Funcionario gerente = new Gerente("Mario", 15000);
        ((Gerente) gerente).setBonus(2000); 
        gerente.exibirInformacoes();
        
        


        Funcionario desenvolvedor = new Desenvolvedor("Carla", 12000, "Backend Java");
        desenvolvedor.exibirInformacoes();
    }
}
