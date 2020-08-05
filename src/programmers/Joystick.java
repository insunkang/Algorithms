package programmers;

public class Joystick {
	
	public static int up(char target) {
		int result =0;
		result = target-'A';
		
		return result;
	}
	public static int down(char target) {
		int result =0;
		result = 'Z'-target+1;
		return result;
	}
	public static int lastA(String target, int a, int b) {
		int result =0;
//		result = 'Z'-target+1;
		return result;
	}

	public static void main(String[] args) {
		String name = "JAN";
		int answer =0;
		int answer2 =0;
		int number = name.length();
		int check = 0;
		for (int i = 0; i < number; i++) {				
			
			if(name.charAt(i)==65) {
				
			}else if(up(name.charAt(i))>down(name.charAt(i))) {
				answer+=down(name.charAt(i));
			}else {
				answer+=up(name.charAt(i));
			}
		
		}
		
		if(up(name.charAt(0))>down(name.charAt(0))) {
			answer2+=down(name.charAt(0));
		}else {
			answer2+=up(name.charAt(0));
		}
		
		for (int i = number-1; i > 1; i--) {
			if(name.charAt(i)==65) {
				
			}else if(up(name.charAt(i))>down(name.charAt(i))) {
				answer+=down(name.charAt(i));
			}else {
				answer+=up(name.charAt(i));
			}
		}
		
//		if(name.charAt(1)==65||name.charAt(name.length()-1)==65) {
//			answer +=number-2;	
//		}else {
//			answer +=number-1;
//		}
		
		
		
		
		System.out.println(answer);

	}

}
