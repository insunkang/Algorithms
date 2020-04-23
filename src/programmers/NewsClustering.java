package programmers;
import java.util.HashMap;
public class NewsClustering {
	public static boolean cal(String some) {
		String bi = " ";
		String[] calcal = some.split("");
		int csc = 0;
		for (int i = 0; i < calcal.length; i++) {
			if(calcal[i].equals(bi)) {
				csc++;
			}
		}
		return csc==calcal.length;
	}
	public static void main(String[] args) {
		String A = "E=M*C^2";
		String B = "e=m*c^2";
		String a = A.toLowerCase();
		String b = B.toLowerCase();
		HashMap<Integer, String> aMap = new HashMap<Integer, String>();
		HashMap<Integer, String> bMap = new HashMap<Integer, String>();
		char[] test = new char[2];
		int key1 = 0;
		int key2 = 0;
		int good = 65536;
		if(a.equals(b)) {
			System.out.println(good);
		}
		else {
		for (int i = 0; i < A.length() - 1; i++) {
				test[0] = a.charAt(i);
				test[1] = a.charAt(i + 1);
				if ((int) test[0] >= 97 && (int) test[0] <= 122) {
					if ((int) test[1] >= 97 && (int) test[1] <= 122) {
						aMap.put(key1, a.substring(i, i + 2));
						key1++;
					}
				}
			}
			for (int i = 0; i < B.split("").length - 1; i++) {
				test[0] = b.charAt(i);
				test[1] = b.charAt(i + 1);
				if ((int) test[0] >= 97 && (int) test[0] <= 122) {
					if ((int) test[1] >= 97 && (int) test[1] <= 122) {
						bMap.put(key2, b.substring(i, i + 2));
						key2++;
					}
				}
			}
			int hap = 0;
			for (int i = 0; i < aMap.size(); i++) {
				for (int j = 0; j < bMap.size(); j++) {
					if (aMap.get(i).equals(bMap.get(j))) {
						aMap.put(i, "0");
						bMap.put(j, "0");
					}
				}
			}
			for (int i = 0; i < aMap.size(); i++) {
				if (aMap.get(i).equals("0")) {
					hap++;
				}
			}

				
			if (bMap.size() == aMap.size() && aMap.size() == hap) {
					
				if (aMap.size() == 0 || bMap.size() == 0) {
					if(cal(A)&&cal(B)) {
						System.out.println(good);
					}else {
						System.out.println(0);	
					}										
				} else {
					System.out.println(good);
				}
			} 
			
			
			else {
				int mother = aMap.size() + bMap.size() - hap;
				double result = (double)((good * hap )/ (mother));
				System.out.println(result);
			}
		}
		
		}
		
		
	}

