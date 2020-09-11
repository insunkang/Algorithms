package programmers;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;



public class DiscController {
	
	
	static class Jobs implements Comparable<Jobs>{
		
		private int time;
		private int value;
		
		Jobs(int time, int value) {
			this.time = time;
			this.value = value;
		}

		@Override
		public int compareTo(Jobs target) {
			return this.value-target.value;
			
		}
		
	}
	

	public static void main(String[] args) {
		int[][] jobs = {{0, 3}, {1, 9}, {2, 6}};
		
		
		
		PriorityQueue<Jobs> pq = new PriorityQueue<>();
		int wholetime=0;
		int answer = 0;
		int index = 0;
		
		Arrays.sort(jobs, new Comparator<int[]>() {

			@Override
			public int compare(int[] o1, int[] o2) {
				
				return o1[0]-o2[0];
			}
		});
		
		
		
		while(true) {
			
			while(index< jobs.length &&jobs[index][0]<=wholetime) {
				pq.add( new Jobs(jobs[index][0],jobs[index][1]));
				index++;
			}
			if (!pq.isEmpty()) {
				Jobs job = pq.poll();
				
				
				wholetime+=job.value;
				answer+=wholetime-job.time;
				
			}else {
				wholetime=jobs[index][0];
			}
			
			if (index==jobs.length&&pq.isEmpty()) {
				break;
			}
		}

		System.out.println(answer/jobs.length);
	}

}
