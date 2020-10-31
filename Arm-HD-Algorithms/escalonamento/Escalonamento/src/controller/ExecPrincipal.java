 package controller;

import java.util.LinkedList;

import model.CSCAN;
import model.DataOUT;
import model.FCFS;
import model.SCAN;
import model.SSF;
import view.Configure;

public class ExecPrincipal {
	public static void principal(Configure configure) {
		DataOUT.writeFileOut(returnFCFSData(configure),"FCFSdata.txt");
		DataOUT.writeFileOut(returnSSFData(configure),"SSFdata.txt");
		DataOUT.writeFileOut(returnSCANData(configure),"SCANdata.txt");
		DataOUT.writeFileOut(returnCSCANData(configure),"CSCANdata.txt");		
	}
	
	public static String returnCSCANData(Configure configure) {
		LinkedList<Integer> dataProcess= new LinkedList<>(configure.getProcess());
		CSCAN CSCAN= new CSCAN(configure,dataProcess);
		String result = CSCAN.toString();						
		return result;
	}
	
	public static String returnSCANData(Configure configure) {
		LinkedList<Integer> dataProcess = new LinkedList<>(configure.getProcess());

		SCAN SCAN= new SCAN(configure,dataProcess);
		String result = SCAN.toString();						
		return result;
	}
	
	public static String returnSSFData(Configure configure) {
		LinkedList<Integer> dataProcess = new LinkedList<>(configure.getProcess());

		SSF SSF= new SSF(configure.getDiscArmInitialCilinder(),dataProcess);
		String result = SSF.toString();
		return result;
	}	
	
	public static String returnFCFSData(Configure configure) {
		LinkedList<Integer> dataProcess = new LinkedList<>(configure.getProcess());

		FCFS FCFS = new FCFS(configure.getDiscArmInitialCilinder(),dataProcess);
		String result = FCFS.toString();
		return result;
	}	

}
