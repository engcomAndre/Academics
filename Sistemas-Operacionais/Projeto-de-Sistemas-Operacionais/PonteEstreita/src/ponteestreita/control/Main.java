package ponteestreita.control;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;

import ponteestreita.carro.Carro;
import ponteestreita.carro.Sentido;
import ponteestreita.ponte.Ponte;

/**
 * Esta é a classe principal.
 *
 * @version 05/10/2017
 */
public class Main {

    public static void main(String[] args) {

        Ponte ponte = Ponte.getInstance();

        List<Carro> carros = new ArrayList<>();

        for (int i = 0; i < ((new Random()).nextInt(5)+3); i++) {

            if (new Random().nextInt(2) == 0) {
                carros.add(new Carro(Sentido.LESTE, ("Carro Leste#" + ((new Random()).nextInt(30)+10) + i), Sentido.LESTE, ponte, ((new Random()).nextInt(10)+5), ((new Random()).nextInt(10)+5)));
            } else {
                carros.add(new Carro(Sentido.LESTE, ("Carro Oeste#" + ((new Random()).nextInt(30)+10) + i), Sentido.OESTE, ponte, ((new Random()).nextInt(10)+5), ((new Random()).nextInt(10)+5)));
            }
        }

        carros.stream().map((Carro) -> new Thread(Carro)).forEach((t) -> {
            t.start();
        });
       
        carros.stream().map((Carro) -> new Thread(Carro)).forEach((t) -> {
            try {
                t.join();
            } catch (InterruptedException ex) {
                Logger.getLogger(Main.class.getName()).log(Level.SEVERE, null, ex);
            }
        });
    }
}
