package programmers;

public class JumpAndTeleport {

	public static void main(String[] args) {
		int n = 5;
		String bi =  Integer.toBinaryString(n);
		int ans =0;
		for (int i = 0; i < bi.length(); i++) {
			if(Character.toString(bi.charAt(i)).equals("1")) {
				ans++;
			}
		}
		System.out.println(ans);
	}

}
