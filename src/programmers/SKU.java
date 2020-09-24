package programmers;

public class SKU {

	public static void main(String[] args) {
		int[] input = {1,4,1,2,7,5,2};
		int[] output= new int[10];
		int[] output2= new int[10];
		
		for (int i = 0; i < input.length; i++) {
			int k = input[i];
			output[k]=output[k]+1;
		}
		
		for (int i = 0; i < output.length; i++) {
			System.out.print(output[i]+" ");
		}
		
		for (int i = 0; i < output2.length; i++) {
			int a = 0;
			for (int j = 0; j < input.length; j++) {
				if (i>=input[j]) {
					a++;
				}
			}
			output2[i]=a;
		}
		System.out.println();
		for (int i = 0; i < output2.length; i++) {
			System.out.print(output2[i]+" ");
		}
		
	}

}
