package monthlyCodingChallenge;

public class Oct1 {

	public static void main(String[] args) {
		int n = 125;
		int answer = 0;
        String test = "";
        while(true){
            if(n<3){
                test=test+Integer.toString(n);
                break;
            }else{
                test=test+Integer.toString(n%3);
                n=n/3;    
            }
            
        }
        String test2 = "";
        for (int i = test.length()-1; i >=0; i--) {
			test2 = test2+test.charAt(i);
		}
//        System.out.println(test2);
//        int check =  Integer.parseInt(test);
        System.out.println(test2);
        for(int i = 0; i<test2.length();i++){
        		int a = test2.charAt(i)-'0';
        		int b = (int)(Math.pow(3, i));
        		answer= answer+(a)*(b);
//        		System.out.println(a+"a");
//        		System.out.println(i+"i");
//        		System.out.println(b+"b");
//        		
//        		System.out.println(answer+"answer");
//        		
//        		System.out.println("");
//        		System.out.println(test2.charAt(i)+"asd2");
        		
			
            
            
        }
        System.out.println(answer);
	}

}
