package baekjoon;

import java.util.Scanner;

public class YoungSick2 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int first = scan.nextInt();
		int second = scan.nextInt();
	
		int a = 0 ;
		
		
		for(int i =first;i<=second;i++) {
			String[] val1 = Integer.toString(i).split("");
			
			while(val1.length!=1) {
				
				for(int j=0;j< val1.length-1;j++) {
					
					val1[j] = Integer.toString(Math.abs(Integer.parseInt(val1[j]) - Integer.parseInt(val1[j+1])));
				}
				
					if(val1.length==1) {
						
							if(Integer.parseInt(val1[0])==7) {
							a=a+1; 	
							}
					
					}
			}//break;
			
		}
		
		System.out.println(a);

	}

}
