package goorm;
import java.io.*;
public class PrimeNumber {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		int val = Integer.parseInt(input);
		int result = 0;
		for(int i = 2; i*i<val;i++){
			if(val%i==0){
				System.out.print("False");
				result++;
				break;
			}
		}
		if(result==0){
			System.out.print("True");
		}
	}

}
