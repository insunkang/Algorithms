package exam;

public class Socar3 {
	
//	public static int del(int[][] target,int[][] tip, int m, int n, boolean[][] check, int money, int max,int time) {
//		int[] a = {0,1,0,-1};
//		int[] b = {1,0,-1,0};
//		if (money>max) {
//			max=money;
//		}
//		int k =0 ;
//		int l = 0;
//		int o = 0;
//		for (int i = 0; i < b.length; i++) {
//			if (m+a[i]>=0&&n+b[i]>=0) {
//				l++;
//			}
//			if (target[m+a[i]][n+b[i]]>time) {
//				o++;
//			}
//		}
//		
//		if (l==o) {
//			return max;
//		}else {
//			if (m+a[0]>=0&&n+b[0]>=0&&target[m+a[0]][n+b[0]]<=time) {
//				if (check[m+a[0]][n+b[0]]==false) {
//					money+=tip[m+a[0]][n+b[0]];
//					time++;
//					check[m+a[0]][n+b[0]]=true;
//					del(target,tip,m+a[0],n+b[0],check,money,max,time);
//				}else {
//					time++;
//					del(target,tip,m+a[0],n+b[0],check,money,max,time);
//				}
//			}
//			if (m+a[1]>=0&&n+b[1]>=0&&target[m+a[1]][n+b[1]]<=time) {
//				if (check[m+a[1]][n+b[1]]==false) {
//					money+=tip[m+a[0]][n+b[0]];
//					time++;
//					check[m+a[1]][n+b[1]]=true;
//					del(target,tip,m+a[1],n+b[1],check,money,max,time);
//				}else {
//					time++;
//					del(target,tip,m+a[1],n+b[1],check,money,max,time);
//				}
//			}
//			if (m+a[2]>=0&&n+b[2]>=0&&target[m+a[2]][n+b[2]]<=time) {
//				if (check[m+a[2]][n+b[2]]==false) {
//					money+=tip[m+a[0]][n+b[0]];
//					time++;
//					check[m+a[2]][n+b[2]]=true;
//					del(target,tip,m+a[2],n+b[2],check,money,max,time);
//				}else {
//					time++;
//					del(target,tip,m+a[2],n+b[2],check,money,max,time);
//				}
//			}
//			if (m+a[3]>=0&&n+b[3]>=0&&target[m+a[3]][n+b[3]]<=time) {
//				if (check[m+a[3]][n+b[3]]==false) {
//					money+=tip[m+a[0]][n+b[0]];
//					time++;
//					check[m+a[3]][n+b[3]]=true;
//					del(target,tip,m+a[3],n+b[3],check,money,max,time);
//				}else {
//					time++;
//					del(target,tip,m+a[3],n+b[3],check,money,max,time);
//				}
//			}
//		}
//
//		
//		
//		
//	}

	public static void main(String[] args) {
		int r =3;
		int[][] delivery = {{1, 5},{8, 3},{4, 2},{2, 3},{3, 1},{3, 2},{4, 2},{5, 2},{4, 1}};
		int[][] target = new int[r][r];
		int[][] tip = new int[r][r];
		int j =0;
		for (int i = 0; i < delivery.length; i++) {
			target[j][i%3]=delivery[i][0];
			tip[j][i%3]=delivery[i][1];
			if ((i+1)%3==0) {
				j++;				
			}
		}
		boolean[][] check = new boolean[r][r];
		
		
//		System.out.println(del(target,tip,0,0,check,0,0,0)); 
		
		
		
//		System.out.println(delivery[3][1]);
	}

}
