package programmers;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class TheFarthestNode2 {
	 static class ListGraph {
	    private ArrayList<ArrayList<Integer>> listGraph;
	 
	    // �׷��� �ʱ�ȭ
	     public ListGraph(int initSize) {
	        this.listGraph = new ArrayList<ArrayList<Integer>>(); // �׷��� ����
	        
	        // �׷��� �ʱ�ȭ
	        // put(int x, int y) ���� �ԷµǴ� ������ ���� 0 �̻��� �����̳�
	        // ArrayList�� index�� 0 ���� �����̹Ƿ� 
	        // ArrayIndexOutOfBoundsException ������ ���� 
	        // ������ ��� ��������Ʈ�� size�� 1�� ���Ͽ� �ʱ�ȭ����
	        // ex) initSize = 3
	        // graph[0]
	        // graph[1] -> 2 -> 3
	        // graph[2] -> 1 -> 3 -> 4
	        // graph[3] -> 1 -> 2 -> 4 -> 5
	        for(int i=0; i<initSize+1; i++) {
	            listGraph.add(new ArrayList<Integer>());
	        }
	    }
	 
	    // �׷��� return
	    public ArrayList<ArrayList<Integer>> getGraph() {
	        return this.listGraph;
	    }
	 
	    // �׷����� Ư�� ��� return
	    public ArrayList<Integer> getNode(int i) {
	        return this.listGraph.get(i);
	    }
	 
	    // �׷��� �߰� (�����)
	    public void put(int x, int y) {
	        listGraph.get(x).add(y);
	        listGraph.get(y).add(x);
	    }
	 
	    // �׷��� �߰� (�ܹ���)
	    public void putSingle(int x, int y) {
	        listGraph.get(x).add(y);
	    }
	    
	    // �׷��� ��� (��������Ʈ)
	    public void printGraphToAdjList() {
	        for(int i=1; i<listGraph.size(); i++) {
	            System.out.print("���� " + i + "�� ��������Ʈ");
	            
	            for(int j=0; j<listGraph.get(i).size(); j++) {
	                System.out.print(" -> " + listGraph.get(i).get(j));
	            }
	            System.out.println();
	        }
	    }
	}


	
	


	
	public static void main(String[] args) {
		  int n = 6;
	        ListGraph adjList = new ListGraph(n);
	        int[][] edge= {{3, 6}, {4, 3}, {3, 2}, {1, 3}, {1, 2}, {2, 4}, {5, 2}};
	        
	        for (int i = 0; i < edge.length; i++) {
				adjList.put(edge[i][0], edge[i][1]);
			}
	        List<Integer> result = new ArrayList<Integer>();
	        
	        Queue<Integer> q = new LinkedList<Integer>();
//	        
//	        for(int j=0; j<adjList.getNode(1).size(); j++) {
//	        	
//               q.add(adjList.getNode(1).get(j));
//            }
	        
	        
	        
	        for (int i = 2; i <= n; i++) {
	        	int depth = 1;
	        	List<Integer> k=  new ArrayList<Integer>();
	        	for(int j=0; j<adjList.getNode(1).size(); j++) {
		        	
	                q.add(adjList.getNode(1).get(j));
	                k.add(1);
	             }
	        	
	        	
	        	while(!q.isEmpty()) {
	        		int a = q.poll();
	        		if (a==i) {
	        			System.out.println(depth);
						result.add(depth);
						break;
								
					}
	        		for(int j=0; j<adjList.getNode(a).size(); j++) {
			        	if (!k.contains(adjList.getNode(a).get(j))) {
			        		q.add(adjList.getNode(a).get(j));
			        		k.add(adjList.getNode(a).get(j));
			                depth++;
						}
		                
		             }
	        	}
	        	
	        	
			}
	        
	        
	      
	        System.out.println(result);
	        

	

	}

}

