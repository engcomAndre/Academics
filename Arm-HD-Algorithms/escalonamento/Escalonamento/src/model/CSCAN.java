package model;

import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;


import model.Estatistics;
import view.Configure;

public class CSCAN {
	//data SCAN algorithm
	private LinkedList<Integer > Process;
	private LinkedList<Integer>callResquisitionsOrder ;		
	private LinkedList<Integer>distances ;
	private int finalDisc;
	public double scheduler;

	public CSCAN(Configure configure,LinkedList<Integer>ProcessIn){
		this.callResquisitionsOrder = new LinkedList<>();
		this.distances = new LinkedList<>();	
		this.Process = ProcessIn;
		this.finalDisc = configure.getQntdCiliders();
		
		this.schedulerCSCAN(configure.getDiscArmInitialCilinder(), Process);
	}

	public LinkedList<Integer> getCallRequisitionOrder(){		
		return callResquisitionsOrder;
	}

	public LinkedList<Integer> getDistances(){
		return distances;
	}

	private void schedulerCSCAN(int atualPosition,LinkedList<Integer>Process) {
		Process.sort(null);
		if(atualPosition <= Process.getFirst()) {//caso a posição esteja no antes da primeira posicao
			Process.addFirst(0);
			while(!Process.isEmpty()) {	
				callResquisitionsOrder.addLast(atualPosition);			
				distances.addLast(Math.abs(atualPosition - Process.getFirst()));			
				atualPosition = Process.removeFirst();			
			}
			return;
			
		}
		if(atualPosition >= Process.getLast()) {//caso a posicao atual seja maior que a ultima requisicao
			Collections.sort(Process, new Comparator<Object>() {
				public int compare(Object num1, Object num2) {                
					return (Integer)num1 >= (Integer)num2?-1:1;
				}
			});	
			while(!Process.isEmpty()) {		
				callResquisitionsOrder.addLast(atualPosition);			
				distances.addLast(Math.abs(atualPosition - Process.getFirst()));			
				atualPosition = Process.removeFirst();			
			}
			return;			
		}		
		
		
		
		//fatiamento das listas
		int i = 0;
		LinkedList<Integer> minList = new LinkedList<>();///lista menor que piv
		LinkedList<Integer>maxList  = new LinkedList<>();//lista menor que piv

		while(atualPosition >= Process.get(i)) {
			minList.addLast(Process.get(i));
			i++;
		}
		i = Process.size();
		while(atualPosition < Process.get(--i) ) {
			maxList.addLast(Process.get(i));
		}		
	
				

		LinkedList<Integer> list = null;

		int maior = maxList.getFirst() - atualPosition;
		int menor = atualPosition - minList.getLast();

		if(menor >= maior) {//subindo
			maxList.addAll(minList);
			list = maxList;					
			maxList.addAll(minList);
			System.out.println("subindo");
			System.out.println(maxList);
			scheduler = (finalDisc - atualPosition)+finalDisc+list.getLast();

		}
		else {//descendo
			Collections.sort(minList, new Comparator<Object>() {
				public int compare(Object num1, Object num2) {                
					return (Integer)num1 >= (Integer)num2?-1:1;
				}
			});

			Collections.sort(maxList, new Comparator<Object>() {
				public int compare(Object num1, Object num2) {                
					return (Integer)num1 >= (Integer)num2?-1:1;
				}
			});
			minList.addAll(maxList);				
			list = minList;
			scheduler = atualPosition + finalDisc+(finalDisc - list.getLast());
		}
		while(!list.isEmpty()) {		
			callResquisitionsOrder.addLast(atualPosition);			
			distances.addLast(Math.abs(atualPosition - list.getFirst()));			
			atualPosition = list.removeFirst();			
		}
		
	}

	@Override
	public String toString() {
		
		Configure.results.addLast(""+String.format("%.0f", this.scheduler));
		Configure.results.addLast(""+String.format("%.2f", this.scheduler/distances.size()));
		Configure.results.addLast(String.format("%.2f", this.scheduler/distances.size()*Configure.seekTime));
		Configure.results.addLast(String.format("%.0f", (Estatistics.variance(Estatistics.mediaSchedulers(distances), distances))));
		Configure.results.addLast(String.format("%.2f", (Estatistics.standardDeviation(distances))));
		
		String result = "Estatisticas para o Algoritmo de CSCAN"
				+ "\r\n"+"Distancia Total = "+String.format("%.0f", this.scheduler)	
				+ "\r\n"+"Distancia Media = "+String.format("%.2f", this.scheduler/distances.size())
				+ "\r\n"+"Tempo Medio     = "+String.format("%.2f", this.scheduler/distances.size()*Configure.seekTime)
				+ "\r\n"+"Variancia       = "+String.format("%.0f", (Estatistics.variance(Estatistics.mediaSchedulers(distances), distances)))
				+ "\r\n"+"Desvio Padrão   = "+String.format("%.2f", (Estatistics.standardDeviation(distances)))
				+ "\r\n"+"Requisições       \n"+callResquisitionsOrder.toString()
				;
		String call = "";
		for(int i = 0;i<callResquisitionsOrder.size();i++) {
			call += callResquisitionsOrder.get(i)+"-";			
		}	
		DataOUT.writeFileOut(call, "Ordem de Chamadas algoritmo CSCAN");
		return result; 
	}

}


