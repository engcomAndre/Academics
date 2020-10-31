package treads;

import java.util.Random;

public class CarroA extends Thread{
	Random randint = new Random();
	public int idCarro;	
	public int tempoTravessia;	//tempo de travessia na ponte;
	public int tempoEspera;		//tempo de espera na ponte deve tentar atravessar caso 0;
	public int  sentido;
	
	public CarroA(int sentido) {
		super();
		this.idCarro = Main.idcarros++;				
		this.tempoTravessia = randint.nextInt(9);
		this.tempoEspera = randint.nextInt(9);
		this.sentido = sentido;		
	}
	public void codigoRegiaoCritica() {
		System.out.printf("Ponte : %s\n",Main.fila_Ponte.size());		
		Main.fila_Ponte.addLast(Main.fila_A.removeFirst());		
		System.out.printf("Carro A %d add na ponte\n",this.idCarro);
		int num = 4;
		if(Main.fila_A.size() < num){
			while(num > 0){
				Main.up_A();
				num--;
			}
		}
		while(this.tempoTravessia > -1 ) {
			
			System.out.printf ("Carro A : %d Posicao : %d\n",this.idCarro,this.tempoTravessia);
			tempoTravessia--;			
		}
		if(Main.fila_Ponte.isEmpty() == false){
			Main.fila_Ponte.removeFirst();
			Main.up_A();
		}		
		
		Main.flagPonte = 0;
		
	}	
	public void run() {
		if(Main.fila_Ponte.isEmpty() == true) {//Ponte Vazia			
			Main.down_Mutex();			//Inicio Região Critica 1
			if(Main.flagPonte == 0) {//Primeiro Carro a entrar
				Main.flagPonte = 1;				
				this.codigoRegiaoCritica();				
			}//FIm Região Critica 1
			Main.up_Mutex();			
		}
		else {
			Main.down_A();			
			System.out.printf("Carro A id : %d solto\n",this.idCarro);
			this.codigoRegiaoCritica();

		}			
	}
}
















		