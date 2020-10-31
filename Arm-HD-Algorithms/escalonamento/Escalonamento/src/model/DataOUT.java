package model;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.LinkedList;

public class DataOUT {
	
	public static void publicResult(LinkedList<Integer>Results) {
		writeFileOut(initFileOut(Results),"tstest");		
	}
	
	public static String initFileOut(LinkedList<Integer>Results) {
		String res = "";
		for (int i = 0; i < Results.size(); i++) {
			res += Results.get(i).toString();
		}
		return res;
	}
	public static void writeFileOut(String data,String name) {
		
		if(!name.contains(".txt")) {
			name+=".txt";
		}		
		String nameFile = "..//Escalonamento//src//result//"+name;		
		File file = new File(nameFile);
		try {
			file.createNewFile();
			FileWriter fw = new FileWriter(file);				
			fw.write(data);			
			fw.close();				

		} catch (IOException e) {
			e.printStackTrace();
		}			
	}


}
