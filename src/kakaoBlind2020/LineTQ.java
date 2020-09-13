package kakaoBlind2020;

public class LineTQ {
		public static void main(String[] args) {
		int n =10007;
		String target = Integer.toString(n);
		int[] result = new int[2];
		if (target.length()==1) {
			result[0]=0;
			result[1]=n;
		}else {
			int k = 0;
			while(target.length()!=1) {
				
				if (target.length()==2) {
					k++;
					result[1]=(target.charAt(0)-'0')+(target.charAt(1)-'0');					
					result[0]=k;
					target=Integer.toString(result[1]);
					if (target.length()==2) {
						k++;
						result[1]=(target.charAt(0)-'0')+(target.charAt(1)-'0');
						result[0]=k;
						target=Integer.toString(result[1]);
					}
				}else {
					int min = Integer.parseInt(target.substring(0,target.length()-1))
							+Integer.parseInt(target.substring(target.length()-1));
//					System.out.println(min);
					
					for (int i = 0; i < target.length()-1; i++) {
						String fstep = target.substring(target.length()-1-i).substring(0,1);
						if (fstep.equals("0")) {
							
						}else {
							int compare=Integer.parseInt(target.substring(0,target.length()-1-i))
									+Integer.parseInt(target.substring(target.length()-1-i));
							
							if (min>compare) {
								min=compare;
							}
						}
						
																	
					}
//					System.out.println(k+"k");
					k++;
					target=Integer.toString(min);
//					System.out.println(min);
				}
				
				
			}
		}
		
//		System.out.println(result[0]+"lastK");
//		System.out.println(result[1]);
	}

}
