package programmers;

public class Joystick {
	
	public static int up(char target) {
		int result =0;
		result = target-'A';
//		result=Math.abs(result);
		return result;
	}
	public static int down(char target) {
		int result =0;
		result = 'Z'-target+1;
//		result=Math.abs(result);
		return result;
	}
//	public static int lastA(String target, int a, int b) {
//		int result =0;
////		result = 'Z'-target+1;
//		return result;
//	}
	public static int checkleft(String target) {
		int result = 0;
		if(target.charAt(0)==65) {
			result+=1;
			
				for (int i = 1; i < target.length(); i++) {
					if (target.charAt(i)==65) {
						result+=1;
					}else {
						break;
					}
				}
			
		}else {
			
		}
		return result;
	}
	public static int checkright(String target) {
		int result = 0;
		if(target.charAt(target.length()-1)==65) {
			result+=1;
			for (int i = target.length()-2; i >= 0; i--) {
				if (target.charAt(i)==65) {
					result+=1;
				}else {
					break;
				}
			}
		}else {
			
		}
		return result;
	}
	

	public static void main(String[] args) {
		String name = "BBAABAAAA";
		int answer =0;
		
		int number = name.length();
		
		if(checkleft(name)>checkright(name)) {
			
			for(int i =number-1;i>=0;i--) {
				
				if(name.charAt(i)==65) {
					
				}else if(up(name.charAt(i))>down(name.charAt(i))) {
					answer+=down(name.charAt(i));
					System.out.println("up"+up(name.charAt(i)));
					System.out.println("down!"+down(name.charAt(i)));
					
				}else {
					answer+=up(name.charAt(i));
					System.out.println("up!"+up(name.charAt(i)));
					System.out.println("down"+down(name.charAt(i)));
					
				}
				if(i!=0) {
					answer+=1;
				}
			}
			
			answer-=checkleft(name);
			System.out.println("left"+checkleft(name));
			System.out.println("right"+checkright(name));
			answer+=1;
		}else {
			
			for (int i = 0; i < number; i++) {				
				
				if(name.charAt(i)==65) {
					
				}else if(up(name.charAt(i))>down(name.charAt(i))) {
					answer+=down(name.charAt(i));
					System.out.println("up"+up(name.charAt(i)));
					System.out.println("down!"+down(name.charAt(i)));
					
				}else {
					answer+=up(name.charAt(i));
					System.out.println("up!"+up(name.charAt(i)));
					System.out.println("down"+down(name.charAt(i)));
					
				}
				if(i!=0) {
					answer+=1;
				}
			
			}
			answer-=checkright(name);
			System.out.println("right"+checkright(name));
		}
		
		
		
	/*	for (int i = 0; i < number; i++) {				
			
			if(name.charAt(i)==65) {
				
			}else if(up(name.charAt(i))>down(name.charAt(i))) {
				answer+=down(name.charAt(i));
			}else {
				answer+=up(name.charAt(i));
			}
		
		}
		*/
		
//		if(up(name.charAt(0))>down(name.charAt(0))) {
//			answer2+=down(name.charAt(0));
//		}else {
//			answer2+=up(name.charAt(0));
//		}
//		
//		for (int i = number-1; i > 1; i--) {
//			if(name.charAt(i)==65) {
//				
//			}else if(up(name.charAt(i))>down(name.charAt(i))) {
//				answer+=down(name.charAt(i));
//			}else {
//				answer+=up(name.charAt(i));
//			}
//		}
		int check = 0;
		if(name.charAt(0)!=65&&name.charAt(1)==65) {
			for (int i = 1; i < name.length(); i++) {
				if (name.charAt(i)==65) {
					check+=1;
				}else {
					break;
				}
			}
			
		}else if(name.charAt(number-1)!=65&&name.charAt(number-2)==65) {
			for(int i=number-2;i>=0;i--) {
				if (name.charAt(i)==65) {
					check+=1;
				}else {
					break;
				}
			}
			check-=1;
		}
		System.out.println("check"+check);
		answer-=check;
		
		
		
		System.out.println(answer);

	}

}
