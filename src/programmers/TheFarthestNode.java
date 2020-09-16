package programmers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class TheFarthestNode {
	static class Node{
		int x;
		int depth;
		 Node(int x, int depth) {
			this.x=x;
			this.depth=depth;
		}

	
	}
	static int last;
	public static ArrayList<Integer> cal(int[][] edge, int endnode, boolean[] check, int presentNode, int result) {
		ArrayList<Integer> answer = new ArrayList<Integer>();
		Queue<Node> q = new LinkedList<Node>(); 
		
		for (int i = 0; i < edge.length; i++) {
			if (edge[i][0]==presentNode&&check[edge[i][1]-1]==false) {
//				System.out.println(edge[i][0]+"  "+edge[i][1]);
				q.add(new Node(edge[i][1],result));
			}
			if (edge[i][1]==presentNode&&check[edge[i][0]-1]==false) {
				q.add(new Node(edge[i][0],result));
			}
		}
		
		System.out.println(q.peek().depth);
//		result=result+1;
		
			while (!q.isEmpty()) {
				
				
				Node nextNode = q.poll();
				
				
//				System.out.println(endnode+"  "+nextNode.x);
//				if (nextNode.x==endnode) {
//					last = nextNode.depth;
//					System.out.println("endnode"+endnode+"depth"+last);
//					return;
//				}
		
					
					for (int i = 0; i < edge.length; i++) {
						if (edge[i][0]==nextNode.x&&check[edge[i][1]-1]==false) {
							check[edge[i][1]-1]=true;
							q.add(new Node(edge[i][1],nextNode.depth+1));
							
//							System.out.println(edge[i][1]+"  "+edge[i][0]);
						}
						if (edge[i][1]==nextNode.x&&check[edge[i][0]-1]==false) {
							check[edge[i][0]-1]=true;
							q.add(new Node(edge[i][0],nextNode.depth+1));
							
//							System.out.println(edge[i][0]+"  "+edge[i][1]);
						}
					}
		
				
			}
			return answer;
		
		
		
		
	}

	public static void main(String[] args) {
		int n =6;
		int[][] edge= {{3, 6}, {4, 3}, {3, 2}, {1, 3}, {1, 2}, {2, 4}, {5, 2}};
		
		
		int max = 0;
		int answer = 0;
		
//		
//		for (int i = 2; i <= n; i++) {
//			boolean[] check = new boolean[n];
////			Arrays.fill(check, false);
//			
//			check[0]=true;
//			
//			last=1;
//			
//			cal(edge,i,check,1,1);
//			
//			if (last>max) {
//				max = last;
//				answer = 1;
//				
//			}else if (last==max) {
//				answer=answer+1;
////				System.out.println(i+"i");
//			}
//		}
//		System.out.println(max+"max");
		boolean[] check = new boolean[n+1];
		ArrayList<ArrayList<Integer>> target = new ArrayList<ArrayList<Integer>>();
		int[] result = new int[n+1];
		for (int i = 0; i < n+1; i++) {
			target.add(new ArrayList<Integer>());
		}
		
		for (int i = 0; i < edge.length; i++) {
			int a = edge[i][0];
			int b = edge[i][1];
			
			target.get(a).add(b);
			target.get(b).add(a);
			
		}
		
		Queue<Integer> q = new LinkedList<Integer>();
		
		q.add(1);
		
		check[0]=check[1]=true;
		int now ;
		while(!q.isEmpty()) {
			now = q.poll();
			
			for(int v:target.get(now)) {
				if (check[v]==false) {
					result[v]=result[now]+1;
					check[v]=true;
					q.add(v);
				}
			}
			
			
		}
		System.out.println(Arrays.toString(result));
		for (int i = 0; i < result.length; i++) {
			if (max<result[i]) {
				max=result[i];
				answer =1;
			}else if (max==result[i]) {
				answer++;
			}
		}
		
		System.out.println(max);
		System.out.println(answer+"answer");
	}

}
