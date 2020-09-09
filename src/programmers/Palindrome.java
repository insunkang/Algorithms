package programmers;

import java.util.HashMap;

public class Palindrome {

	public static void main(String[] args) {
		String s = "abcdcba";
		int answer = 1 ;
		
		
//		HashMap<String, Integer> target = new HashMap<String, Integer>();
		
		
//		for (int i = 0; i < s.length(); i++) {
//			if (target.containsKey(Character.toString(s.charAt(i)))) {
//				target.put(Character.toString(s.charAt(i)), target.get(Character.toString(s.charAt(i)))+1);
//			}else {
//				target.put(Character.toString(s.charAt(i)), 1);
//			}
//			
//		}
//		for (int i = 0; i < s.length(); i++) {
//			if (target.get(Character.toString(s.charAt(i)))%2==1) {
////				System.out.println(i);
//				int left = i-1;
//				int right = i+1;
//				int result=1;
//				while(i!=0&&i!=s.length()-1&&left>=0&&right<=s.length()-1) {
//					if (s.charAt(left)==s.charAt(right)) {
//						result=result+2;
//						left=left-1;
//						right=right+1;
//					}else {
//						break;
//					}
//				}
//				if (answer<result) {
//					answer=result;
//				}
//				
//			}
//		}
		
		for (int i = 1; i < s.length(); i++) {
			int left =i-1;
			int right=i+1;
			int result=1;
			while(left>=0&&right<=s.length()-1) {
				if (s.charAt(left)==s.charAt(right)) {
					result=result+2;
					left=left-1;
					right=right+1;
				}else {
					break;
					
				}
			}
			if(result>answer) {
				answer=result;
			}
		}
		for (int i = 0; i < s.length()-1; i++) {
			
			int right=i+1;
			int result=0;
			if (s.charAt(i)==s.charAt(right)) {
				int left=i-1;
				right=right+1;
				result=result+2;
				while(left>=0&&right<=s.length()-1) {
					if (s.charAt(left)==s.charAt(right)) {
						result=result+2;
						left=left-1;
						right=right+1;
					}else {
						break;
						
					}
				}
			}
			
			if(result>answer) {
				answer=result;
			}
			if (s.length()==1) {
				answer=1;
			}
		}
		
		System.out.println(answer);
	}

}
