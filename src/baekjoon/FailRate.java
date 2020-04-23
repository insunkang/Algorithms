
package baekjoon;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

public class FailRate {

 public static void main(String[] args) {
  int N = 5;
  int[] stages = {2,1,2,6,2,4,3,3};
  HashMap<Integer, Float> map = new HashMap<Integer, Float>();
  float[] FailRate = new float[N];
  
  Queue Rate = new LinkedList();
  for(int j=1; j<=N;j++) {
   int getPeople = 0 ;
   int XclearPeople = 0 ;
   
   
   for(int i=0;i<stages.length;i++) {
    if(stages[i]==j) {
     XclearPeople=XclearPeople+1;
    }
    if (stages[i]>=j) {
     getPeople=getPeople+1;
    }
    
   }
   
   FailRate[j-1]= ((float)XclearPeople/(float)getPeople)*100;
   float a =((float)XclearPeople/(float)getPeople)*100;
   System.out.println(FailRate[j-1]);
   map.put(j, a);
  }
  System.out.println(map);

	  
  
  
  //--------------------------------------------
	   Set<Integer> a = map.keySet();
	   
  		float max = 0; 
	  for(int i=1;i<FailRate.length;i++) {
	   if(FailRate[i]>max) {
	    max = FailRate[i];
	   }
	  }
	  
	  for(int i=0;i<FailRate.length;i++) {
	   if(max==FailRate[i]) {
	    Rate.add(i+1);
	   }
	  }
	  System.out.println(Rate);
	  System.out.println(max);
	  
	  for(int i=0; i<map.size();i++) {
		  if(map.get(i+1)==max) {
			  map.remove(i+1);
		  }
		  
	  }
	  System.out.println(map);
	  System.out.println(map.keySet());
	  
	  
//	  int[] index = new int[map.size()];
//		 for(int i =map.size(); i>0;i--) {	
//		  index[i-1] = i;
//		  
//		 }
//	  
	  
	 
  }
 
  


}
