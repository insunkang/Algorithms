package kakaoBlind2020;

import java.util.Arrays;

public class FirstQ {

	public static void main(String[] args) {
		String new_id = "=.=";
		
		String a = "";
//		for (int i = 0; i < new_id.length(); i++) {  //1st step
//			a=a+Character.toString(new_id.charAt(i)).toLowerCase();
//		}
		new_id=new_id.toLowerCase();
		
		System.out.println(new_id);
		for (int i = 0; i < new_id.length(); i++) { //2nd step
			char chartarget = new_id.charAt(i);
			String strtarget = new_id.substring(i,i+1); 
			
//					Character.toString(new_id.charAt(i));
			if (strtarget.equals("-")||strtarget.equals("_")||strtarget.equals(".")) {
				a=a+strtarget;
			}else if(chartarget>=48&&chartarget<=57){
				a=a+strtarget;
			}else if(chartarget>=97&&chartarget<=122){
				a=a+strtarget;
			}
//			
		}
		
		new_id = a;
		a="";
		System.out.println(new_id);
		boolean[] check = new boolean[new_id.length()];
		Arrays.fill(check, true);
		
			
		for (int i = 0; i < new_id.length(); i++) { //3rd step
			String strtarget = new_id.substring(i,i+1);
//				String strtarget2 = Character.toString(new_id.charAt(i+1));
			if (strtarget.equals(".")) {
				check[i]=false;
			}
		}
		int k = 0;
		for (int i = 0; i < new_id.length(); i++) { //3rd step
			String strtarget = new_id.substring(i,i+1);
			if(k==0) {
				if (check[i]==false) {
					a=a+strtarget;
					k++;
				}else {
					a=a+strtarget;
				}
			}else {
				if (check[i]==false) {
					
					k++;
				}else {
					k=0;
					a=a+strtarget;
				}
			}
				
		}
		new_id = a;
		a="";
		System.out.println(new_id);
		//4th step
		if (new_id.substring(0,1).equals(".")) {
			if (new_id.length()==1) {
				new_id="";
			}else if(new_id.length()==2){
				new_id=new_id.substring(1,3);
			}else {
				new_id=new_id.substring(1,new_id.length());
			}
			
		}
		
		if (new_id.length()!=0&&Character.toString(new_id.charAt(new_id.length()-1)).equals(".")) {
			if (new_id.length()==1) {
				new_id="";
			}else if(new_id.length()==2){
				new_id=new_id.substring(0,2);
			}else {
			
				
				new_id=new_id.substring(0,new_id.length()-1);				
			}

		}
		System.out.println(new_id);
		
		if (new_id.length()==0) { //5th step
			new_id="a"; 
		}
		System.out.println(new_id);
		if (new_id.length()>15) {
			new_id=new_id.substring(0,15);
			for (int i = 0; i < new_id.length(); i++) { //6th+1 step
				String strtarget = new_id.substring(i,i+1);
				if (strtarget.equals(".")) {
					if (i==0||i==new_id.length()-1) {
						
					}else {
						a=a+strtarget;
					}
				}else {
					a=a+strtarget;
				}
			}
			new_id = a;
			a="";
		}
		System.out.println(new_id);
		
		
		if (new_id.length()<=2) { //7th step
			String strtarget = new_id.substring(new_id.length()-1);
			System.out.println(strtarget);
			while(new_id.length()!=3) {
				new_id=new_id+strtarget;
			}
		}
		System.out.println(new_id);
		
		
	}

}
