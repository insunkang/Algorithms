package exam;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Socar1 {


	public static void main(String[] args)  {
		String[] bakery_schedule = {"09:05 10", "12:20 5","13:25 6","14:24 5"};
		String current_time = "12:05";
		int K = 10;
		int num = bakery_schedule.length;
		SimpleDateFormat sd = new SimpleDateFormat("HH:mm");
		Date currentDate = null;
		try {
			currentDate = sd.parse(current_time);
		} catch (ParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
		String[] schedule = new String[num];
		int[] bakery = new int[num];

		String lastTime =null;
		
		int result = 0;
		for (int i = 0; i < bakery.length; i++) {
			if (result>=K) {
				break;
			}
			String compare = bakery_schedule[i].split(" ")[0];
			SimpleDateFormat yourDateFormat = new SimpleDateFormat("HH:mm");
			Date yourDate = null;
			try {
				yourDate = yourDateFormat.parse(compare);
			} catch (ParseException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			if (yourDate.after(currentDate)||yourDate.equals(currentDate)) {
				result+=Integer.parseInt(bakery_schedule[i].split(" ")[1]);
				lastTime=compare;
				
			}
		}
		
		
		if (result<K) {
			System.out.println(-1);
		}else {
			
			int last = (Integer.parseInt(lastTime.split(":")[0])*60+Integer.parseInt(lastTime.split(":")[1]))
					-(Integer.parseInt(current_time.split(":")[0])*60+Integer.parseInt(current_time.split(":")[1]));
			
		}
	}

}
