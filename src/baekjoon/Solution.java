package baekjoon;

import java.util.Scanner;

public class Solution {

 public static void main(String[] args) {
			  Scanner scan = new Scanner(System.in);
			  int first = scan.nextInt();
			  int second = scan.nextInt();
			  String sum = new String();
			  String[] val1 = {};
			  int a = 0 ;
			  int b = 0 ;
			  for(int i =first;i<=second;i++) {
				  	 val1 = Integer.toString(i).split("");
				  																				  				  	
			  		while(val1.length!=1){					  			
					  			sum = "";
					  		for(int j=0;j<val1.length-1;j++) {		
//					  			b = Math.abs(Integer.parseInt(val1[j]) - Integer.parseInt(val1[j+1]));
//					  			if(b>0) {
//								sum =sum+ Integer.toString(b);
//					  			}
					  			
					  			sum =sum+ 
					  			Integer.toString(Math.abs(Integer.parseInt(val1[j]) - Integer.parseInt(val1[j+1])));
					  		 }					  			
					  			val1 = sum.split("");					  								  								  							  									  			
					  		}
					 if(Integer.parseInt(val1[0])==7) {
					  			a=a+1;
					  }
					 
				 }				  			   
			  	
			  System.out.println(a);
			 }

}