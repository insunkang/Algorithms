package kakaoBlind2020;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

public class SecondQ {
	
	 static void reculsion(List<String> arr, List<String> result, int index, int n, int r,ArrayList<List<String>> answer) {

		if (r == 0) {
			List<String> addd = new ArrayList<String>();
			for (int i = 0; i < result.size(); i++) {
				addd.add(result.get(i));
			}
			answer.add(addd);
//			System.out.println(result.toString());
			return;
		}

		for (int i = index; i < n; i++) {

			result.add(arr.get(i));
			reculsion(arr, result, i + 1, n, r - 1,answer);
			result.remove(result.size() - 1);
		}
	}	

	public static void main(String[] args) {
		String[] orders = {"ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"};
		
		int[] course = {2,3,4};
		
		List<String> targetCourse = new ArrayList<String>();
		
		for (int i = 0; i < orders.length; i++) {
			for (int j = 0; j < orders[i].length(); j++) {
				if (targetCourse.contains(Character.toString(orders[i].charAt(j)))) {
					
				}else {
					targetCourse.add(Character.toString(orders[i].charAt(j)));
				}
			}
		}
		System.out.println(targetCourse);
		
		HashMap<List<String>, Integer> orderset = new HashMap<List<String>, Integer>();
		
		for (int i = 0; i < course.length; i++) {
			int n = course[i];
			
			List<String> result = new ArrayList<String>();
			ArrayList<List<String>> answer = new ArrayList<List<String>>();
			reculsion(targetCourse,result,0,targetCourse.size(),n,answer);
			
			for (int j = 0; j < answer.size(); j++) {
				int dfs = 0;
				List<String> ds = new ArrayList<String>();
				for (int k = 0; k < answer.get(j).size(); k++) {
					ds.add(answer.get(j).get(k));
				}
				
				for (int j2 = 0; j2 < orders.length; j2++) {
					int ok = 0;
					for (int k = 0; k < ds.size(); k++) {
						if (orders[j2].contains(ds.get(k))) {
							ok++;
						}
					}
					if (ok==ds.size()) {
						dfs++;
					}
					
				}
				if(dfs>=2) {
					orderset.put(answer.get(j), dfs);
				}
			}
//			System.out.println(answer.toString());
			
		}
		ArrayList<String> last = new ArrayList<String>();
		for (int i = 0; i < orders.length; i++) {
			List<String> compare = new ArrayList<String>();
			for (int j = 0; j < orders[i].length(); j++) {
				compare.add(Character.toString(orders[i].charAt(j)));
			}
			for (int j = 0; j < orderset.size(); j++) {
				
				if (orderset.containsKey(compare)) {
					if (last.contains(orders[i])) {
						
					}else {
						last.add(orders[i]);
					}
					
				}
			}
		}
		Collections.sort(last);
		String[] lastanswer = new String[last.size()];
		for (int i = 0; i < last.size(); i++) {
			lastanswer[i]=last.get(i);
		}
		System.out.println(last);
//				입력값 〉	["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]
//				기댓값 〉	["ACD", "AD", "ADE", "CD", "XYZ"]
//				실행 결과 〉	실행한 결괏값 [ 'AB', 'ACD', 'ADE', 'CD', 'XYZ' ]이(가) 기댓값 [ 'ACD', 'AD', 'ADE', 'CD', 'XYZ' ]와(과) 다릅니다.
//				출력 〉	[A, B, C, D, E, X, Y, Z]
		
//				테스트 3
//				입력값 〉	["XYZ", "XWY", "WXA"], [2, 3, 4]
//				기댓값 〉	["WX", "XY"]
//				실행 결과 〉	실행한 결괏값 []이(가) 기댓값 [ 'WX', 'XY' ]와(과) 다릅니다.
//				출력 〉	[X, Y, Z, W, A]
	}

}
