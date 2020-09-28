package exam;

import java.util.ArrayList;

public class The11stQ {

	public static void main(String[] args) {
		String S = "baaaa";
		ArrayList<String> targetA = new ArrayList<String>();
		ArrayList<String> target = new ArrayList<String>();
		String a ="";
		int result = 0;
		for (int i = 0; i < S.length(); i++) {
			
			String subs=Character.toString(S.charAt(i));
			if (subs.equals("a")) {
				a=a+subs;
				if (i==S.length()-1) {
					targetA.add(a);
				}
			}else if(!a.equals("")){
				targetA.add(a);
				target.add(subs);
				a="";
			}else {
				target.add(subs);
			}
			
			
		}
		
		for (int i = 0; i < targetA.size(); i++) {
			if (targetA.get(i).length()==1) {
				result++;
			}else if (targetA.get(i).length()>=3) {
				System.out.println(-1);
			}
		}
		result=result+(target.size()+1-targetA.size())*2;
		
		System.out.println(target.toString());
		System.out.println(targetA.toString());
		System.out.println(result);
	}

}
