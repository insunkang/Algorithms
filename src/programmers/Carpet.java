package programmers;

import java.util.ArrayList;

public class Carpet {
	
	public static boolean check(int[][] target, int m, int n ,int yellow) {
		int test = 0;
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (i==0||j==0||i==m-1|j==n-1) {
					test++;
				}
			}
		}
		
		if (((m*n)-test)==yellow) {
			
			return true;
		}else {
			
			
			return false;
		}
	}

	public static void main(String[] args) {
		int brown = 24;
		int yellow = 24;
		int[] answer = new int[2];
		
		
		int mn = brown+yellow;
		
		
		for (int i = 3; i <= mn; i++) {
			if(mn/i>=3&&mn%i==0&&i>=mn/i) {
				
				int m = i;
				int n = mn/i;
				int[][] target = new int[n][m];
				System.out.println(n);
				System.out.println(m);
				if (check(target,n,m,yellow)==true) {
					System.out.println("yes");
					answer[0]=m;
					answer[1]=n;
					
					break;
				}
				
			}
			
		}
		

	}

}
