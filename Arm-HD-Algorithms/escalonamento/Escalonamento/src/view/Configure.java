package view;

import java.util.LinkedList;

import model.DataIN;

public class Configure {
	public static LinkedList<String>results = new LinkedList<>();
	private  int qntdCilinder;
	private  int discArmInitialCilinder ;
	public static double seekTime;
	public static String nameFile;
	private LinkedList <Integer> Process;	
	
	public Configure(int qntdCilinder,int initialArmPosition,double seekTime,LinkedList<Integer>Process) {
		this.qntdCilinder = qntdCilinder;
		this.discArmInitialCilinder  = initialArmPosition;
		if(this.discArmInitialCilinder > this.qntdCilinder) {
            System.out.println("ERROR - Posição Inicial maior que a quantidade cilindros");
            return;
		}		
		Configure.seekTime = seekTime;
		this.Process = Process;
		
	}
	
	//gets	
	public int getQntdCiliders() {
		return this.qntdCilinder;
	}
	
	public double getSeekTime() {
		return seekTime;
	}
	
	public int getDiscArmInitialCilinder() {
		return this.discArmInitialCilinder ;
	}
	
	public LinkedList<Integer> getProcess() {
		return this.Process;
	}

	@Override
	public String toString() {
		return "Configure"
			+ "\n   Quantidade de Cilindos = " + this.qntdCilinder
			+ "\n   Posição Inicial Braço  = " + this.discArmInitialCilinder
			+ "\n   Tempo de Seek	  = " + Configure.seekTime 
			+ "\n   Vetor de Processos 	  = " + DataIN.getProcessArray() ;
	}	
}
