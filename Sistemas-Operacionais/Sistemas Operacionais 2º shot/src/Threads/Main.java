package Threads;

import java.util.LinkedList;
import java.util.Random;
import java.util.concurrent.Semaphore;

public class Main {	
	//globais acesso de qualquer lugar
	public static int permissoes = 1;
	public static int quantCarros = 10;
	public static Random randint =  new Random();
	public static Semaphore semaforo_A =  new Semaphore(0,true);
	public static Semaphore semaforo_B =  new Semaphore(0,true);
	public static Semaphore mutex =  new Semaphore(permissoes,true);
	public static Semaphore Ponte =  new Semaphore(3);
	public static LinkedList<Object> fila_Ponte =  new LinkedList<Object>();
	public static LinkedList<Object> fila_A =  new LinkedList<Object>();
	public static LinkedList<Object> fila_B =  new LinkedList<Object>();
	public static int flagPonte = 0;
	public static int idcarros = 0;
	public static int lotPonte = 0;

	
	public static void main(String[] args) {
		for (int i = 0; i < quantCarros; i++) {
			fila_A.addLast(new CarroA(1));			
			fila_B.addLast(new CarroB(-1));
		}
		for (int i = 0; i < quantCarros-1; i++) {
			((Thread) fila_B.get(i)).start();
			((Thread) fila_A.get(i)).start();			
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
	public static void up_A( ) {		
			semaforo_A.release();
		
	}
	public static void up_B( ) {
		semaforo_B.release();		
	}
	public static void up_Mutex() {
		mutex.release();
	}
	public static void up_Ponte() {
		Ponte.release();
	}

}


