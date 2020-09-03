package goorm;
import java.io.*;
public class ReverseString {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		for(int i=input.length()-1;i>=0;i--){
			System.out.print(input.charAt(i));
		}
	}

}
