package programmers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;

public class BestAlbum {

	public static void main(String[] args) {
//		String[] genres = {"classic","pop", "classic", "classic", "pop","k","k","k"};
//		int[] plays = {500,600, 150, 800, 2500,30000,30000,2};
		String[] genres =  {"c","b","a","b"};
	      int[] plays = {1,3,3,3};
		
		List<Integer> rank = new ArrayList<Integer>();
		
		HashMap<String, List<Integer>> target = new HashMap<String, List<Integer>>();
		
		
		ArrayList<String> gen = new ArrayList<String>();
		HashMap<String,Integer> rankGen = new HashMap<String,Integer>();
		ArrayList<String> rankGenStr = new ArrayList<String>();
		
		for (int i = 0; i < genres.length; i++) {
			
			List<Integer> list = new ArrayList<Integer>();
			
			if (target.containsKey(genres[i])) {
				list = target.get(genres[i]);
				list.add(plays[i]);
				target.put(genres[i], list);
			}else {
				gen.add(genres[i]);
				list.add(plays[i]);
				target.put(genres[i], list);
			}
		}
		

		while(!gen.isEmpty()) {
			String first = gen.get(0);
			int firstSum = target.get(first).stream().mapToInt(Integer::intValue).sum();
			
			String forCal=first ;
			int k =0;
			for (int i = 0; i < gen.size(); i++) {
				if (firstSum<target.get(gen.get(i)).stream().mapToInt(Integer::intValue).sum()) {
					forCal=gen.get(i);
					firstSum=target.get(gen.get(i)).stream().mapToInt(Integer::intValue).sum();
					k=i;
				}
			}
			
			List<Integer> list = new ArrayList<Integer>();
			list = target.get(forCal);
			
			rankGenStr.add(forCal);
			Collections.sort(list,Comparator.reverseOrder());
			if (list.size()>=2) {
				rank.add(list.get(0));
				rank.add(list.get(1));
				rankGen.put(forCal, 2);
			}else {
				rank.add(list.get(0));
				rankGen.put(forCal, 1);
			}
			gen.remove(k);
			
		}
//		System.out.println(rank);
		ArrayList<Integer> result = new ArrayList<Integer>();
		Boolean[] check = new Boolean[genres.length];
		Arrays.fill(check, false);
		while(!rank.isEmpty()) {
			int a = rank.remove(0);
			
			String gens = rankGenStr.get(0);
			System.out.println(gens);
			for (int i = 0; i < plays.length; i++) {
				if (plays[i]==a&&genres[i].equals(gens)&&check[i]==false) {
					result.add(i);
					rankGen.put(gens, rankGen.get(gens)-1);
					check[i]=true;
					break;
				}
			}
			
			if (rankGen.get(gens)==0) {
				rankGenStr.remove(0);
			}
		}
		
		int[] answer = result.stream().mapToInt(i->i).toArray();
		for (int j = 0; j < answer.length; j++) {
			System.out.println(answer[j]);
		}
		
	}

}
