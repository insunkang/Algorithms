package baekjoon;

import java.util.LinkedList;
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
	
	public static void surveil(int[][] target,int[][] origin, int m, int n, Queue<int[]> key, Queue<Integer> value,int i) {
		
		int[] left = {-1,0,1,0};
		int[] right = {0,1,0,-1};
		while(!key.isEmpty()) {
		if (i>=key.size()) {
			if (check(target, m, n)<result) {
				result = check(target, m, n);
			}
			System.out.println(23);
			for (int j = 0; j < m; j++) {
				for (int j2 = 0; j2 < n; j2++) {
					if (j2==n-1) {
						System.out.println(target[j][j2]);
					}else {
						System.out.print(target[j][j2]);
					}
				}
			}
			target=origin;			
		}else if(i<key.size()){
			System.out.println(12);
			int[] k = key.poll();
			int v = value.poll();
			if (v==1) {
				for (int j = 0; j < 4; j++) {
					int a =k[0]+left[j];
					int b =k[1]+right[j];
					while(a>=0&&b>=0&&a<m&&b<n&&target[a][b]!=6) {
						target[a][b]=-1;
						a+=left[j];
						b+=right[j];
						
					}				
					surveil(target,origin,m,n,key,value,i++);
					target=origin;	
					for (int fd = 0; fd < m; fd++) {
						for (int j2 = 0; j2 < n; j2++) {
							if (j2==n-1) {
								System.out.println(target[fd][j2]);
							}else {
								System.out.print(target[fd][j2]);
							}
						}
					}
				}
				
			}else if (v==2) {
				for (int j = 0; j < 2; j++) {
					int a = k[0]+left[j];
					int b = k[1]+right[j];
					
					while(a>=0&&b>=0&&a<m&&b<n&&target[a][b]!=6) {
						target[a][b]=-1;
						a+=left[j];
						b+=right[j];
					}
										
					int c = k[0]+left[j+2];
					int d = k[1]+right[j+2];
					
					while(c>=0&&d>=0&&c<m&&d<n&&target[c][d]!=6) {
						target[c][d]=-1;
						c+=left[j+2];
						d+=right[j+2];
					}
					surveil(target,origin,m,n,key,value,i++);
					target.equals(origin);
					
				}
				
			}else if (v==3) {
				for (int j = 0; j < 4; j++) {
					int a = k[0]+left[j];
					int b = k[1]+right[j];
					
					while(a>=0&&b>=0&&a<m&&b<n&&target[a][b]!=6) {
						target[a][b]=-1;
						a+=left[j];
						b+=right[j];
					}
					
					
					int c = k[0]+left[(j+1)%4];
					int d = k[1]+right[(j+1)%4];
					
					
					
					while(c>=0&&d>=0&&c<m&&d<n&&target[c][d]!=6) {
						target[c][d]=-1;
						c+=left[(j+1)%4];
						d+=right[(j+1)%4];
					}
					surveil(target,origin,m,n,key,value,i++);
					target.equals(origin);
				}
			}else if (v==4) {
				for (int j = 0; j < 4; j++) {
					int a = k[0]+left[j];
					int b = k[1]+right[j];
					
					while(a>=0&&b>=0&&a<m&&b<n&&target[a][b]!=6) {
						target[a][b]=-1;
						a+=left[j];
						b+=right[j];
					}
										
					int c = k[0]+left[(j+2)%4];
					int d = k[1]+right[(j+2)%4];
					
					while(c>=0&&d>=0&&c<m&&d<n&&target[c][d]!=6) {
						target[c][d]=-1;
						c+=left[(j+2)%4];
						d+=right[(j+2)%4];
					}
					
					int e = k[0]+left[(j+3)%4];
					int f = k[1]+right[(j+3)%4];
					
					while(e>=0&&f>=0&&e<m&&f<n&&target[e][f]!=6) {
						target[e][f]=-1;
						e+=left[(j+3)%4];
						f+=right[(j+3)%4];
					}
					surveil(target,origin,m,n,key,value,i++);
					target.equals(origin);	
				}
			}else if(v==5){
				for (int j = 0; j < 4; j++) {
					int a = k[0]+left[j];
					int b = k[1]+right[j];
					if (a>=0&&b>=0&&a<m&&b<n) {
						while(target[a][b]!=6) {
							target[a][b]=-1;
							a+=left[j];
							b+=right[j];
						}
						
					}
				}
				surveil(target,origin,m,n,key,value,i++);
				target.equals(origin);	
			}
			for (int j = 0; j < m; j++) {
				for (int j2 = 0; j2 < n; j2++) {
					if (j2==n-1) {
						System.out.println(target[j][j2]);
					}else {
						System.out.print(target[j][j2]);
					}
				}
			}
			if (check(target, m, n)<result) {
				result = check(target, m, n);
			}
		}
	}
		
	}
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int m = scan.nextInt();
		int n = scan.nextInt();
		
		int[][] target = new int[m][n];
		result = m*n;
		Queue<int[]> key = new LinkedList<int[]>();
		Queue<Integer> value = new LinkedList<Integer>();
		
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				
				int[] mn = {i,j};
				int put = scan.nextInt();
				target[i][j]= put;
				if (put>0&&put<6) {
					key.add(mn);
					value.add(put);
				}
				
				
			}
		}
		
//		for (int i = 0; i < key.size(); i++) {
//			System.out.println(value.get(i));
//		}
		
		
		surveil(target, target, m, n, key, value, 0);
		
		
		System.out.println(result);
		
		
		
		
		
		
		
		
		
		
		
	}

}
