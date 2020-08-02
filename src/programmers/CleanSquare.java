package programmers;

public class CleanSquare {

	public static void main(String[] args) {
		int w =8;
		int h =12;
		int result=0;
		
		
		for(int i=0;i<w;i++) {
			result+=h*i/w;
		}
		System.out.println(result*2);
		
	}

}
