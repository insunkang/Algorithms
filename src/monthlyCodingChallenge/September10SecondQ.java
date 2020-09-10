package monthlyCodingChallenge;

public class September10SecondQ {

	public static void main(String[] args) {
		int n = 7;
		int[][] target = new int[n][n];
		
		boolean[][] check = new boolean[n][n];
		
		for (int i = 0; i < check.length; i++) {
			for (int j = 0; j < check.length; j++) {
				if (j>i) {
					check[i][j]=false;
				}else {
					check[i][j]=true;
				}
			}
		}
		target[0][0]=1;
		check[0][0]=false;
		int k = 2;
		int a = 1;
		int b = 0;
		while(true) {
			if (check[a][b]==true) {
				target[a][b]=k;
				check[a][b]=false;
				k++;
				if (a!=b&&a+1<n&&check[a+1][b]==true) {
					a++;
				}else if (a==n-1&&b+1<n&&check[a][b+1]==true) {
					b++;
				}else if (b>0&&a==b&&check[a-1][b-1]==true) {
					a--;
					b--;
				}else if (a==b&&check[a-1][b-1]==false&&check[a+1][b]==true) {
					a++;
				}else if (check[a-1][b]==false) {
					
					if (check[a][b+1]==true) {
						b++;
					}else if (check[a-1][b-1]==true) {
						a--;
						b--;
					}else {
						break;
					}
				}else if (check[a+1][b]==false) {
					if (check[a][b+1]==true) {
						b++;
					}else if (check[a-1][b-1]==true) {
						a--;
						b--;
					}else {
						break;
					}
				}else{
					break;
				}
				
				
			}
		}
		int o = 0;
		int[] answer = new int[k];
		for (int i = 0; i < check.length; i++) {
			for (int j = 0; j < check.length; j++) {
				if (i==j) {
					System.out.println(target[i][j]);
				}else {
					System.out.print(target[i][j]);
					
				}
				
			}
		}
//		for (int i = 0; i < check.length; i++) {
//			for (int j = 0; j < check.length; j++) {
//				if (target[i][j]==0) {
//					
//				}else {
//					answer[o]=target[i][j];
//					o++;
//				}
//				
//			}
//		}

	}

}
