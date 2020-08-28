package exam;

public class Ebay1 {

	public static void main(String[] args) {
		int N =2;
		int[][] simulation_data = {{0, 3}, {2, 5}, {4, 2}, {5, 3}};
		int[] target = new int[N];
		for (int i = 0; i < target.length; i++) {
			target[i]=0;
		}
		int result = 0;
		
		int sec = 0;
		int client=0;
		while(true) {
			if (simulation_data[client][0]==sec) {
				
				for (int i = 0; i < target.length; i++) {
					if (target[i]==0) {
						target[i]=simulation_data[client][1];
						client++;
						break;
						
					}else if (i==target.length-1&&target[i]!=0) {
						result++;
					}
				}
				
				
			}
			
			for (int j = 0; j < target.length; j++) {
				if (target[j]>0) {
					target[j]--;
				}
				
			}
			for (int i = 0; i < target.length; i++) {
				System.out.println(sec);
				System.out.println(target[0]+""+target[1]);
			}
			
			
			sec++;
			if (client-1==simulation_data.length) {
				break;
			}
		}
		
		System.out.println(result);

	}

}
