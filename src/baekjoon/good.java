package baekjoon;

import java.lang.reflect.Array;
import java.util.Scanner;

public class good {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
			
			int[] r1;
			r1 = new int[10];
			int point;
			int a = 0;
			for(int i=0;i<r1.length;i++) {
				point = scan.nextInt();
				r1[i]=point%42;
					}
//			for(int i=0;i<r1.length;i++) {
//				System.out.print(r1[i]+" ");
//					}
			int[] check;
			check = new int[9];
			
			for(int i=1;i<r1.length;i++) {
			if(r1[0]==r1[i]) {
				check[0]=0;
				break;
			}else {
					check[0]=1;
				}
			}
			for(int i=2;i<r1.length;i++) {
				if(r1[1]==r1[i]) {
					check[1]=0;
					break;
				}else {
					check[1]=1;
				}
			}
			for(int i=3;i<r1.length;i++) {
				if(r1[2]==r1[i]) {
					check[2]=0;
					break;
				}else {
					check[2]=1;
				}
			}
			for(int i=4;i<r1.length;i++) {
				if(r1[3]==r1[i]) {
					check[3]=0;
					break;
				}else {
					check[3]=1;
				}
			}
			for(int i=5;i<r1.length;i++) {
				if(r1[4]==r1[i]) {
					check[4]=0;
					break;
				}else {
					check[4]=1;
				}
			}
			for(int i=6;i<r1.length;i++) {
				if(r1[5]==r1[i]) {
					check[5]=0;
					break;
				}else {
					check[5]=1;
				}
			}
			for(int i=7;i<r1.length;i++) {
				if(r1[6]==r1[i]) {
					check[6]=0;
					break;
				}else {
					check[6]=1;
				}
			}
			for(int i=8;i<r1.length;i++) {
				if(r1[7]==r1[i]) {
					check[7]=0;
					break;
				}else {
					check[7]=1;
				}
			}
			for(int i=9;i<r1.length;i++) {
				if(r1[8]==r1[i]) {
					check[8]=0;
					break;
				}else {
					check[8]=1;
				}
			}
			int sum =1;
			for(int i=0;i<check.length;i++) {
				sum = sum+check[i];
			
			
			
					}
			System.out.println(sum);
	}

}
