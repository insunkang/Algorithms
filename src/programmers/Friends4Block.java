package programmers;

public class Friends4Block {

	public static void main(String[] args) {
		int m = 4;
		int n = 4;
		String[] board = {"ABCD", "BACE", "BCDD", "BCDD"};
		String[][] val = new String[m][n];
		
		for(int i=0;i<m;i++) {
			for (int j = 0; j < n; j++) {
				val[i][j]= board[i].split("")[j];
			}
		}
		for(int i=0;i<m;i++) {
			for (int j = 0; j < n; j++) {
				if(j==n-1) {
					System.out.println(val[i][j]);
				}else {
					System.out.print(val[i][j]);
				}
				
			}
		}
		String[][] test = new String[n][m];
		String temp = "";
		for(int i=0;i<n;i++) {
			for (int j = 0; j < m; j++) {
				test[i][j]=val[j][i];
			}
		}
		System.out.println("--------------");
		for(int i=0;i<n;i++) {
			for (int j = 0; j < m; j++) {
				if(j==m-1) {
					System.out.println(test[i][j]);
				}else {
					System.out.print(test[i][j]);
				}
				
			}
		}
	
	int result =0;
	while(true) {
		boolean[][] CB = new boolean[n][m];
		int check = 0;
		
		
		
		for(int i=n-1;i>=0;i--) {
			while(true) {
				for(int j=m-1;j>=1;j--) {
					if(test[i][j].equals("0")&&!test[i][j-1].equals("0")) {
						test[i][j]=test[i][j-1];
						test[i][j-1]="0";
					}
				}
				if(!test[i][m-1].equals("0")) {
					break;
				}
				if(test[i][m-1].equals("0")) {
					int p = 0;
					for(int k=0;k<m;k++) {
						if(test[i][k].equals("0")) {
							p++;
						}
					}
					if(p==m) {
						break;
					}
				}
			}
			
		}
		for(int i=0;i<n;i++) {
			for (int j = 0; j < m-1; j++) {
				if(!test[i][j].equals("0")&&test[i][j+1].equals("0")) {
					test[i][j+1]=test[i][j];
					test[i][j]="0";
				}
			}
		}
	
		for(int i=0;i<n-1;i++) {
			for (int j = 0; j < m-1; j++) {
				if(!test[i][j].equals("0")&&test[i][j].equals(test[i][j+1])&&
						test[i][j].equals(test[i+1][j])&&
							test[i][j].equals(test[i+1][j+1])) {
					CB[i][j]=true;
					CB[i][j+1]=true;
					CB[i+1][j]=true;
					CB[i+1][j+1]=true;
					
				}
				
			}
		}
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if(CB[i][j]==true) {
					test[i][j]="0";
					check++;
					result++;
				}
			}
		}
		System.out.println("--------------");
		for(int i=0;i<n;i++) {
			for (int j = 0; j < m; j++) {
				if(j==m-1) {
					System.out.println(test[i][j]);
				}else {
					System.out.print(test[i][j]);
				}
				
			}
		}
		if(check==0) {
			break;
		}
		
	}
	
	System.out.println(result);
	

	}

}
