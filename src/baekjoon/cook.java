package baekjoon;

import java.util.Scanner;

public class cook {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
				int[] r1;
				int[] r2;
				int[] r3;
				int[] r4;
				int[] r5;
				
				int[] sum;
				
				r1 = new int[4];
				r2 = new int[4];
				r3 = new int[4];
				r4 = new int[4];
				r5 = new int[4];
				
				sum = new int[5];
				
				int point;
				
				int a = 0;
				int b = 0;
				int c = 0;
				int d = 0;
				int e = 0;
				for(int i=0;i<=3;i++) {
					point = scan.nextInt();
					r1[i]=point;
					a = a + point;
   					}
				for(int i=0;i<=3;i++) {
					point = scan.nextInt();
					r2[i]=point;
					b = b + point;
   					}
				for(int i=0;i<=3;i++) {
					point = scan.nextInt();
					r3[i]=point;
					c = c + point;
   					}
				for(int i=0;i<=3;i++) {
					point = scan.nextInt();
					r4[i]=point;
					d = d + point;
   					}
				for(int i=0;i<=3;i++) {
					point = scan.nextInt();
					r5[i]=point;
					e = e + point;
   					}
				sum[0]=a;
				sum[1]=b;
				sum[2]=c;
				sum[3]=d;
				sum[4]=e;
				int dex = 0;
				int max= sum[0];
				for(int i=0;i<sum.length;i++) {
					if(sum[i]>max) {
						max=sum[i];
					}
				}
				if(max==a) {
					dex=1;
				}else if(max==b) {
					dex=2;
				}else if(max==c) {
					dex=3;
				}else if(max==d) {
					dex=4;
				}else if(max==e) {
					dex=5;
				}
				System.out.print(dex+" ");
				System.out.println(max);
	}

}
