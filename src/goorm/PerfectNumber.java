package goorm;
import java.io.*;
public class PerfectNumber {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		String[] val = input.split(" ");
		int a = Integer.parseInt(val[0]);
		int b = Integer.parseInt(val[1]);
		
		for(int i = a; i<=b;i++){
			int tot = 0;
			for(int j = 1; j <= i-1; j++){
				if(i%j==0){
					tot+=j;
				}
			}
			if(tot==i){
				System.out.print(i+" ");
			}
		}

	}

}
