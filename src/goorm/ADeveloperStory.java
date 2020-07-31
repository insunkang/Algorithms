package goorm;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;

public class ADeveloperStory {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		
		int division = 2;
		String a = null ;
		
		while(true) {
			
			int test = Integer.parseInt(input);
			Stack<Integer> value = new Stack<Integer>();
			while(test<division) {
				value.add(test/division);
				test= test%division;
				
			}
			for (int i = 0; i < value.size(); i++) {
				a=a+value.pop();
				System.out.println(a);
			}
			
			
			
			if(Math.sqrt(Double.parseDouble(a))-Math.sqrt(Double.parseDouble(a))/Math.sqrt(Double.parseDouble(a))==0) {
				break;
			}
			division++;
		}
		
		System.out.println(division);
	}

}
