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
		
		int[][] target = new int[][];
		
		
	}

}
