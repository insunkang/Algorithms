package programmers;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class Lifeboat {

	public static void main(String[] args) {
		int[] people = {70, 50, 80, 50};
		
		int limit = 100;
		
		HashMap<Integer, Integer> test = new HashMap<Integer, Integer>();
		ArrayList<Integer> target = new ArrayList<Integer>();
		int result = 0;

		for (int i = 0; i < people.length; i++) {
			target.add(people[i]);
			
		}

		Collections.sort(target);
		int	j=0;
		for (int i = target.size()-1; i >=j; i--) {
		
			
			if(target.get(i)+target.get(j)<=limit) {
				result++;
				j++;
				
			}else {
				result++;
			}
			
		}


		System.out.println(result);
	}

}
