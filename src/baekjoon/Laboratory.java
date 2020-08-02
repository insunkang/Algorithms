package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Laboratory {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		String[] nm = input.split(" ");
		String[] val = new String[Integer.parseInt(nm[0])];
		
		for (int i = 0; i < val.length; i++) {
			val[i] = br.readLine();
		}
		
		
		
		String[][] target = new String[Integer.parseInt(nm[0])][Integer.parseInt(nm[1])];
		for (int i = 0; i < Integer.parseInt(nm[0]); i++) {
			for (int j = 0; j < Integer.parseInt(nm[1]); j++) {
				target[i][j]=val[i].split(" ")[j];
			}
		}
		
//		for (int i = 0; i < Integer.parseInt(nm[0]); i++) {
//			for (int j = 0; j < Integer.parseInt(nm[1]); j++) {
//				
//						System.out.println(target[i][j]);
//			}
//		}
		//1을 3개씩 넣는 경우의 수 들을 어떻게 구하지 ? 
		
		
		
	}

}
