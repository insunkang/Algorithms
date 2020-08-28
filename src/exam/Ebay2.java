package exam;

import java.util.Stack;

public class Ebay2 {
	public static int min;
	public static int min2;
	public static Stack<Integer> stack = new Stack<Integer>();
	public static Stack<Integer> Ccards = new Stack<Integer>();
	
	public static void decompose(int[] cards) {
		
		while(true) {
//			if (min<min2) {
//				break;
//			}
			Stack<Integer> compare = new Stack<Integer>();
			System.out.println(stack.toString());
			
			compare.addAll(stack);
			
			int num = 0;
			while(!compare.isEmpty()) {
				int a= compare.pop();
				for (int i = 0; i < cards.length; i++) {
					if (cards[i]==a) {
						num++;
						System.out.println("yes");
						break;
						
					}
					
					
				}
//				if (cards.contains(compare.pop())) {
//					System.out.println("yes");
//					
//					num++;
//					
//				}
				
				if (num==stack.size()) {
					System.out.println(stack.size());
					min = Math.min(min, stack.size());
				}
				
			}
			
			int temp=stack.pop();
			if (temp!=1) {
				stack.push(temp-1);
				stack.push(1);
			}else {
				int sum=2;
				for (;!stack.isEmpty()&&stack.peek()==1;stack.pop()) 
					sum++;
				if (stack.isEmpty()) 
					break;
				
				int pivot =stack.pop()-1;
				stack.push(pivot);
				
				if (!Ccards.contains(pivot)) {						
					
					
				}else {
					while(sum>pivot) {
						stack.push(pivot);
						sum-=pivot;
					}
					stack.push(sum);
				}
				
				
				
			}
		}
	}
	public static void main(String[] args) {
		int num = 18;
		int[] cards = {1,2,5};
		min=cards.length*cards.length;
		min2=cards.length*cards.length;
		for (int i = 0; i < cards.length; i++) {
			Ccards.add(cards[i]);
		}
		
		stack.push(num);
		decompose(cards);
		System.out.println(min);
	}

}
