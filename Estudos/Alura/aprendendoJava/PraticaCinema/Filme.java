package PraticaCinema;


public class Filme {
    private final String nomeFilme;
    private String tempoFilme;
    private String generoFilme;
    private int nota = 0;
    private int quantidadeAvaliacoes = 0;


    public void adicionarAvalicao(int avaliacao) {
        if (avaliacao < 0 || avaliacao > 5) {
            System.out.printf("A nota %d é inválida, precisa ser entre 0 e 5!%n", avaliacao);
        } 
        else {
            nota += avaliacao;
            quantidadeAvaliacoes++;
            System.out.println("Avaliação adicionada com sucesso!");
        }
    }

    public void resultadoMedia(){
        if (quantidadeAvaliacoes == 0) {
            System.out.printf("%nO filme '%s' ainda não possui avaliações.%n", nomeFilme);
            return;
        }
        double media = (double) nota / quantidadeAvaliacoes;
        System.out.printf("%nMédia de avaliação do filme '%s' é de %.1f%n", nomeFilme, media);
    }


    public Filme(String nomeFilme, String tempoFilme, String generoFilme) {
        this.nomeFilme = nomeFilme;
        this.tempoFilme = tempoFilme;
        this.generoFilme = generoFilme;
    }




    public String getNomeFilme() {
        return nomeFilme;
    }




    public String getTempoFilme() {
        return tempoFilme;
    }




    public void setTempoFilme(String tempoFilme) {
        this.tempoFilme = tempoFilme;
    }




    public String getGeneroFilme() {
        return generoFilme;
    }




    public void setGeneroFilme(String generoFilme) {
        this.generoFilme = generoFilme;
    }   
}
