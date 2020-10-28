package exam;

import java.util.ArrayList;
import java.util.Collections;

public class Bitmango2 {

	public static void main(String[] args) {
		int k = 3;
		String letters = "zbgaj";
		String[] abc = letters.split("");
		ArrayList<Integer> let = new ArrayList<Integer>();
		String result="";
		for (int i = 0; i < abc.length; i++) {
			let.add((int)letters.charAt(i));
			
		}
		
		Collections.sort(let);
		for (int i = 0; i < let.size(); i++) {
			System.out.println(let.get(i));
		}
		int check = 0;
		
		ArrayList<Integer> last = new ArrayList<Integer>();
		for (int i = let.size()-1; i >= 0; i--) {
			
			last.add(let.get(i));
			
			check ++;
			if (check==k) {
				break;
			}
		}
		System.out.println("----------------");
		for (int i = 0; i < last.size(); i++) {
			System.out.println(last.get(i));
		}
		let.clear();
		
		for (int i = 0; i < abc.length; i++) {
			let.add((int)letters.charAt(i));
			
		}
		
		for (int i = 0; i < let.size(); i++) {
			if(last.contains(let.get(i))) {
				System.out.println(i);
				int a = let.get(i);
				char b = (char) a;
				String c = Character.toString(b);
				result+= c;
				last.remove(let.get(i));
			}
		}
		System.out.println(result);
	}

}
