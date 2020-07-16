package programmers;

public class TruckPassingBridge {
	
	public static int arrSum(int[] arr) {
		int result=0;
		for (int i = 0; i < arr.length; i++) {
			result +=arr[i];
		}
		return result;
	}
	public static int[] moveForward(int[] arr) {
		
		for (int i = 0; i < arr.length-1; i++) {
			arr[i]=arr[i+1];
		}
		arr[arr.length-1]=0;
		return arr;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int bridge_length = 100;
		int weight = 100;
		int[] truck_weights = {10};
		
		int[] bridge_status = new int[bridge_length];
		
		int i = 0;
		int result=1;
		while(i<truck_weights.length) {
//			System.out.println(arrSum(bridge_status));
			if (arrSum(bridge_status)==0&&i==0) { //맨 처음
				
				bridge_status[bridge_length-1]=truck_weights[i];
				i++;
			}else if(arrSum(bridge_status)+truck_weights[i]<=weight){
				
				bridge_status[bridge_length-1]=truck_weights[i];
				i++;
			}else {
				
			}
			result++;
			moveForward(bridge_status);
			
						
		}
		
		while(arrSum(bridge_status)!=0) {
//			System.out.println(arrSum(bridge_status));
			result++;
			moveForward(bridge_status);
		}
		
		System.out.println(result);
	}

}
