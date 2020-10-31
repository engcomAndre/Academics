package ponteestreita.ponte;

import java.util.LinkedHashSet;
import java.util.logging.Level;
import java.util.logging.Logger;

import ponteestreita.carro.Carro;
import ponteestreita.carro.Sentido;

import java.util.concurrent.Semaphore;

/**
 * Está classe representa a Ponte.
 *
 * @version 05/10/2017
 */

public class Ponte {


    private static final int CAPACITY = 3;

    private static Ponte instance = new Ponte(CAPACITY);

    private Sentido atualSentido;

    private final int capacidade;
    
    private int esperandoPrioridade;
    
    private int esperandoNormal;
    
    private int maisLento;

    private LinkedHashSet<Carro> carros;

    private Semaphore semaforo;
    private Semaphore saiuMutex;
    private Semaphore entrouMutex;
    private Semaphore esperaPrioridade;
    private Semaphore esperaNormal;

    public Ponte(int capacidade) {
        this.capacidade = capacidade;
        this.atualSentido = Sentido.NONE;
        this.carros = new LinkedHashSet<>();
        this.esperandoPrioridade = 0;
        this.esperandoNormal = 0;
        this.semaforo = new Semaphore(this.capacidade, true);
        this.saiuMutex = new Semaphore(1, true);
        this.entrouMutex = new Semaphore(1, true);
        this.esperaPrioridade = new Semaphore(0, true);
        this.esperaNormal = new Semaphore(0, true);
    }

    public static Ponte getInstance() {
        return instance;
    }

    public void addCarro(Carro carro) {
        try {
            this.semaforo.acquire();
        } catch (InterruptedException ex) {
            Logger.getLogger(Ponte.class.getName())
                    .log(Level.SEVERE, null, ex);
        }

        if (this.isEmpty()) {
            this.atualSentido = carro.getSentido();
            this.maisLento = carro.getTempoDepoisTravessia();
        }
       
        if (!this.estaCheia() && !this.carros.contains(carro)
                && getAtualSentido().equals(carro.getSentido())) {
            try {
                this.entrouMutex.acquire();
            } catch (InterruptedException ex) {
                Logger.getLogger(Ponte.class.getName())
                        .log(Level.SEVERE, null, ex);
            }
         
            if (this.carros.add(carro)) {
                System.out.println(carro.getName() + " Está atravessando ponte para o " + carro.getSentido());
            }
            
            this.entrouMutex.release();
            
            if (this.estaCheia()) {
                System.out.println("A Ponte está cheia");
            }
        }
    }
    
    public void esperaCarroPrioridade(Carro carro) {
    	 try {
    		 System.out.println(carro.getName() + " Está esperando.");
    		 this.esperandoPrioridade++;
             this.esperaPrioridade.acquire();
         } catch (InterruptedException ex) {
             Logger.getLogger(Ponte.class.getName())
                     .log(Level.SEVERE, null, ex);
         }  
    }
    
    public void esperaCarroNormal(Carro carro) {
   	 try {
   		 System.out.println(carro.getName() + " Está esperando.");
   		 this.esperandoNormal++;
            this.esperaNormal.acquire();
        } catch (InterruptedException ex) {
            Logger.getLogger(Ponte.class.getName())
                    .log(Level.SEVERE, null, ex);
        }
   }
    
    public void removeCarro(Carro carro) {
        this.semaforo.release();
     
        if (!this.isEmpty()) {
            try {
                this.saiuMutex.acquire();
            } catch (InterruptedException ex) {
                Logger.getLogger(Ponte.class.getName())
                        .log(Level.SEVERE, null, ex);
            }
            if (this.carros.remove(carro)) {
                System.out.println(carro.getName() + " Saiu da ponte");
            }
            this.saiuMutex.release();
        
            if (this.isEmpty()) {
                System.out.println("A ponte está vazia");
                this.atualSentido = Sentido.NONE;
                if (esperandoPrioridade > 0) {
                	this.esperaPrioridade.release(this.esperandoPrioridade);
                    this.esperandoPrioridade = 0;
                } else {
                	this.esperaNormal.release(this.esperandoNormal);
                    this.esperandoNormal = 0;
                }
            }
        }
    }
    
    public boolean estaNaPonte(Carro carro) {
        return this.carros.contains(carro);
    }
    
    
    public boolean isEmpty() {
        return this.carros.isEmpty();
    }
    
    public boolean estaCheia() {
        return this.capacidade == this.carros.size();
    }
    
    public Sentido getAtualSentido() {
        return this.atualSentido;
    }
    
    public int getMaisLento() {
        return this.maisLento;
    }
    
    public int getEsperandoPrioridade() {
        return this.esperandoPrioridade;
    }

    @Override
    public String toString() {
        return "Ponte{" + "atualSentido = " + this.atualSentido
                + ", capacidade = " + this.capacidade
                + ", numberOfCarros = " + this.carros.size() + '}';
    }

}
