package algoBook;

public class Greedy1 {

	public static void main(String[] args) {
//		1�� �ɶ� ����
		
		int n = 25;
		int k = 5;
		int i = 0;
		while(true) {
			if (n==1) {
				break;
			}
			if(n%k!=0) {
				n=n-k;
				i++;
			}else {
				n=n/k;
				i++;
			}
			
			
		}
		
		System.out.println(i);

	}

}
