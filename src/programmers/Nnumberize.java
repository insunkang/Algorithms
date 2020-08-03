package programmers;

public class Nnumberize {

	public static void main(String[] args) {
		int n = 16; //진법 
		int t = 16 ; //말해야하는 숫자 
		int m = 2; //사람수 
		int p = 2; //순서			
		int count= 0;
		String number ="";	
		
		while(number.length()<=t*m+(p-1)) {
			String target="";
			int val = count;
			if(val<n) {
				if(val>=10) {
					target+=(char)(val+55);
				}else {
					target+=val;
				}
				
			}else {
				while(true) {
					
						if(val%n>=10) {
							target=(char)(val%n+55)+target;
						}else {
							target=val%n+target;
						}																	
						val=val/n;															
					if(val<n) {
						if(val>=10) {
							target=(char)(val+55)+target;
						}else {
							target=val+target;
						}						
						break;
					}
					
				}
			}			
			number+=target;
			count++;						
		}	
		String result="";
		int ch=p-1;
		int stop = 0;
		while(true) {
			
			result+=number.charAt(ch);
			ch+=m;
			stop++;
			if(stop==t) {
				break;
			}
		}
//		for(int i =p-1; i<t*m;i+=m) {
//			result+=number.charAt(i);
//		}
		System.out.println(number);

		System.out.println(result);

	}

}
