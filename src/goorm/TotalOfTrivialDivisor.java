package goorm;
import java.io.*;
public class TotalOfTrivialDivisor {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		int val = Integer.parseInt(input);
		int result = 0;
		for(int i = 1; i<=val;i++){
			if(val%i==0){
				result+=i;
			}
		}
		
		System.out.print(result);

	}

}
