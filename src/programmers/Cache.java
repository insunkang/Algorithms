package programmers;

import java.util.LinkedList;
import java.util.Queue;

public class Cache {

	public static void main(String[] args) {
		int cacheSize =3;
		String[] cities = {"Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"};
		
		Queue<String> q = new LinkedList<String>();
		
		int result = 0;
		
		int index = 0;
		if(cacheSize==0) {
			result = cities.length*5;
		}else {
			while(index!=cities.length) {
				if (q.size()==cacheSize) {
					if (q.contains(cities[index].toLowerCase())) {
						
						q.remove(cities[index].toLowerCase());
						q.add(cities[index].toLowerCase());
						result=result+1;
					}else {
						q.poll();
						q.add(cities[index].toLowerCase());
						result=result+5;
					}
					
				}else {
					if (q.contains(cities[index].toLowerCase())) {
						
						q.remove(cities[index].toLowerCase());
						q.add(cities[index].toLowerCase());
						result=result+1;
					}else {
						
						q.add(cities[index].toLowerCase());
						result=result+5;
					}
				}
				
				
				
				
				
				index++;			
			}
		}
		
		System.out.println(result);
		

	}

}
