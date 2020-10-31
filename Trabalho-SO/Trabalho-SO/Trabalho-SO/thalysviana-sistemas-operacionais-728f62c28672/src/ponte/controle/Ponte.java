package ponte.controle;


import java.util.HashMap;
import java.util.LinkedList;
import java.util.Random;
import java.util.concurrent.Semaphore;

import javafx.animation.TranslateTransition;
import javafx.scene.image.ImageView;
import ponte.carro.CarroLeste;
import ponte.carro.CarroOeste;
import ponte.carro.Sentido;

public class Ponte {
	
	public static Sentido prioridadeDefinida = Sentido.NENHUM;
	public static Sentido sentidoAtual = Sentido.NENHUM; 
	public static int idCarro = 0;
	public static int indoLeste = 0;
	public static int indoOeste = 0;
	public static boolean ehPrimeiraExecucao = true;
	public static Semaphore ponte = new Semaphore(3, true);
	public static Semaphore Mutex= new Semaphore(1, true);

	public static Semaphore mutexOeste = new Semaphore(0, true);
	public static Semaphore mutexLeste = new Semaphore(0, true);
	public static HashMap<Integer, TranslateTransition> translates = new HashMap<>(); 
	public static HashMap<Integer, ImageView> carrosView = new HashMap<>();
	public static LinkedList<CarroOeste> filaCarrosOeste = new LinkedList<CarroOeste> ();
	public static LinkedList<CarroLeste> filaCarrosLeste = new LinkedList<CarroLeste> ();
	public static LinkedList<Thread> filaPonte = new LinkedList<Thread> ();
	
	
	public static int zzzCarroLeste = 0;
	public static int zzzCarroOeste= 0;
	public static int zzzMutex = 0;



//
//	public static void main(String[] args) {
//		System.out.println("Sentido: " + Ponte.sentidoAtual);
//		for(int i = 0;i < 2;i++){
//			new CarroLeste(++idCarro, new Random().nextInt(20), new Random().nextInt(20)).start();
//			new CarroOeste(++idCarro, new Random().nextInt(20), new Random().nextInt(20)).start();
//			
//		}
//		
//	}
	
	public static void downPonte() {
		try {
			Ponte.ponte.acquire();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	public static void upPonte() {
		Ponte.ponte.release();
	}
	
	public static void downOeste() {
		try {
			zzzCarroOeste++;
			Ponte.mutexOeste.acquire();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	public static void upOeste() {
		Ponte.mutexOeste.release(zzzCarroOeste);
	}
	
	public static void downLeste() {
		try {
			zzzCarroLeste++;
			Ponte.mutexLeste.acquire();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	public static void upLeste() {
		Ponte.mutexLeste.release(zzzCarroLeste);
	}
	
	public static void downMutex() {
		try {
			zzzMutex++;
			Ponte.Mutex.acquire();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	
	public static void upMutex() {
		Ponte.Mutex.release(zzzMutex);
	}
	
}
