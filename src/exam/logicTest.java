package exam;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

public class logicTest {
   static int ans = 0;

   public static void main(String[] args) {
      int r = 3;
      int[][] delivery = { { 1, 5 }, { 8, 3 }, { 4, 2 }, { 2, 3 }, { 3, 1 }, { 3, 2 }, { 4, 2 }, { 5, 2 }, { 4, 1 } };
      System.out.println(solution(r, delivery));
      
      
      int r2 = 4;
      int[][] delivery2 = {{1,10},{8,1},{8,1},{3,100},{8,1},{8,1},{8,1},{8,1},{8,1},{8,1},{8,1},{8,1},{9,100},{8,1},{8,1},{8,1}};
      System.out.println(solution(r2, delivery2));
      
   }

   public static int solution(int r, int[][] delivery) {
      int limit = 0;
      HashMap<Integer,DeliveryMap> hashMap = new HashMap<>();
      Stack<String> st1 = new Stack<>();
      Stack<String> st2 = new Stack<>();
      for(int i=0; i<r; i++) {
         for(int j=0; j<r; j++) {
            hashMap.put(i*r+j,new DeliveryMap(j,i,delivery[(i*r)+j][0],delivery[(i*r)+j][1]));
            limit = Math.max(limit, delivery[(i*r)+j][0]);
         }
      }
      //System.out.println(hashMap);
      st1.add("0");
      for(int i=1; i<= limit; i++) {
         while(!st1.empty()) {
            String pop = st1.pop();
            String[] popArr = pop.split(",");
            int one = Integer.parseInt(popArr[popArr.length-1]);
            int x = one%r;
            int y = one/r;
            if(y+1<r) {
               st2.add(pop+","+((y+1)*r + x));
            }
            if(y-1>=0) {
               st2.add(pop+","+((y-1)*r + x));
            }
            if(x+1<r) {
               st2.add(pop+","+(y*r+(x+1)));
            }
            if(x-1>=0) {
               st2.add(pop+","+((y*r)+(x-1)));
            }
         }
         st1 = (Stack<String>) st2.clone();
         st2.clear();
      }
      //System.out.println(st1);
      int answer = 0;
      Set<Integer> set = new HashSet<>();
      while(!st1.empty()) {
         String[] road = st1.peek().split(",");
         String test = st1.pop();
         
         int temp = 0;
         for(int i=0; i<road.length;i++) {
            if(!set.contains(Integer.parseInt(road[i]))) {
               if(hashMap.get(Integer.parseInt(road[i])).limit>=i) {
                  temp += hashMap.get(Integer.parseInt(road[i])).tip;
               }
               set.add(Integer.parseInt(road[i]));
            } else {
               set.add(Integer.parseInt(road[i]));
            }
            
         }
         
         answer = Math.max(answer, temp);
         //System.out.println(test);
         set.clear();
      }
      
      return answer;
   }
   
}

class DeliveryMap {
   int x;
   int y;
   int limit;
   int tip;
   public DeliveryMap(int x, int y, int limit, int tip) {
      this.x = x;
      this.y = y;
      this.limit = limit;
      this.tip = tip;
   }
   
   @Override
   public String toString() {
      return "map [x=" + x + ", y=" + y + ", limit=" + limit + ", tip=" + tip + "]";
   }
}
