package programmers;

import java.util.ArrayList;
import java.util.List;

public class TakeGroupPhoto {
	private static void reculsion(List<String> arr, List<String> result, int n, int r,String[] data, int number,int answer) {
		
		if (r == 0) {
			for (int i = 0; i < data.length; i++) {
				if(Character.toString(data[i].charAt(3)).equals("=")) {
					if(Math.abs(result.indexOf(data[i].charAt(0))-result.indexOf(data[i].charAt(2)))==Integer.parseInt(Character.toString(data[i].charAt(4)))) {
							answer++;
					}
				}else if(Character.toString(data[i].charAt(3)).equals("=")) {
					
				}else if(Character.toString(data[i].charAt(3)).equals("=")) {
					
				}
				 
			}
//			System.out.println(result.toString());
			return;
		}

		for (int i = 0; i < n; i++) {

			result.add(arr.remove(i));
			reculsion(arr, result, n - 1, r - 1,data,number,answer);
			arr.add(i, result.remove(result.size() - 1));
		}
	}

	public static void main(String[] args) {
		int number = 2;
		String[] data = {"N~F=0", "R~T>2"};
		int answer =0;
		List<String> arr = new ArrayList<>();
		arr.add("A");
		arr.add("C");
		arr.add("F");
		arr.add("J");
		arr.add("M");
		arr.add("N");
		arr.add("R");
//		arr.add("T");
		
		List<String> result = new ArrayList<>();
		reculsion(arr, result, arr.size(), 7, data,number,answer);
	}

}
