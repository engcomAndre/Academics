package model;


import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;

import model.Estatistics;
import view.Configure;

public class SCAN {
	//data SCAN algorithm
	private LinkedList<Integer>callResquisitionsOrder ;		
	private LinkedList<Integer>distances ;
	public int scheduler;

	public SCAN(Configure configure,LinkedList<Integer>Process){
		this.callResquisitionsOrder = new LinkedList<>();
		this.distances = new LinkedList<>();		
		this.schedulerSCAN(configure.getDiscArmInitialCilinder(), Process);
	}

	public LinkedList<Integer> getCallRequisitionOrder(){		
		return callResquisitionsOrder;
	}

	public LinkedList<Integer> getDistances(){
		return distances;
	}

	private void schedulerSCAN(int atualPosition,LinkedList<Integer>Process) {

		Process.sort(null);		
		System.out.println(Process);

		int i = 0;		
		while(atualPosition >= Process.get(i) && i < Process.size()) {
			i++;
		}

		//fatiando listas
		LinkedList<Integer> minList = new LinkedList<>(Process.subList(0, i));
		Collections.sort(minList, new Comparator<Object>() {
			public int compare(Object num1, Object num2) {                
				return (Integer)num1 >= (Integer)num2?-1:1;
			}
		});
		LinkedList<Integer>maiorList = new LinkedList<>(Process.subList(i, Process.size()));
		LinkedList<Integer> list;
		if((atualPosition - minList.getLast())>(maiorList.getFirst() - atualPosition)) {
			minList.addAll(maiorList);
			list = new LinkedList<>(minList);			
			scheduler = (atualPosition)+list.getLast();

		}
		else {
			maiorList.addAll(minList);
			list = new LinkedList<>(maiorList);
			scheduler = list.getLast() - atualPosition+list.getLast();

		}		

		while(!list.isEmpty()) {		
			callResquisitionsOrder.addLast(atualPosition);			
			distances.addLast(Math.abs(atualPosition - list.getFirst()));			
			atualPosition = list.removeFirst();			
		}	
	}


	public String toString() {
		
		Configure.results.addLast(""+(int)Estatistics.schedulers(distances));
		Configure.results.addLast(""+String.format("%.2f", Estatistics.mediaSchedulers(distances)));
		Configure.results.addLast(String.format("%.2f", Estatistics.mediaSchedulers(distances)*Configure.seekTime));
		Configure.results.addLast(String.format("%.0f", (Estatistics.variance(Estatistics.mediaSchedulers(distances), distances))));
		Configure.results.addLast(String.format("%.2f", (Estatistics.standardDeviation(distances))));
		
		String result = "Estatisticas para o Algoritmo de SCAN"
				+ "\n"+"Distancia Total = "+(int)Estatistics.schedulers(distances)
				+ "\n"+"Distancia Media = "+String.format("%.2f", Estatistics.mediaSchedulers(distances))
				+ "\n"+"Tempo Medio     = "+String.format("%.2f", Estatistics.mediaSchedulers(distances)*Configure.seekTime)
				+ "\n"+"Variancia       = "+String.format("%.0f", (Estatistics.variance((this.scheduler/(double)callResquisitionsOrder.size()), distances)))
				+ "\n"+"Desvio Padrão   = "+String.format("%.2f", (Estatistics.standardDeviation(distances)))
				+ "\n"+"Requisições       \n"+callResquisitionsOrder.toString()
				;
		String call = "";
		for(int i = 0;i<callResquisitionsOrder.size();i++) {
			call += callResquisitionsOrder.get(i)+"-";			
		}	
		DataOUT.writeFileOut(call, "Ordem de Chamadas algoritmo SCAN");

		return result; 
	}

}