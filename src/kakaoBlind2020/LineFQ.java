package kakaoBlind2020;

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class LineFQ {

	public static void main(String[] args) {
		int[][] boxes= {{1, 2},{2, 3},{1, 3}};
		
		
		List<String> firstBox = new ArrayList<String>();
		List<String> secondBox = new ArrayList<String>();
		
		Queue<String> box = new LinkedList<String>();
		for (int i = 0; i < boxes.length; i++) {
			firstBox.add(Integer.toString(boxes[i][0]));
			firstBox.add(Integer.toString(boxes[i][1]));
			
			
		}	
		
		for (int i = 0; i < firstBox.size(); i++) {
			box.add(firstBox.get(i));
		}
		Collections.sort(firstBox);
//		System.out.println(firstBox);
		int k = 0;
		
		while(!box.isEmpty()) {
			String a = box.poll();
			if (secondBox.contains(a)) {
				secondBox.remove(a);
				k++;
			}else {
				secondBox.add(a);
			}
		}
//		while(!secondBox.isEmpty()) {
//			int a = secondBox.poll();
//			if (firstBox.contains(a)) {
//				k++;
//			}
//		}
//		
		System.out.println(boxes.length-k);

	}

}
