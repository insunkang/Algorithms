package programmers;

import java.util.ArrayList;
import java.util.HashMap;

public class TheSongJustHeard {

	public static void main(String[] args) {
		String m ="ABC";
		String[] musicinfos = {"12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"};
		ArrayList<Integer> key = new ArrayList<Integer>();
		
		HashMap<Integer, String> check = new HashMap<Integer, String>();
		String answer = "`(None)'";
		for (int i = 0; i < musicinfos.length; i++) {
			String[] target = musicinfos[i].split(",");
			
			int h = Integer.parseInt(target[1].split(":")[0])-Integer.parseInt(target[0].split(":")[0]);
			int mi = Integer.parseInt(target[1].split(":")[1])-Integer.parseInt(target[0].split(":")[1]);
			int time = h*60+mi;
			
			String compare = target[3] ;
			
			if (time>target[3].length()) {
				for (int j = 0; j < time/target[3].length(); j++) {
					compare=compare+compare;
					if (compare.length()>=m.length()*3) {
						break;
					}
				}
				compare=compare+target[3].substring(0,time%target[3].length());
				
			}else if(time<target[3].length()) {
				compare = target[3].substring(0,time);
			}
			String compare2 = m+"#";
			if (compare.contains(m)&&!compare.contains(compare2)) {
				System.out.println(compare);
				System.out.println("yes");
				if (key.contains(time)) {
					
				}else {
					key.add(time);
					check.put(time, target[2]);
				}
				

			}
			
			
			
		}
		
		if (key.size()>0) {
			int max = 0;
			for (int i = 0; i < key.size(); i++) {
				if (key.get(i)>max) {
					max = key.get(i);
				}
				
			}
			answer = check.get(max);
			System.out.println(answer);
		}else {
			System.out.println(answer);
		}
		
	}

}
