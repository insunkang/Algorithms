package exam;

import java.util.Arrays;

public class Ebay2_2 {
	static int numb =0;
	static int result =0;
	private static void makeOverlabCombination(int r, int[] temp, int current, int start,int[] arr) {
		if (r == current) {
			System.out.println(Arrays.toString(temp));
			int sum = 0 ;
			for (int i = 0; i < temp.length; i++) {
				sum+=temp[i];
			}
			if (sum==numb) {
				result = temp.length;
			}
		} else {
			for (int i = start; i < arr.length; i++) {
				temp[current] = arr[i];
				makeOverlabCombination(r, temp, current + 1, i,arr);
			}
		}
	}
	public static void main(String[] args) {
		int[] cards = {1,4,6};
		int r= 1;
		numb = 8;
		while(true) {
			int[] temp = new int[r];
			makeOverlabCombination(r, temp, 0, 0, cards);
			r++;
			if (result>0) {
				break;
			}
			if (r>=cards.length*cards.length) {
				result=-1;
				break;
			}
		}
		System.out.println(result);
	}

}
