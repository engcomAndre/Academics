package classes;

import java.util.LinkedList;
import java.util.Random;
import java.util.concurrent.Semaphore;

import javafx.application.Application;
import javafx.stage.Stage;

public class Main extends Application{	
	//globais acesso de qualquer lugar
	public static int constTempo = 750;
	public static int quantCarros = 8;
	public static Random randint =  new Random();
	public static Semaphore semaforo_A =  new Semaphore(0);
	public static Semaphore semaforo_B =  new Semaphore(0);
	public static Semaphore mutex =  new Semaphore(1);
	public static Semaphore Ponte =  new Semaphore(3);
	public static LinkedList<Thread> fila_Ponte =  new LinkedList<Thread>();
	public static LinkedList<CarroA> fila_A =  new LinkedList<CarroA>();
	public static LinkedList<CarroB> fila_B =  new LinkedList<CarroB>();
	public static int direcaoPonte = 0;
	public static int prioridadePonte = -1;
	static int contCarros = 0; 	
	
	public static void main(String[] args) {
		for (int i = 0; i <= quantCarros; i++) {
			CarroA.getInstance().start();
			CarroB.getInstance().start();
		}		
	}	
	
	

	public static void down_Ponte() {
		try {
			Ponte.acquire();
		} catch (InterruptedException e) {	
			e.printStackTrace();
		}
	}		
	public static void down_A() {
		try {
			semaforo_A.acquire();
		} catch (InterruptedException e) {	
			e.printStackTrace();
		}
	}	
	public static void down_B() {
		try {
			semaforo_B.acquire();
		} catch (InterruptedException e) {	
			e.printStackTrace();
		}
	}
	public static void down_Mutex() {
		try {
			mutex.acquire();
		} catch (InterruptedException e) {	
			e.printStackTrace();
		}
	}
	public static void up_A() {
		semaforo_A.release();
	}
	public static void up_B() {
		semaforo_B.release();
	}
	public static void up_Mutex() {
		mutex.release();
	}
	public static void up_Ponte() {
		Ponte.release();
	}



	@Override
	public void start(Stage primaryStage) throws Exception {
		// TODO Auto-generated method stub
		
	}

}


