package programmers;

import java.util.LinkedList;
import java.util.Queue;

public class Pressing {

	public static void main(String[] args) {
		String s = "aabbaccc";
		int min = s.length();
		int check=1;
		
		
		
		while(check<=s.length()/2) {
			int length=0;
			
				length=s.length()/check+1;
			
			String[] a = new String[length];
			Queue<String> queue = new LinkedList<>(); 
			
			for (int i = 0; i < a.length; i++) {
				int o = i*check;
				int k = o+check;
				if(k>s.length()) {
					a[i]=s.substring(o, s.length());
					queue.add(s.substring(o, s.length()));
				}else {
					a[i]=s.substring(o, k);
					queue.add(s.substring(o, k));
				}
				
			}
			
			String result = "";
			
			String backN = "";
			int frontN=1;
			System.out.println("length"+a.length);
			for (int i = 0; i < a.length; i++) {
				
				String cp = queue.remove();
				System.out.print(backN+"___");
				System.out.println(cp);
				if(backN.equals(cp)) {
					
					frontN++;
					
				}else {
					
					if(frontN==1) {
						
						result+=backN;
						
					}else {
						
						result+=frontN+backN;
						
					}
					
					backN=cp;
					frontN=1;
				}
			}
			if(backN!="") {
				result+=backN;
			}
			System.out.println("result= "+result);
			
			if(min>result.length()) {
				min=result.length();
			}
			
		

			check++;
		}

		System.out.println(min);

	}

}
