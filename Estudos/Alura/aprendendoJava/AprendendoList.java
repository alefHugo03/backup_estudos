import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;

public class AprendendoList {
    public static void main(String[] args) {
        // O List permite valore iguais, retornando todos os valores
        List<String> funcionarios = new ArrayList<>();
        funcionarios.add("João");
        funcionarios.add("Maria");
        funcionarios.add("João");

        System.out.println(funcionarios);

        // O SET não permite valore iguaia, retornando os diferentes
        Set<String> produtos = new HashSet<>();
        produtos.add("coxinha");
        produtos.add("bolo");
        produtos.add("coxinha");

        System.out.println(produtos);


        // Com o Map ele trabalha com forme a chave do valor, ou seja, cada valor tem um identificador unico dentro para ser usado e sobreescrevido
        Map<Integer, String> clietes = new HashMap<>();
        clietes.put(1, "Maria");
        clietes.put(2, "Marcos");
        clietes.put(1, "Ana");

        System.out.println(clietes);

        // Usando funções auxiliares com stream
        List<String> pessoas = List.of("Ana", "Maria", "José");
        List<String> pessoasLetraA = pessoas.stream()
            .filter(p -> p.startsWith("A"))
            .collect(Collectors.toList());
        
        System.out.println(pessoasLetraA);


        List<Double> valoresVendas = List.of(500.0, 1800.0, 6200.0);
        List<Double> comissao = valoresVendas.stream()
            .map(v -> v * 0.05)
            .collect(Collectors.toList());

        System.out.println(comissao);

        double totalVendas = valoresVendas.stream()
            .reduce(0.0, Double::sum);
        
        System.out.println(totalVendas);

    }
}
