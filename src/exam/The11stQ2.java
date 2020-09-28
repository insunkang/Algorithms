package exam;

public class The11stQ2 {

	public static void main(String[] args) {
		
		String[] S = {"zzzz","ferz","zdsr","fgtd"};
		int len = S[0].length();
		int[] solution = {0,0,0};
//		for (int i = 0; i < S.length; i++) {
//			String a ="";
//			String b ="";
//			int leftint=0;
//			int rightint=0;
//			for (int j=i+1 ; j < S.length; j++) {
//				a= S[i];
//				 b= S[j];
//				leftint = i;
//				rightint = j;
//				
//			}
//			System.out.println(rightint+"rj");
//			for (int k = 0; k < len; k++) {
//				String Left = Character.toString(a.charAt(k));
//				 String Right = Character.toString(b.charAt(k));
//
//				if (Left.equals(Right)) {
//					solution[0]=leftint;
//					solution[1]=rightint;
//					solution[2]=k;
//				}
//				if (solution[1]>0) {
//					break;
//				}
//			}
//			
//			if (solution[1]>0) {
//				break;
//			}
//			
//			
//		}
		for (int i = 0; i < S.length; i++) {
			for (int j=i+1 ; j < S.length; j++) {
				for (int k = 0; k < len; k++) {
					String a = Character.toString(S[i].charAt(k));
					String b = Character.toString(S[j].charAt(k));
					if (a.equals(b)) {
						solution[0]=i;
						solution[1]=j;
						solution[2]=k;
					}
					if (solution[1]>0) {
						break;
					}
				}
				if (solution[1]>0) {
					break;
				}
			}
			
		}
		if (solution[1]==0) {
			System.out.println(new int[1]);
		}else {
			System.out.println(solution[0]+""+solution[1]+""+solution[2]);
		}
		

	}

}
