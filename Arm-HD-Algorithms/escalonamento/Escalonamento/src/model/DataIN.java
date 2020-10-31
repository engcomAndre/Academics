package model;
import view.SelectionFileVIEW;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.LinkedList;

public class DataIN {
	private static String line = "";
	private static String number = "";
	private static String cat = "";
	private static String numbers = "0123456789";
	private static LinkedList<Integer>Process = new LinkedList<Integer>();
	private String nameFile;

	private static String getLine(FileReader file){
		String temp = null; 
		BufferedReader readFile = new BufferedReader(file);
		try {
			temp = readFile.readLine();
		} catch (IOException e) {
			e.printStackTrace();
			System.out.println("No Memory");
		}	
		
		return temp;
	}

	public static LinkedList<Integer> getProcessArray(){
		line = DataIN.getLine(SelectionFileVIEW.learquivo());
		for(int i = 0;i < line.length();i++) {
			cat = ""+line.charAt(i);
			if(numbers.contains(cat)) {
				number = number.concat(cat);				
			}			
			else {
				Process.add(Integer.parseInt(number));
				number = "";										
			}
		}	
		
		return Process;
	}		
}

