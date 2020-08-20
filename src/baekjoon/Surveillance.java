package baekjoon;

public class Surveillance {
	
	public static int check(int[][] target, int m, int n) {
		int result =0;
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (target[i][j]==0) {
					result++;
				}
			}
		}
		return result;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
