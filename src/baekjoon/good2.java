package baekjoon;

import java.lang.reflect.Array;
import java.util.Scanner;

public class good2 {

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

			int[] check;
			check = new int[9];
			
			for(int an=0;an<=9;an++) {
				for(int i=an+1;i<r1.length;i++) {
					if(r1[an]==r1[i]) {
						check[an]=0;
						break;
					}else {
							check[an]=1;
						}
					}
			}
			
			int sum =1;
			for(int i=0;i<check.length;i++) {
				sum = sum+check[i];
								
					}
			System.out.println(sum);
	}

}
