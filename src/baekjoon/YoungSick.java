package baekjoon;

import java.util.Scanner;

public class YoungSick {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int first = scan.nextInt();
		int second = scan.nextInt();
		//String[] val1 = Integer.toString(first).split("");
		//String[] val2 = Integer.toString(second).split("");
		//int[] a ;
		//a = new int[10];
		int a = 0 ;
		String[] val2;
		
		for(int i =first;i<=second;i++) {
			String[] val1 = Integer.toString(i).split("");
			
			if(val1.length==1) {
				
				if(val1[0]=="7") {
					a= a+1;
				}
				break;
			
			}else {
			
			for(int j=0;j<val1.length-1;j++) {
				int b= Integer.parseInt(val1[j]) - Integer.parseInt(val1[j+1]);
				
			}
		  }
		}
		

	}

}
