package ponte.carro;

import java.util.Random;

import ponte.controle.Ponte;

public class CarroOeste extends Thread{
	
	private int idCarro;
	private long tempoPermanencia;
	private long tempoTravessia;
	
	public CarroOeste(int id, long tempoPermanencia, long tempoTravessia) {
		this.idCarro = id;
		this.tempoPermanencia = tempoPermanencia;
		this.tempoTravessia = tempoTravessia;
	}
	
	public void aguardarTentativa(){
		int segDecorrido = 0;
		while(segDecorrido <= this.tempoPermanencia){
			long tempoFinal = System.currentTimeMillis() + this.getTempoPermanencia()*1000;
			while(System.currentTimeMillis() <= tempoFinal);
			System.out.printf("Carro OESTE id: %d - TENTATIVA em %d de %d segundos\n",this.idCarro,segDecorrido,this.tempoPermanencia);
			segDecorrido++;
			
		}
					
	}
	
	public void atravessandoPonte(){
		int segDecorrido = 0;
		while(segDecorrido <= this.tempoTravessia){
			long tempoFinal = System.currentTimeMillis() + this.getTempoTravessia()+ 1000;
			while(System.currentTimeMillis() <= tempoFinal);
			System.out.printf("Carro OESTE id: %d - ATRAVESSANDO em %d de %d segundos\n",this.idCarro,segDecorrido,this.tempoTravessia);
			segDecorrido++;

		}					
	}
	
	
	public void aguardarVolta(){
		int tempoRetorno = new Random().nextInt(30);
		int segDecorrido = 0;
		while(segDecorrido <= tempoRetorno){
			long tempoFinal = System.currentTimeMillis() + tempoRetorno+ 1000;
			while(System.currentTimeMillis() <= tempoFinal);
			System.out.printf("Carro OESTE id: %d - VOLTANDO em %d de %d segundos\n",this.idCarro,segDecorrido,tempoRetorno);
			segDecorrido++;

		}					
	}
	public void destroy(){
		return;
	}
	
	@Override
	public void run() {
		System.out.printf("Carro LESTE id: %d - INICIANDO\n",this.idCarro);


		System.out.printf("Carro OESTE id: %d - AGUARDANDO TENTATIVA em  %ds\n",this.idCarro,this.tempoPermanencia);
		if(Ponte.prioridadeDefinida == Sentido.LESTE){
			if(Ponte.filaCarrosLeste.isEmpty() == false){
				Ponte.upLeste();
				Ponte.downOeste();				
			}
		}
		this.aguardarTentativa();
		System.out.printf("Carro OESTE id: %d - FIM TEMPO DE AGUARDO TENTANDO ATRAVESSAR PONTE\n",this.idCarro);

		
		Ponte.downMutex();
		Ponte.filaCarrosOeste.addLast(this);
		Ponte.upMutex();
		
		if(Ponte.filaPonte.isEmpty() == true){
			System.out.printf("Carro OESTE id: %d - DOWN MUTEX - %s\n",this.idCarro,Ponte.Mutex.availablePermits()==0?"PASSOU":"DORMINDO");
			Ponte.downMutex();
			if(Ponte.sentidoAtual == Sentido.NENHUM){
				Ponte.sentidoAtual = Sentido.OESTE;			
				System.out.printf("Carro OESTE id: %d - DIREÇÃO PONTE : %s\n",this.idCarro,"OESTE");
			}
			Ponte.upMutex();			

			System.out.printf("Carro OESTE id: %d ACORDANDO DO MUTEX \n",this.idCarro);
		}
		/////
		if(Ponte.sentidoAtual == Sentido.LESTE){			
			System.out.printf("Carro OESTE id: %d CARRO NO SENTIDO OPOSTO - DORMINDO\n",this.idCarro);
			Ponte.downOeste();
			System.out.printf("Carro OESTE id: %d FIM CARRO NO SENTIDO OPOSTO - ACORDADO\n",this.idCarro);
		}
		/////
		System.out.printf("Carro OESTE id: %d - PONTE - %s\n",this.idCarro,Ponte.ponte.availablePermits()==0?"LOTADA - DORMINDO":"ATRAVESSANDO");
		Ponte.downPonte();
		Ponte.upOeste();
		Ponte.translates.get(this.idCarro).play();
		

		this.atravessandoPonte();		
		Ponte.upPonte();
		System.out.printf("Carro OESTE id: %d FIM TRAVESSIA\n",this.idCarro);
		/////
		if(Ponte.filaPonte.isEmpty() == true ){
			System.out.printf("Carro OESTE id: %d - PONTE VAZIA\n",this.idCarro);
			Ponte.sentidoAtual = Sentido.NENHUM;
			Ponte.upLeste();
			Ponte.upOeste();
		}
		/////	
		System.out.printf("Carro OESTE id: %d - PONTE - %s\n",this.idCarro,"AGUARDANDO VOLTA");
		this.aguardarVolta();
		new CarroLeste(this.idCarro, this.tempoPermanencia,this.tempoTravessia).start();	
		System.out.printf("Carro OESTE id: %d - SENTIDO DESTE CARRO AGORA É LESTE\n",this.idCarro);
		this.destroy();		
		
//		Ponte.downMutexLeste();
//		Ponte.indoLeste++;
//		
//		if (Ponte.indoLeste == 1)
//			Ponte.downPonte();
//		Ponte.upMutexLeste();
//		
//		// Tempo permanência
//		long tempoEsperando = System.currentTimeMillis() + this.getTempoPermanencia()*1000;
//		while(System.currentTimeMillis() <= tempoEsperando);
//		
//		// Pega o respectivo objeto TranslateTransition e inicializa a animação
//		Ponte.translates.get(Ponte.idCarro).play();
//		
//		Ponte.downMutexLeste();
//		Ponte.indoLeste--;
//
//		System.out.println("Carro Oeste " + this.getIdCarro() + " está atravessando a ponte por " + this.getTempoTravessia() + "s");
//		
//		// Tempo travessia
//		long tempoAtravessando = System.currentTimeMillis() + this.getTempoTravessia()*1000;
//		while(System.currentTimeMillis() <= tempoAtravessando);
//		
//		System.out.println("Carro Oeste " + this.getIdCarro() + " atravessou a ponte");
//		
//		if (Ponte.indoLeste == 0)
//			Ponte.upPonte();
//		Ponte.upMutexLeste();
//		
	}
	
	public int getIdCarro() {
		return idCarro;
	}

	public long getTempoPermanencia() {
		return tempoPermanencia;
	}

	public long getTempoTravessia() {
		return tempoTravessia;
	}
	
}
