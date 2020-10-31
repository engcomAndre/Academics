package ponteestreita.carro;

import ponteestreita.ponte.Ponte;

/**
 * Está classe respresenta o carro.
 *
 * @version 05/10/2017
 */
public class Carro implements Runnable {

    private final String id;

    private Sentido sentido;

    private final Ponte ponte;

    private final int tempoTravessia;
    
    private final int tempoDepoisTravessia;

    private boolean podeSair;

    private boolean querEntarNaPonte;
    
    private final Sentido prioridade;

    public Carro(Sentido prioridade, String id, Sentido sentido, Ponte ponte, int tempoTravessia, int tempoDepoisTravessia) {
        this.id = id;
        this.sentido = sentido;
        this.ponte = ponte;
        this.tempoTravessia = tempoTravessia;
        this.tempoDepoisTravessia = tempoDepoisTravessia;
        this.prioridade = prioridade;
        this.podeSair = false;
        this.querEntarNaPonte = true;
    }

    public void usePonte() {
    
        this.ponte.addCarro(this);
        if (this.ponte.estaNaPonte(this)) {
        		
        	long tempoFinalDurante = System.currentTimeMillis() + this.getTempoTravessia()*1000;
            	
            while(System.currentTimeMillis() <= tempoFinalDurante);
        }
        	
            this.podeSair = true;
            
			System.out.println(getName() + " Atravessou");
			
			System.out.println(this.getName() + " vai passear por " + this.getTempoDepoisTravessia() + "s");
			
			long tempoFinalDepois = System.currentTimeMillis() + this.getTempoDepoisTravessia()*1000;
        	
        	while(System.currentTimeMillis() <= tempoFinalDepois);
        	
        	if(this.getSentido().equals(Sentido.LESTE)) {
        		this.setSentido(Sentido.OESTE);
        	} else {
        		this.setSentido(Sentido.LESTE);
        	}		
        }
    
    public void esperaPrioridade() {
    	this.ponte.esperaCarroPrioridade(this);
    }
    
    public void esperaNormal() {
    	this.ponte.esperaCarroNormal(this);
    }

    public void saiDaPonte() {

        this.ponte.removeCarro(this);
        this.podeSair = false;
        //this.querEntarNaPonte = false;
    }

    public String getName() {
        return this.id;
    }

    public Sentido getSentido() {
        return this.sentido;
    }
    
    public void setSentido(Sentido sentido) {
	    this.sentido = sentido;
	}
    
    public int getTempoTravessia() {
		return tempoTravessia;
	}
    
    public int getTempoDepoisTravessia() {
		return tempoDepoisTravessia;
	}
    
    public Sentido getPrioridade() {
		return prioridade;
	}
    
    public int desaceleracao(int tempo1, int tempo2) {
    	int dS1 = (tempo1 + tempo2)/2;
    	int dS2 = tempo1;
    	return dS1;
    }

    @Override
    public void run() {
        System.out.println(this.getName() + " em " + this.getTempoTravessia() + "s");
    
        while (this.querEntarNaPonte) {
       
            if ((this.ponte.getAtualSentido().equals(this.getSentido())
                    || this.ponte.getAtualSentido().equals(Sentido.NONE))
            		&& !this.ponte.estaCheia()
                    && !this.ponte.estaNaPonte(this) 
                    && (this.ponte.getEsperandoPrioridade() == 0)) {
            	
                this.usePonte();
                
            } else if (this.getSentido().equals(this.getPrioridade())) {
            	
            	this.esperaPrioridade();
            	
            }else {
        
            	this.esperaNormal();
            	
            }

            if (this.podeSair) {
                this.saiDaPonte();
            }
        }
    }

    @Override
    public String toString() {
        return "Carro{" + "id = " + this.id + ", sentido = " + this.sentido + ", tempoTravessia = " + this.tempoTravessia +  ", tempoDepoisTravessia = " + this.tempoDepoisTravessia + "}";
    }

}
