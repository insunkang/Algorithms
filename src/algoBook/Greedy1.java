package algoBook;

public class Greedy1 {

	public static void main(String[] args) {
//		1이 될때 까지
		
//		int n = 25;
//		int k = 5;
//		int i = 0;
//		while(true) {
//			if (n==1) {
//				break;
//			}
//			if(n%k!=0) {
//				n=n-k;
//				i++;
//			}else {
//				n=n/k;
//				i++;
//			}
//			
//			
//		}
//		
//		System.out.println(i);
//		왕실의 나이트
//		String input = "a1";
//		int n =8;
//		String x = "a";
//		int a = input.charAt(1)-'0'-1;
//		int b = (int)input.charAt(0)-(int)x.charAt(0);
//		int result =0 ;
//		System.out.println("a"+a);
//		System.out.println("b"+b);
//		if (a-2>=0&&a-2<n) {
//			if (b-1>=0&&b-1<n) {
//				result++;
//			}else if (b+1>=0&&b-1<n) {
//				result++;
//			}
//		}
//		
//		if (a+2>=0&&a+2<n) {
//			if (b-1>=0&&b-1<n) {
//				result++;
//			}else if (b+1>=0&&b-1<n) {
//				result++;
//			}
//		}
//		
//		if (b+2>=0&&b+2<n) {
//			if (a-1>=0&&a-1<n) {
//				result++;
//			}else if (a+1>=0&&a-1<n) {
//				result++;
//			}
//		}
//		
//		if (b-2>=0&&b-2<n) {
//			if (a-1>=0&&a-1<n) {
//				result++;
//			}else if (a+1>=0&&a-1<n) {
//				result++;
//			}
//		}
//		
//		System.out.println(result);
//	게임 개발
		int m = 4;
		int n = 4;
		int[][] target = {{1, 1, 1, 1}, {1, 0, 0, 1}, {1, 1, 0, 1}, {1, 1, 1, 1}};
		boolean[][] check = new boolean[m][n];
		int dir = 0;
		int[] present = {0,0};
		int[] dx = {-1, 0, 1, 0};
		int[] dy = {0, -1, 0, 1};
		
		int dircheck = 0;
		while(true) {
			if (present[0]+dx[dir]<0&&present[0]+dx[dir]>3&&present[1]+dy[dir]<0&&present[1]+dy[dir]>3||target[present[0]+dx[dir]][present[1]+dy[dir]]==0) {
				if(dir==3) {
					dir=0;
				}else {
					dir++;
				}
				dircheck++;
				if (dircheck==4) {
					break;
				}
				continue;
			}
		}
		
		
		
	}

}
