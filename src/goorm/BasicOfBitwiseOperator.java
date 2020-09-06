package goorm;
import java.io.*;
public class BasicOfBitwiseOperator {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		String[] val = input.split(" ");
		
		System.out.println(Integer.parseInt(val[0])>>Integer.parseInt(val[1]));
		System.out.println(Integer.parseInt(val[0])<<Integer.parseInt(val[1]));

	}

}
