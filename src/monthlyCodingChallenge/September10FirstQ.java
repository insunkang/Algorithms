package monthlyCodingChallenge;

import java.util.ArrayList;
import java.util.Collections;

public class September10FirstQ {

	public static void main(String[] args) {
		int[] numbers =	{2,1,3,4,1};
		ArrayList<Integer> target = new ArrayList<Integer>();
		for (int i = 0; i < numbers.length-1; i++) {
			for (int j = i+1; j < numbers.length; j++) {
				if (target.contains(numbers[i]+numbers[j])) {
					
				}else {
					target.add(numbers[i]+numbers[j]);
				}
			}
		}
		Collections.sort(target);
		int[] answer = target.stream().mapToInt(i->i).toArray();
		System.out.println(answer);
	}

}
