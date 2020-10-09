package exam;

public class Coupang1 {

	public static void main(String[] args) {
		int N = 14;
		int k=0;
		int max = 0;
		int[] answer = new int[2];
		for (int i = 2; i <=9 ; i++) {
			int a = N;
			int multi = 1;
			
			
			while(a>=i) {
				int last = a%i;
				
				if (last!=0) {
					multi=multi*last;
				}
				a=a/i;
				
			}
			multi=multi*a;
			if (multi>=max) {
				k=i;
				max=multi;
			}
		}
//		System.out.println(max);
		answer[0] = k;
		answer[1] = max;
		for (int i = 0; i < answer.length; i++) {
			System.out.println(answer[i]);
		}
		
	}

}
