package kakaoBlind2020;

import java.util.ArrayList;
import java.util.List;

public class LineSQ {

	public static void main(String[] args) {
		int[] ball = {11};
		int[] order = {11};
		
		
		List<Integer> orderOrder = new ArrayList<Integer>();
		List<Integer> ballOrder = new ArrayList<Integer>();
		List<Integer> result = new ArrayList<Integer>();
		int[] answer = new int [ball.length];
		
		if (ball.length==1) {
//			return ball;
			System.out.println(ball[0]);
		}else {
			for (int i = 0; i < ball.length; i++) {
				ballOrder.add(ball[i]);
			}
			
			
			int k = 0;					
			orderOrder.add(order[k]);
//			System.out.println(order[k]);
			while(result.size()<ball.length) {
				
				
				for (int i = 0; i <orderOrder.size(); i++) {
					int a = orderOrder.get(i);
					
					if (ballOrder.get(0)==a) {
						
						ballOrder.remove(0);
						result.add(a);						
						orderOrder.remove(i);
						
						break;
					}else if (ballOrder.get(ballOrder.size()-1)==a) {
						
						ballOrder.remove(ballOrder.size()-1);
						result.add(a);						
						orderOrder.remove(i);
						
						break;
					}
				}
				
				if (k<order.length-1) {
					k++;
					orderOrder.add(order[k]);
				}
				
			}
			
			for (int i = 0; i < result.size(); i++) {
				answer[i]=result.get(i);
				System.out.println(result.get(i));
			}
//			return answer;
		}
			
	}

}
