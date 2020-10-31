package ponte.carro;

import java.util.Random;

import ponte.controle.Ponte;

public class CarroLeste extends Thread{
	
	private int idCarro;
	private long tempoPermanencia;
	private long tempoTravessia;
	
	public CarroLeste(int id, long tempoPermanencia, long tempoTravessia) {
		this.idCarro = id;
		this.tempoPermanencia = tempoPermanencia;
		this.tempoTravessia = tempoTravessia;
	}
	
	public void aguardarTentativa(){
		int segDecorrido = 0;
		while(segDecorrido <= this.tempoPermanencia){
			long tempoFinal = System.currentTimeMillis() + this.getTempoPermanencia()*500;
			while(System.currentTimeMillis() <= tempoFinal);
			System.out.printf("Carro LESTE id: %d - TENTATIVA em %d de %d segundos\n",this.idCarro,segDecorrido,this.tempoPermanencia);
			segDecorrido++;
			
		}
					
	}
	
	public void atravessandoPonte(){
		int segDecorrido = 0;
		while(segDecorrido <= this.tempoTravessia){
			long tempoFinal = System.currentTimeMillis() + this.getTempoTravessia()* 500;
			while(System.currentTimeMillis() <= tempoFinal);
			System.out.printf("Carro LESTE id: %d - ATRAVESSANDO em %d de %d segundos\n",this.idCarro,segDecorrido,this.tempoTravessia);
			segDecorrido++;

		}					
	}
	
	
	public void aguardarVolta(){
		int tempoRetorno = new Random().nextInt(30);
		int segDecorrido = 0;
		while(segDecorrido <= tempoRetorno){
			long tempoFinal = System.currentTimeMillis() + tempoRetorno* 500;
			while(System.currentTimeMillis() <= tempoFinal);
			System.out.printf("Carro LESTE id: %d - VOLTANDO em %d de %d segundos\n",this.idCarro,segDecorrido,tempoRetorno);
			segDecorrido++;

		}					
	}
	
	public void destroy(){
		return;
	}
	
	
	
	
	
	@Override
	public void run() {
		System.out.printf("Carro LESTE id: %d - INICIANDO\n",this.idCarro);
		
		System.out.printf("Carro LESTE id: %d - AGUARDANDO TENTATIVA em %ds\n",this.idCarro,this.tempoPermanencia);
		
//		if(Ponte.prioridadeDefinida == Sentido.OESTE){
//			if(Ponte.filaCarrosOeste.isEmpty() == false){
//				Ponte.upOeste();
//				Ponte.downLeste();				
//			}
//		}
		
		this.aguardarTentativa();
		System.out.printf("Carro LESTE id: %d - FIM TEMPO DE AGUARDO TENTANDO ATRAVESSAR PONTE\n",this.idCarro);

		Ponte.downMutex();
		Ponte.filaCarrosLeste.addLast(this);
		Ponte.upMutex();
		
		if(Ponte.filaPonte.isEmpty() == true){
			System.out.printf("Carro LESTE id: %d - DOWN MUTEX - %s\n",this.idCarro,Ponte.Mutex.availablePermits()==0?"PASSOU":"DORMINDO");
			Ponte.downMutex();
			if(Ponte.sentidoAtual == Sentido.NENHUM){
				Ponte.sentidoAtual = Sentido.LESTE;			
				System.out.printf("Carro LESTE id: %d - DIRE��O PONTE : %s\n",this.idCarro,"LESTE");
			}
			Ponte.upMutex();			

			System.out.printf("Carro LESTE id: %d ACORDANDO DO MUTEX \n",this.idCarro);
		}
		////
		if(Ponte.sentidoAtual == Sentido.OESTE){
			
			System.out.printf("Carro LESTE id: %d CARRO NO SENTIDO OPOSTO - DORMINDO\n",this.idCarro);
			Ponte.downLeste();
			System.out.printf("Carro LESTE id: %d FIM CARRO NO SENTIDO OPOSTO - ACORDADO\n",this.idCarro);
		}
		/////
		if(Ponte.prioridadeDefinida == Sentido.OESTE && Ponte.filaCarrosOeste.isEmpty() == false){
			//Ponte.upOeste();
			System.out.printf("Carro LESTE id: %d PRIORIDADE DE CARRO MAIOR - DORMINDO\n",this.idCarro);
			Ponte.sentidoAtual = Sentido.LESTE;
			System.out.printf("Carro LESTE id: %d PRIORIDADE DE CARRO MAIOR - DORMINDO\n",this.idCarro);

			Ponte.downLeste();		
		}
		/////
		System.out.printf("Carro LESTE id: %d - PONTE - %s\n",this.idCarro,Ponte.ponte.availablePermits()==0?"LOTADA - DORMINDO":"ATRAVESSANDO");
		Ponte.downPonte();
		Ponte.upLeste();
		
		
//		Ponte.translates.get(this.idCarro).play();
		
		
		this.atravessandoPonte();
		Ponte.upPonte();
		System.out.printf("Carro LESTE id: %d FIM TRAVESSIA\n",this.idCarro);
		
		/////
		if(Ponte.filaPonte.isEmpty() == true ){
			System.out.printf("Carro LESTE id: %d - PONTE VAZIA\n",this.idCarro);
			Ponte.sentidoAtual = Sentido.NENHUM;
			Ponte.upLeste();
			Ponte.upOeste();
		}
		/////		
		System.out.printf("Carro LESTE id: %d - PONTE - %s\n",this.idCarro,"AGUARDANDO VOLTA");
		this.aguardarVolta();
		
		Ponte.downMutex();
		new CarroOeste(this.idCarro, this.tempoPermanencia,this.tempoTravessia).start();	
		Ponte.upMutex();
		System.out.printf("Carro LESTE id: %d - SENTIDO DESTE CARRO AGORA � OESTE\n",this.idCarro);
		this.destroy();	
		
	}
		
//		Ponte.downMutexOeste();
//		Ponte.indoOeste++;
//		
//		if (Ponte.indoOeste == 1)
//			Ponte.downPonte();
//		Ponte.upMutexOeste();
//		
//		// Tempo perman�ncia
//		
//		
//		
//		// Pega o respectivo objeto TranslateTransition e inicializa a anima��o
//		Ponte.translates.get(Ponte.idCarro).play();
//		
//		Ponte.downMutexOeste();
//		Ponte.indoOeste--;
//		
//		System.out.println("Carro Leste " + this.getIdCarro() + " est� atravessando a ponte por " + this.getTempoTravessia() + "s");
//		
//		// Tempo travessia
//		long tempoAtravessando = System.currentTimeMillis() + this.getTempoTravessia()*1000;
//		while(System.currentTimeMillis() <= tempoAtravessando);
//		
//		System.out.println("Carro Leste " + this.getIdCarro() + " atravessou a ponte");
//		
//		if (Ponte.indoOeste == 0)
//			Ponte.upPonte();
//		Ponte.upMutexOeste();
		
	
	
	public int getIdCarro() {
		return this.idCarro;
	}

	public long getTempoPermanencia() {
		return tempoPermanencia;
	}

	public long getTempoTravessia() {
		return tempoTravessia;
	}

}
