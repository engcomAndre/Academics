package model;

import java.util.LinkedList;

public class Estatistics {
	private static double sum;
	private static String res;
	
	
	public static String publicEstatistics(double seekTime,LinkedList<Integer> Scheduler) {		
		System.out.printf("%10.5g %10.5g %10.5g %10.5g %10.5g\n\n",
						schedulers(Scheduler),
						mediaSchedulers(Scheduler),
						mediaTimeScheduler(seekTime, Scheduler),
						variance(mediaSchedulers(Scheduler), Scheduler),						
						standardDeviation(Scheduler));
		return res;				
	}
	
	public static double schedulers(LinkedList<Integer> Scheduler ) {
		sum = 0;
		
		for (int i = 0; i < Scheduler.size(); i++) {
			sum += Scheduler.get(i);			
		}
		return sum;
	}
	
	public static double mediaSchedulers(LinkedList<Integer> Scheduler) {
		sum = 0;
		for (int i = 0; i < Scheduler.size(); i++) {
			sum += Scheduler.get(i);			
		}
		return sum/(Scheduler.size());
	}

	
	public static double mediaTimeScheduler(double seek,LinkedList<Integer> Scheduler) {
		return mediaSchedulers(Scheduler)*seek;		
	}
	

	public static double variance(double media,LinkedList<Integer> Scheduler) {
		sum = 0;		
			
		for (int i = 0; i < Scheduler.size(); i++) {
			sum += Math.pow(Scheduler.get(i) - media, 2);	
			
		}
		return sum/(Scheduler.size() - 1);
	}	
	
	public static double standardDeviation(LinkedList<Integer> Scheduler) {
		return Math.sqrt(variance(mediaSchedulers(Scheduler), Scheduler));		
	}	


}
