package kakaoBlind2020;

public class ThirdQ {

	public static void main(String[] args) {
		String[] info = {"java backend junior pizza 150","python frontend senior chicken 210",
				"python frontend senior chicken 150","cpp backend senior pizza 260",
				"java backend junior chicken 80","python backend senior chicken 50"};				
		String[] query = {"java and backend and junior and pizza 100",
				"python and frontend and senior and chicken 200",
				"cpp and - and senior and pizza 250","- and backend and senior and - 150",
				"- and - and - and chicken 100","- and - and - and - 150"};
		
		
		int[] result = new int[query.length];
		
		
		for (int i = 0; i < query.length; i++) {
			String[] queryset = query[i].split(" and ");
			String[] value = queryset[3].split(" ");
			int a = 0;
			for (int j = 0; j < info.length; j++) {
				String[] infoset = info[j].split(" ");
				if (queryset[0].equals("-")||queryset[0].equals(infoset[0])) {
					
					if (queryset[1].equals("-")||queryset[1].equals(infoset[1])) {
						
						if (queryset[2].equals("-")||queryset[2].equals(infoset[2])) {
							
							
							if (value[0].equals("-")||value[0].equals(infoset[3])) {
								
								if (Integer.parseInt(infoset[4])>=Integer.parseInt(value[1])) {
									a++;
								}
							}
						}
					}
				}
				
			}
			result[i]=a;
		}
		
		
		for (int i = 0; i < result.length; i++) {
			System.out.println(result[i]);
		}

	}

}
