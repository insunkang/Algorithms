package baekjoon;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;

public class Surveillance {
	static int result;
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
	
	public static void surveil(int[][] target,int[][] origin, int m, int n, List<int[]> key, Queue<Integer> value,int i) {		
		int[] left = {-1,0,1,0};
		int[] right = {0,1,0,-1};
		
		if (key.size()==i) {
			if (check(target, m, n)<result) {
				result = check(target, m, n);
			}
			return;
		}
		
		
			int[] k = key.get(i);
			int v = origin[k[0]][k[1]];
			
			if (v==1) {
				
				for (int j = 0; j < 4; j++) {
					int[][] nextTarget = new int[m][n];
					for (int l = 0; l < m; l++) {
						for (int l2 = 0; l2 < n; l2++) {
							nextTarget[l][l2]=target[l][l2];
						}
					}
					int a =k[0]+left[j];
					int b =k[1]+right[j];
					while(a>=0&&b>=0&&a<m&&b<n&&nextTarget[a][b]!=6) {
						
						
						nextTarget[a][b]=8;													
						a+=left[j];
						b+=right[j];
						
					}
					
					
					surveil(nextTarget,origin,m,n,key,value,i+1);
					
//					for (int l = 0; l < m; l++) {
//						for (int l2 = 0; l2 < n; l2++) {
//							target[l][l2]=origin[l][l2];
//							}
//					}
					
				}
				
			}else if (v==2) {
				
				for (int j = 0; j < 2; j++) {
					int[][] nextTarget = new int[m][n];
					for (int l = 0; l < m; l++) {
						for (int l2 = 0; l2 < n; l2++) {
							nextTarget[l][l2]=target[l][l2];
						}
					}
					int a = k[0]+left[j];
					int b = k[1]+right[j];
					
					while(a>=0&&b>=0&&a<m&&b<n&&nextTarget[a][b]!=6) {
						
						nextTarget[a][b]=8;
						a+=left[j];
						b+=right[j];
					}
										
					int c = k[0]+left[j+2];
					int d = k[1]+right[j+2];
					
					while(c>=0&&d>=0&&c<m&&d<n&&nextTarget[c][d]!=6) {
						
						nextTarget[c][d]=8;
						c+=left[j+2];
						d+=right[j+2];
					}
					
					
					surveil(nextTarget,origin,m,n,key,value,i+1);
//					for (int l = 0; l < m; l++) {
//						for (int l2 = 0; l2 < n; l2++) {
//							target[l][l2]=origin[l][l2];
//						}
//					}
					
					
				}
				
			}else if (v==3) {
				
				for (int j = 0; j < 4; j++) {
					int[][] nextTarget = new int[m][n];
					for (int l = 0; l < m; l++) {
						for (int l2 = 0; l2 < n; l2++) {
							nextTarget[l][l2]=target[l][l2];
						}
					}
					int a = k[0]+left[j];
					int b = k[1]+right[j];
					
					while(a>=0&&b>=0&&a<m&&b<n&&nextTarget[a][b]!=6) {
						
						nextTarget[a][b]=8;
						a+=left[j];
						b+=right[j];
					}
					
					
					int c = k[0]+left[(j+1)%4];
					int d = k[1]+right[(j+1)%4];
					
					
					
					while(c>=0&&d>=0&&c<m&&d<n&&nextTarget[c][d]!=6) {
						
						nextTarget[c][d]=8;
						c+=left[(j+1)%4];
						d+=right[(j+1)%4];
					}
					
					
					
					surveil(nextTarget,origin,m,n,key,value,i+1);
					
//					for (int l = 0; l < m; l++) {
//						for (int l2 = 0; l2 < n; l2++) {
//							target[l][l2]=origin[l][l2];
//						}
//					}
				}
				
			}else if (v==4) {
				
				for (int j = 0; j < 4; j++) {
					int[][] nextTarget = new int[m][n];
					for (int l = 0; l < m; l++) {
						for (int l2 = 0; l2 < n; l2++) {
							nextTarget[l][l2]=target[l][l2];
						}
					}
					int a = k[0]+left[j];
					int b = k[1]+right[j];
					
					while(a>=0&&b>=0&&a<m&&b<n&&nextTarget[a][b]!=6) {
						
						nextTarget[a][b]=8;
						a+=left[j];
						b+=right[j];
					}
										
					int c = k[0]+left[(j+2)%4];
					int d = k[1]+right[(j+2)%4];
					
					while(c>=0&&d>=0&&c<m&&d<n&&nextTarget[c][d]!=6) {
						
						nextTarget[c][d]=8;
						c+=left[(j+2)%4];
						d+=right[(j+2)%4];
					}
					
					int e = k[0]+left[(j+3)%4];
					int f = k[1]+right[(j+3)%4];
					
					while(e>=0&&f>=0&&e<m&&f<n&&nextTarget[e][f]!=6) {
						
						nextTarget[e][f]=8;
						e+=left[(j+3)%4];
						f+=right[(j+3)%4];
					}
					
					
					
					surveil(nextTarget,origin,m,n,key,value,i+1);
					
//					for (int l = 0; l < m; l++) {
//						for (int l2 = 0; l2 < n; l2++) {
//							target[l][l2]=origin[l][l2];
//						}
//					}
					
				}
			}else if(v==5){
				int[][] nextTarget = new int[m][n];
				for (int l = 0; l < m; l++) {
					for (int l2 = 0; l2 < n; l2++) {
						nextTarget[l][l2]=target[l][l2];
					}
				}
				for (int j = 0; j < 4; j++) {
					
					int a = k[0]+left[j];
					int b = k[1]+right[j];
					
					while(a>=0&&b>=0&&a<m&&b<n&&nextTarget[a][b]!=6) {
						
						nextTarget[a][b]=8;
						a+=left[j];
						b+=right[j];
					}
					
					
				}
				surveil(nextTarget,origin,m,n,key,value,i+1);
				
				
				
			}
			
			
		
	
		
		
	}
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int m = scan.nextInt();
		int n = scan.nextInt();
		
		int[][] target = new int[m][n];
		int[][] origin = new int[m][n];
		result = m*n;
		
		
		
		Queue<Integer> value = new LinkedList<Integer>();
		
		List<int[]> key = new ArrayList<int[]>();
		
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				
				int[] mn = {i,j};
				int put = scan.nextInt();
				target[i][j]= put;
				origin[i][j]= put;
				if (put>0&&put<6) {
					key.add(mn);
					value.add(put);
				}
				
				
			}
		}
		
//		for (int i = 0; i < key.size(); i++) {
//			System.out.println(value.peek());
//		}
		
		
		surveil(target, origin, m, n, key, value,0);
		
		
		System.out.println(result);
		
		
		
		
		
		
		
		
		
		
		
	}

}
