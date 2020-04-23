package baekjoon;

import java.util.Scanner;

public class brotherSangsu {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int a = scan.nextInt();
		int b = scan.nextInt();
		
		int c = 
				a/100
				+
				((a-(a/100)*100)/10)*10
				+
				(a-(a/100)*100-((a-(a/100)*100)/10)*10)*100
				;
		int d =
				b/100
				+
				((b-(b/100)*100)/10)*10
				+
				(b-(b/100)*100-((b-(b/100)*100)/10)*10)*100
				;
		if(c>d) {
			System.out.println(c);
		}else {
			System.out.println(d);
		}

	}

}
