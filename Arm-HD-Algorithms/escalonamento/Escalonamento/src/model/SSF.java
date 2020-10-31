package model;

import java.util.LinkedList;

import view.Configure;

public class SSF {
	//data SSF algorithm
	private LinkedList<Integer>callResquisitionsOrder ;		
	private LinkedList<Integer>distances ;

	public SSF(int initialPosition,LinkedList<Integer>Process){
		this.callResquisitionsOrder = new LinkedList<>();
		this.distances = new LinkedList<>();
		this.schedulerSSF(initialPosition, Process);
	}

	public LinkedList<Integer> getCallRequisitionOrder(){		
		return callResquisitionsOrder;
	}

	public LinkedList<Integer> getDistances(){
		return distances;
	}

	private void schedulerSSF(int atualPosition,LinkedList<Integer>Process) {
		int distance,prox = 0;
		while(!Process.isEmpty()){			
			callResquisitionsOrder.addLast(atualPosition);		

			distance = Math.abs(atualPosition - Process.get(0));
			prox = Process.get(0);
			for(int i = 1;i < Process.size();i++) {//escolhendo menos distancia					
				if(distance>= Math.abs(atualPosition - Process.get(i))) {
					distance = Math.abs(atualPosition - Process.get(i));
					prox = Process.get(i);
				}
			}
			distances.addLast(distance);
			atualPosition = Process.remove(Process.indexOf(prox));
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
		
		String result = "Estatisticas para o Algoritmo de SSF"
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
		DataOUT.writeFileOut(call, "Ordem de Chamadas algoritmo SSF");
		return result; 
	}

}			


