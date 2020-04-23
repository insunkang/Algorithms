package baekjoon;

import java.util.HashMap;
import java.util.Scanner;

public class Apartment {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int a = scan.nextInt();
		int key = 0;
		int[][] apartment = new int[a][a];			
		for (int i = 0; i < a; i++) {
			String b = scan.next();
			String[] apart = b.split(""); 
			for (int j = 0; j < a; j++) {
				
				apartment[i][j] = Integer.parseInt(apart[j]);
			}
		}
		HashMap<int[], Integer> result = new HashMap<int[], Integer>(); 
		
		
		//key랑 value를 반대로해서 구분
		for (int i = 0; i < apartment.length; i++) {
			for (int j = 0; j < apartment.length; j++) {
				int[] value = {i,j};
				int[] find1 = {i,j-1};
				int[] find2 = {i-1,j};
				if(i==0) {
					if(j==0) {//[0,0]
						if(apartment[i][j]==1) {
							//int[] value = {i,j};
							result.put(value,key);
							key++;
						}
					}else{//[0,j]
						if(apartment[i][j]==1) {
							if(apartment[i][j-1]==1) {
								//int[] value = {i,j};
								//int[] find1 = {i,j-1};
								result.put(value, result.get(find1));
							}else {
								//int[] value = {i,j};
								result.put(value, key);
								key++;
							}
						}
					}
				}
				else {
					if(j==0) {//[1이상,0]
						if(apartment[i][j]==1) {
							if(apartment[i-1][j]==1) {
								//int[] value = {i,j};
								//int[] find2 = {i-1,j};
								result.put(value, result.get(find2));
							}else {
								//int[] value = {i,j};
								result.put(value,key);
								key ++;
							}
						}
					}else {//[1이상,1이상]
						if(apartment[i][j]==1) {
							if(apartment[i-1][j]==1) {
								//int[] value = {i,j};
								//int[] find2 = {i-1,j};
								result.put(value,result.get(find2));
							}else if(apartment[i][j-1]==1) {
								//int[] value = {i,j};
								//int[] find1 = {i,j-1};
								result.put(value, result.get(find1));
								
							}else {
								//int[] value = {i,j};
								result.put(value, key);
								key++;
							}
						}
						
					}
				}
			}
		}
		
		
//				for (int i = 0; i < a; i++) {
//					for (int j = 0; j < a; j++) {
//						
//							if(apartment[i][j]==1) {
//									if(result.size()==0) {
//										key++;
//									}
//									if(i==0) {
//										
//										if(j==0) {//[0],[0]
//											
//										}else {//[0],[j]
//											
//										}
//										
//									}else {
//										
//										if(j==0) {//[i],[0]
//											
//										}
//										
//									}
//									
//							}else {
//								
//							}
//						
//					}
//				}
		
		System.out.println(key);
		
			System.out.println(result);
		
	}

}
