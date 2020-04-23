package programmers;

import java.util.HashMap;

public class kakaoOpenChat {

	public static void main(String[] args) {
		String[] chat = { "Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo",
				"Change uid4567 Ryan" };
		String[] word;
		HashMap<String, String> user = new HashMap<String, String>();
		HashMap<Integer, String[]> chatRecord = new HashMap<Integer, String[]>();
		int order = 1;

		for (int i = 0; i < chat.length; i++) {
			word = chat[i].split(" ");

			for (int j = 0; j < word.length; j++) {
				if (word[0].equals("Enter")) {
					user.put(word[1], word[2]);
					String[] a = { word[0], word[1] };
					chatRecord.put(order, a);
					order++;

				} else if (word[0].equals("Leave")) {
					String[] a = { word[0], word[1] };
					chatRecord.put(order, a);
					order++;

				} else if (word[0].equals("Change")) {
					user.put(word[1], word[2]);

				}

			}
			String str="";
			for (int j = 0; j < word.length; j++) {
				str=str+"prodo";
				
				
			}

		}

		System.out.println(user.toString());
		System.out.println(chatRecord.get(1)[0]+","+chatRecord.get(1)[1]);

	}

}
