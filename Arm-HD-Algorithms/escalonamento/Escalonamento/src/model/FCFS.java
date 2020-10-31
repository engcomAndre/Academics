package model;

import java.util.LinkedList;

import view.Configure;


public class FCFS {		
	//data FCFS algorithm
	private LinkedList<Integer>callResquisitionsOrder ;		
	private LinkedList<Integer>distances ;

	public FCFS(int initialPosition,LinkedList<Integer>Process){
		this.callResquisitionsOrder = new LinkedList<>();
		this.distances = new LinkedList<>();
		this.schedulerFCFS(initialPosition, Process);
	}
	
	public LinkedList<Integer> getCallRequisitionOrder(){		
		return callResquisitionsOrder;
	}

	public LinkedList<Integer> getDistances(){
		return distances;
	}

	private void schedulerFCFS(int atualPosition,LinkedList<Integer>Process) {	
		int prox;
		while(!Process.isEmpty()){		
			prox = Process.removeFirst();					
			distances.addLast(Math.abs(atualPosition - prox));
			callResquisitionsOrder.addLast(prox);
			atualPosition = prox;			
		}
	}	


	public void printData() {		
		System.out.println("Processos Chamados    = "+this.callResquisitionsOrder);
		System.out.println("Distancias            = "+this.distances);

	}

	@Override
	public String toString() {
		Configure.results.addLast(""+(int)Estatistics.schedulers(distances));
		Configure.results.addLast(""+String.format("%.2f", Estatistics.mediaSchedulers(distances)));
		Configure.results.addLast(String.format("%.2f", Estatistics.mediaSchedulers(distances)*Configure.seekTime));
		Configure.results.addLast(String.format("%.0f", (Estatistics.variance(Estatistics.mediaSchedulers(distances), distances))));
		Configure.results.addLast(String.format("%.2f", (Estatistics.standardDeviation(distances))));
	
		String result = "Estatisticas para o Algoritmo de FCFS"
				+ "\r\n"+"Distancia Total = "+(int)Estatistics.schedulers(distances)
				+ "\r\n"+"Distancia Media = "+String.format("%.2f", Estatistics.mediaSchedulers(distances))
				+ "\r\n"+"Tempo Medio     = "+String.format("%.2f", Estatistics.mediaSchedulers(distances)*Configure.seekTime)
				+ "\r\n"+"Variancia       = "+String.format("%.0f", (Estatistics.variance(Estatistics.mediaSchedulers(distances), distances)))
				+ "\r\n"+"Desvio Padrão   = "+String.format("%.2f", (Estatistics.standardDeviation(distances)))
		 		+ "\r\n"+"Requisições       \n"+callResquisitionsOrder.toString()
				;
		String call = "";
		for(int i = 0;i<callResquisitionsOrder.size();i++) {
			call += callResquisitionsOrder.get(i)+"-";			
		}				
		DataOUT.writeFileOut(call, "Ordem de Chamadas algoritmo FCFS");
		return result; 
	}
	
}			

