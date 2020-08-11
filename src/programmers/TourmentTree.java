package programmers;

public class TourmentTree {

	public static void main(String[] args) {
		int A =2;
		int B =3;
		int ans = 1;
		if(A>B) {
			while(B+1!=A||B%2==0) {
				
				if(A%2==0) {
					A/=2;
				}else {
					A=(A+1)/2;
				}
				
				if(B%2==0) {
					B/=2;
				}else {
					B=(B+1)/2;
				}
				ans++;
			}
			
		}else if(B>A) {
			while(A+1!=B||A%2==0) {
				
				if(A%2==0) {
					A/=2;
				}else {
					A=(A+1)/2;
				}
				
				if(B%2==0) {
					B/=2;
				}else {
					B=(B+1)/2;
				}
				
				ans++;
			}
		}else {
			
		}
		System.out.println(ans);
	}

}
