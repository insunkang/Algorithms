package exam;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class Coupang3 {

	public static void main(String[] args) {
		int k = 3;
		int[] score = {24,22,20,10,5,3,2,1};
		
		int[] multi = new int[score.length];
		int[] lastmulti = new int[score.length];
		
		HashMap<Integer, Integer> check = new HashMap<Integer, Integer>();
		int answer = 0;
		
		
		
		if (score.length<3) {
			System.out.println(0);
//			return answer;
		}else {
			multi[0] = Math.abs(score[0]-score[1]);
			lastmulti[0] = Math.abs(score[0]-score[1]);
			
			for (int i = 1; i < score.length; i++) {
				multi[i] = Math.abs(score[i] - score[i-1]);
				lastmulti[i] = Math.abs(score[i] - score[i-1]);
			}
//			ArrayList<Integer> multiA = new ArrayList<Integer>();
//			
//			for (int i = 0; i < multi.length; i++) {
//				multiA.add(multi[i]);
//			}
			
			Arrays.sort(multi);
			for (int i = 0; i < multi.length; i++) {
//				System.out.println(multi[i]);
			}
				
			ArrayList<Integer> result = new ArrayList<Integer>();
			
			int last = 0;
			int a = 0;
			int keys = 0;
			for (int i = 0; i < multi.length; i++) {
				
				
				if (check.containsKey(multi[i])) {
					int test = check.get(multi[i])+1;
					check.put(multi[i], test);
					a++;
					
					
				}else {
					if (a+1>=k) {
						last=last+a+1;
						a=0;
						result.add(keys);
					}
					keys = multi[i];
					check.put(multi[i], 1);
				}
			}
			
			
			int[] Finalist = new int[score.length];
			
			for (int i = 1; i < lastmulti.length; i++) {
				for (int j = 0; j < result.size(); j++) {
					if (lastmulti[i]==result.get(j)) {
						Finalist[i-1]=1;
						Finalist[i]=1;
					}
				}
			}
			
			for (int i = 0; i < Finalist.length; i++) {
//				System.out.println(Finalist[i]);
				if (Finalist[i]==0) {
					answer++;
				}
			}
//			System.out.println(result);
//			System.out.println(score.length-a);
			System.out.println(answer);
		}
		
		

	}

}
