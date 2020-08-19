package programmers;

import java.util.ArrayList;

public class WordChain {

	public static void main(String[] args) {
		int n = 2;
		int result = 0;
//		String[] words = {"tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank","tank"};
//		String[] words = {"hello", "one", "even", "never", "now", "world", "draw"};
		String[] words = {"land", "dream", "mom","mom"};
		for (int i = 1; i < words.length; i++) {
			if (words[i].charAt(0)==words[i-1].charAt(words[i-1].length()-1)) {
				
			}else {
				result = i;
				break;
			}
		}
		ArrayList<String> test = new ArrayList<String>();
		test.add(words[0]);
		int min =0;
		for (int i = 1; i < words.length; i++) {
			if (test.contains(words[i])) {
				min = i ;
				break;
			}else {
				test.add(words[i]);
			}
			
		}
		
		int lastone = 0;
		if (result==0&&min==0) {
			
		}else if(result==0&&min!=0){
			lastone = min;
		}else if(min==0&&result!=0) {
			lastone = result;
		}else {
			lastone = Math.min(min, result);
		}
		
		System.out.println(min);
		System.out.println(result);
		System.out.println(lastone);
		int[] answer = new int[2];
		
		if (lastone==0) {
			answer[0]=0;
			answer[1]=0;
		}else {
			if ((lastone+1)%n==0) {
				answer[0]=n;
				answer[1]=((lastone+1)/n);
			}else {
				answer[0]=(lastone+1)%n;
				answer[1]=((lastone+1)/n)+1;
			}
			
			
		}
		
		
		for (int i = 0; i < answer.length; i++) {
			System.out.println(answer[i]);
		}
		
		
	}

}
