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
	public static int zero(int[][] target, int m, int n, int left,int right, boolean[][] checked, int min) {
		if (target[m][n]==1) {
			
			for (int i = 0; i < m; i++) {
				for (int j = 0; j < n; j++) {
					if (target[m][n]>0&&!checked[m][n]) {
						
					}
				}
			}
			
		}else if (target[m][n]==2) {
			
		}else if (target[m][n]==3) {
			
		}else if (target[m][n]==4) {
			
		}else if(target[m][n]==5){
			 
		}else {
			int result = check(target,left,right);
			if (min>result) {
				min=result;
			}
//			return result;
		}
	}
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
