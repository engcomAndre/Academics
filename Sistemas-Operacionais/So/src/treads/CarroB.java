package treads;

import java.util.Random;

public class CarroB extends Thread{
	Random randint = new Random();
	public int idCarro;	
	public int tempoTravessia;	//tempo de travessia na ponte;
	public int tempoEspera;		//tempo de espera na ponte deve tentar atravessar caso 0;
	public int  sentido;
	
	public CarroB(int sentido) {
		super();
		this.idCarro = Main.idcarros++;				
		this.tempoTravessia = 5;
		this.tempoEspera = randint.nextInt(9);
		this.sentido = sentido;		
	}
	
	public void codigoRegiaoCritica() {
		System.out.printf("Ponte : %s\n",Main.fila_Ponte.size());		
		Main.fila_Ponte.addLast(Main.fila_B.removeFirst());
		System.out.printf("Carro B %d add na ponte\n",this.idCarro);
		int num = 4;

		while(this.tempoTravessia > -1) {
			if(Main.fila_Ponte.size() < num){
				while(num > 0){
					Main.up_B();
					num--;
				}
			}
			System.out.printf ("Carro B : %d Posicao : %d\n",this.idCarro,this.tempoTravessia);
			tempoTravessia--;
		}		
		if(Main.fila_Ponte.isEmpty() == false){
			Main.fila_Ponte.removeFirst();
			Main.up_B();
		}
		Main.flagPonte = 0;
	}
	
	public void run() {
		if(Main.fila_Ponte.isEmpty() == true) {			
			Main.down_Mutex();
			if(Main.flagPonte == 0) {				
				Main.flagPonte = -1;				
				this.codigoRegiaoCritica();
			}
			Main.up_Mutex();			
		}
		else {
			Main.down_B();
			System.out.printf("Carro B id : %d solto\n",this.idCarro);
			this.codigoRegiaoCritica();
			

		}				
	}	
}


























