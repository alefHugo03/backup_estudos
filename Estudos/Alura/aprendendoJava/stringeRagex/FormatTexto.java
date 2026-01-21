package stringeRagex;

public class FormatTexto {

    public static void main(String[] args) {
        String nome = "Alef";
        String disciplina = "Arquitetura de Software";

        String texto = String.format("Documento:  %s - %s", nome, disciplina);
        System.out.println(texto);
    }
}
