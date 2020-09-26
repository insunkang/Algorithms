package exam;

import java.util.ArrayList;
import java.util.Collections;

public class Naver2 {

	public static void main(String[] args) {
		int n = 9;
		int[][] edges= {{0,2},{2,1},{2,4},{3,5},{5,4},{5,7},{7,6},{6,8}};
		
		ArrayList<ArrayList<Integer>> node = new ArrayList<ArrayList<Integer>>();
		 for(int i = 0; i < n; i++) {
	            node.add(new ArrayList<Integer>()); 
	        }
		for (int i = 0; i < edges.length; i++) {
			int m = edges[i][0];
			int h = edges[i][1];
			node.get(m).add(h);
			node.get(h).add(m);
		}
		ArrayList<Integer> result = new ArrayList<Integer>();
		int max = 0;
		
		for (int i = 0; i < node.size(); i++) {
			if (node.get(i).size()>max) {
				max=node.get(i).size();
			}
		}
		for (int i = 0; i < node.size(); i++) {
			if (node.get(i).size()==max) {
				result.add(i);
			}
		}
		Collections.sort(result);
		int[] answer = new int[result.size()];
		
		for (int i = 0; i < answer.length; i++) {
			answer[i]=result.get(i);
		}
		for (int i = 0; i < answer.length; i++) {
			System.out.println(answer[i]);
		}

	}

}
