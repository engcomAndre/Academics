package view;

import java.io.FileReader;
import java.io.IOException;

import javax.swing.JFileChooser;

public class SelectionFileVIEW {
	private static FileReader file;


	public static FileReader learquivo() {
		JFileChooser chooser = new JFileChooser();
		chooser.setMultiSelectionEnabled(false);
		chooser.showOpenDialog(null);
		chooser.getSelectedFiles();	
		Configure.nameFile = ""+chooser.getSelectedFile();
		System.out.println("Nome do arquivo :" + chooser.getSelectedFile());
		try {
			file = new FileReader(chooser.getSelectedFile());
//			file = new FileReader("..//Escalonamento//src//result//fileIn.txt");		

		} catch (IOException e) {
			e.printStackTrace();
			System.out.println("Arquivo Inválido ou não existente");
		}
		return file;
	}
}
	
	
