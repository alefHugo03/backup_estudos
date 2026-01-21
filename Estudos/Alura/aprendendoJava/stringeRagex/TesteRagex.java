package stringeRagex;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class TesteRagex {
    public static void main(String[] args) {
        
        String texto = "Meu email é alef65507@gmail.com";

        Pattern pattern = Pattern.compile("\\w+@\\w+.\\w+");

        Matcher matcher = pattern.matcher(texto);

        if (matcher.find()){
            System.out.println(matcher.group());
        }


    }
}
