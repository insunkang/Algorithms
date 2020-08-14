package baekjoon;

import java.util.Scanner;

public class Imigration {
	public static boolean sum(int n, int l, int r, int[][] target) {
		int[] left = {-1,1,0,0};
		int[] right = {0,0,-1,1};
		boolean result = true;
		int check = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if(i+left[0]>=0&&j+right[0]>=0) {
					if(Math.abs(target[i][j]-target[i+left[0]][j+right[0]])>=l&&Math.abs(target[i][j]-target[i+left[0]][j+right[0]])<=r) {
						check++;
					}
				}
				if(i+left[1]>=0&&j+right[1]>=0) {
					if(Math.abs(target[i][j]-target[i+left[1]][j+right[1]])>=l&&Math.abs(target[i][j]-target[i+left[1]][j+right[1]])<=r) {
						check++;
					}
				}
				if(i+left[2]>=0&&j+right[2]>=0) {
					if(Math.abs(target[i][j]-target[i+left[2]][j+right[2]])>=l&&Math.abs(target[i][j]-target[i+left[2]][j+right[2]])<=r) {
						check++;
					}
				}
				if(i+left[3]>=0&&j+right[3]>=0) {
					if(Math.abs(target[i][j]-target[i+left[3]][j+right[3]])>=l&&Math.abs(target[i][j]-target[i+left[3]][j+right[3]])<=r) {
						check++;
					}
				}
			}
		}
		if(check>0) {
			result=false;
		}else {
			result=true;
		}
		return result;
	}
	public static boolean[][] unionM(int n, int l, int r,int i,int j, int[][] target, boolean[][] check,int union) {
		int[] left = {-1,1,0,0};
		int[] right = {0,0,-1,1};
		boolean result = true;
		
		
				if(i+left[0]>=0&&j+right[0]>=0&&check[i][j]==false) {
					if(Math.abs(target[i][j]-target[i+left[0]][j+right[0]])>=l&&Math.abs(target[i][j]-target[i+left[0]][j+right[0]])<=r) {
						check[i][j]=true;
						unionM(n,l,r,i+left[0],j+right[0],target,check,union);
					}
				}
				if(i+left[1]>=0&&j+right[1]>=0&&check[i][j]==false) {
					if(Math.abs(target[i][j]-target[i+left[1]][j+right[1]])>=l&&Math.abs(target[i][j]-target[i+left[1]][j+right[1]])<=r) {
						check[i][j]=true;
						unionM(n,l,r,i+left[1],j+right[1],target,check,union);
					}
				}
				if(i+left[2]>=0&&j+right[2]>=0&&check[i][j]==false) {
					if(Math.abs(target[i][j]-target[i+left[2]][j+right[2]])>=l&&Math.abs(target[i][j]-target[i+left[2]][j+right[2]])<=r) {
						check[i][j]=true;
						unionM(n,l,r,i+left[2],j+right[2],target,check,union);
					}
				}
				if(i+left[3]>=0&&j+right[3]>=0&&check[i][j]==false) {
					if(Math.abs(target[i][j]-target[i+left[3]][j+right[3]])>=l&&Math.abs(target[i][j]-target[i+left[3]][j+right[3]])<=r) {
						check[i][j]=true;
						unionM(n,l,r,i+left[3],j+right[3],target,check,union);
					}
				}
		
			return check;
		}

		
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int l = scan.nextInt();
		int r = scan.nextInt();
		
		
		int[] left = {-1,1,0,0};
		int[] right = {0,0,-1,1};
		
		int[][] target = new int[n][n];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				target[i][j]= scan.nextInt();
			}
		}
		int checkNum= 0;
		
		boolean visited[][] = new boolean[n][n];
		
		while(sum(n,l,r,target)==false) {
			
			for (int i = 0; i < target.length; i++) {
				
				for (int j = 0; j < target.length; j++) {
					if(visited[i][j]==false) {
						
						
						
						
					}
				}
			}
		}
		
				
		
	}

}
