package dataHora;

import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;

public class Principal {
    public static void main(String[] args) {

        /* Formatador da data para o do Brasil */
        DateTimeFormatter formato = DateTimeFormatter.ofPattern("dd/MM/yyyy");

        /* Status do pagamento */
        String status = "Em Aberto";

        /* Operadores de data */
        LocalDate diaHoje = LocalDate.now();
        LocalDate dataCompra = LocalDate.of(2026, 1, 1);
        LocalDate dataPrimeiraParcela = LocalDate.of(2026, 1, 21);
        LocalDate dataSegundaParcela = dataPrimeiraParcela.plusDays(15);


        /* Sem precisar formatar a data (Pegando o estilo de data da região) */
        ZonedDateTime dataConclusaoCompra = ZonedDateTime.now();

        /* Textos para ser enviados */
        String texto0 = String.format("***************************\nData de hoje - %s\n***************************\n", diaHoje);  
        String texto1 = String.format("Data da compra - %s\n", dataCompra.format(formato));
        String texto2 = String.format("Data da primeira parcela - %s\n", dataPrimeiraParcela.format(formato));
        String texto3 = String.format("Data da segunda parcela - %s\n", dataSegundaParcela.format(formato));

        /* Retorna:
        2026-01-21T17:23:48.338971397-03:00[America/Sao_Paulo] */
        String texto4 = String.format("Data de conclusão da compra - %s\n", dataConclusaoCompra);
        
        /* Saida das datas de pagamento e compra */
        System.out.println(texto0);
        System.out.println(texto1);
        System.out.println(texto2);
        System.out.println(texto3);
        System.out.println(texto4);
        

        /* Condições do primeiro pagamento */
        if (dataPrimeiraParcela.isEqual(diaHoje) || dataPrimeiraParcela.isAfter(diaHoje) || dataPrimeiraParcela.isBefore(diaHoje) && status.equalsIgnoreCase("Pago")) {
            System.out.println("SUA PARCELA ESTÁ PAGA! STATUS: "+status);
        }

        if (dataPrimeiraParcela.isEqual(diaHoje) && status.equalsIgnoreCase("Em Aberto")) {
            System.out.println("HOJE É O DIA DO PAGAMENTO DA PARCELA!");
        }
        
        if (dataPrimeiraParcela.isBefore(diaHoje) || dataPrimeiraParcela.isEqual(diaHoje) && status.equalsIgnoreCase("Atrasado")) {
            System.out.println("A PARCELA ESTÁ ATRASADA! STATUS: "+status);
        }

        if (dataPrimeiraParcela.isAfter(diaHoje) && status.equalsIgnoreCase("Em Aberto")) {
            System.out.println("NÃO É DIA DE VENCIMENTO DA PARCELA! STATUS: "+status);
        }


        
    }
}
