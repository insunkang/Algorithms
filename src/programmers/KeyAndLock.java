package programmers;

import java.util.ArrayList;

public class KeyAndLock {

	public static void main(String[] args) {
		int[][] key = {{0, 0, 0}, {1, 0, 0}, {0, 1, 1}};
		int[][] lock = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}};
		
		
		
		ArrayList<int[]> targetLock = new ArrayList<int[]>();

		
		for (int i = 0; i < lock.length; i++) {
			for (int j = 0; j < lock.length; j++) {
				if (lock[i][j]==0) {
					int[] a = new int[2];
					a[0]=i;
					a[1]=j;
					targetLock.add(a);
				}
			}
		}
		
		
		int k =key.length-1;
		int[][] target = new int[lock.length+k*2][lock.length+k*2];
		
		for (int i = 0; i < target.length; i++) {
			for (int j = 0; j < target.length; j++) {
				if (i>=k&&i<target.length+k&&j>=k&&j<target.length+k) {
					target[i][j]=0;
				}else {
					target[i][j]=1;
				}
			}
		}
		
		
		
		
	}

}
