package exam;

public class NT2 {
	public static int result =0;
	public static int check(int[][] target, int n) {
		int a= 0;
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < n; j++) {
				if(target[i][j]>0) {
					a++;
				}
			}
		}
		if (a==n*2) {
			return 1;
		}else {
			return 0;
		}
	}
	public static void dfs(int[][] target, int m, int n) {
		int[][] targetA = new int[2][n];
		int[][] targetB = new int[2][n];
		
		if (m==n) {
			result++;
			return;
		}
		
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < n; j++) {
				targetA[i][j]=target[i][j];
				targetB[i][j]=target[i][j];
			}
		}
		int[] dx = { 1, 0};
		int[] dy = { 0, 1};
		targetA[0][m]=1;
		targetA[1][m]=1;
		dfs(targetA, m+1, n);
		if (m+1<n) {
			targetB[0][m]=1;
			targetB[1][m]=1;
			targetB[0][m+1]=1;
			targetB[1][m+1]=1;		
			dfs(targetB, m+2, n);
		}
		
		
		
	}

	public static void main(String[] args) {
		int n = 7;
		
		int[][]	 target = new int[2][n];
		for (int i = 0; i < 2; i++) {
			for (int j = 0; j < n; j++) {
				target[i][j]=0;
			}
		}
		
		
		dfs(target,0, n);
		
		System.out.println(result);
	}

}
