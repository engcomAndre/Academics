package classes;

import java.util.Random;

public class CarroA extends Thread{
	Random randint = new Random();
	public int idCarro;	
	public int tempoTravessia;	//tempo de travessia na ponte;
	public int tempoEspera;		//tempo de espera na ponte deve tentar atravessar caso 0;
	public int  sentido;
	
	public CarroA(int sentido) {
		super();
		this.idCarro = Main.contCarros++;	
		if(randint.nextInt(5) % 2 == 0){
			this.tempoTravessia = 10;
		}
		else{
			this.tempoTravessia = randint.nextInt(5);
		}
		this.tempoTravessia = randint.nextInt(5);
		this.tempoEspera = randint.nextInt(9);
		this.sentido = sentido;		
	}
	
	static CarroA getInstance(){
		return new CarroA(1);
	}
	
	public void codigoRegiaoCritica() {
		System.out.printf("CarroA id : %d diz Cruzando Ponte\n",this.idCarro);
		Main.fila_Ponte.addLast(Main.fila_A.removeFirst());		
		this.decrementarTravessia();
		Main.fila_Ponte.removeFirst();	
	}

/*Essas Funções Sicronizam as threads com o tempo do sistema*/	
//	public void decrementarTravessia(){
//		int segDecorrido = 0;
//		while(segDecorrido <= this.tempoTravessia){
//			long tempoFinal = System.currentTimeMillis() + Main.constTempo;
//			while(System.currentTimeMillis() <= tempoFinal);
//			System.out.printf("CarroA id : %d diz TRAVESSIA Segundos: %d -> %d \n",this.idCarro,segDecorrido,this.tempoTravessia);
//			segDecorrido++;
//		}	
//	}//	
//	public void decrementarTempoEspera(){		
//		int segDecorrido = 0;
//		while(segDecorrido <= this.tempoEspera){
//			long tempoFinal = System.currentTimeMillis() + Main.constTempo;
//			while(System.currentTimeMillis() <= tempoFinal);
//			System.out.printf("CarroA id : %d diz ESPERA Segundos: %d -> %d\n",this.idCarro,segDecorrido,this.tempoEspera);
//			segDecorrido++;
//		}		
//	}
	public void decrementarTempoEspera(){		
		while(this.tempoEspera > 0){
			int cont = 0;
			while(cont < Math.pow(4, 15)){
				cont++;
			}
			this.tempoEspera--;
			System.out.printf("CarroA id : %d diz ESPERA : %d\n",this.idCarro,this.tempoEspera);
		}
	}
	
	public void decrementarTravessia(){		
		while(this.tempoTravessia> 0){
			int cont = 0;
			while(cont < Math.pow(4, 15)){
				cont++;
			}	
			this.tempoTravessia--;
			System.out.printf("CarroA id : %d diz CRUZANDO PONTE : %d\n",this.idCarro,this.tempoTravessia);
		}
	}
	
	
	public void destroy(){
		return;
	}
	
	public void run() {
		System.out.printf("CarroA id : %d diz INSTANCIADO\n",this.idCarro);
		this.decrementarTempoEspera();//Aguardando para entrar na ponte
		Main.fila_A.addLast(this);

		if(Main.fila_Ponte.isEmpty() == true){
			System.out.printf("CarroA id : %d diz DORMINDO MUTEX\n",this.idCarro);
			Main.down_Mutex();
			if(Main.direcaoPonte == 0){
				System.out.printf("CarroA id : %d diz DOWN_MUTEX\n",this.idCarro);
				Main.direcaoPonte = 1;	//Ponte Sentido Leste -> Oeste
				System.out.printf("CarroA id : %d diz DIRECAO PONTE: %s\n",this.idCarro,Main.direcaoPonte == 1?"LESTE -> OESTE":"OESTE -> LESTE");
			}		
			Main.up_Mutex();
			System.out.printf("CarroA id : %d diz SAINDO MUTEX\n",this.idCarro);

		}
		//Ponte com Carros
		//continua execução	
		//OBS:Tratamento caso a caso

		if(Main.direcaoPonte == -1 || (Main.prioridadePonte == -1 && Main.fila_B.isEmpty() == false)) {//Carro no sentido oposto 
			System.out.printf("CarroA id : %d diz CARRO NO SENTIDO OPOSTO\n",this.idCarro);
			Main.down_A();							
		}
//		if(Main.fila_B.isEmpty() == false && Main.prioridadePonte == -1 ){//Prioridade dos Carros no sentid oposto
//			System.out.printf("CarroA id : %d diz PRIORIDADE DO SENTIDO OPOSTO %d\n",this.idCarro,Main.Ponte.availablePermits());
//			Main.direcaoPonte = -1;		
//			Main.down_A();			
//		}

		System.out.printf("CarroA id : %d diz PERMISSÕES : %d\n",this.idCarro,Main.Ponte.availablePermits());

		if(Main.Ponte.availablePermits() == 0){
			System.out.printf("CarroA id : %d diz PONTE LOTADA:\n",this.idCarro);
			
		}
		Main.down_Ponte();
		Main.up_A();
		Main.up_A();
		
		this.codigoRegiaoCritica();
		Main.up_Ponte();
		Main.down_A();
		Main.down_A();
		if(Main.fila_Ponte.isEmpty() == true) {
			Main.direcaoPonte = 0;
			Main.up_B();
		}
		System.out.printf("CarroA id : %d diz FIM\n",this.idCarro);
		this.destroy();
	}


}
















		