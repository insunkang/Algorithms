package exam;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Coupang2 {

	public static void main(String[] args) throws ParseException {
		String[] customers = {"10/01 23:20:25 30","10/01 23:25:20 26"};
		String a = "10/01 23:20:25";
		String b = "10/01 23:20:25";
		SimpleDateFormat day1 = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
		a="2019/"+a;
		b="2019/"+b;
		Date a1 =  day1.parse(a);
		Date b1 =  day1.parse(a);
//		System.out.println(a1);
		
//		String from = "04/08 10:10:10";
//		from = "2019/"+from;
//		SimpleDateFormat transFormat = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
//
//		Date to = transFormat.parse(from);

		SimpleDateFormat f = new SimpleDateFormat("yyyy/MM/dd HH:mm:ss");
		
//		System.out.println(sec);

		int[] customerTime = new int[customers.length];
		for (int i = 0; i < customers.length; i++) {
			customerTime[i] = Integer.parseInt(customers[i].split(" ")[2]);
		}
		
		
		long[] customerdate = new long[customers.length];
		customerdate[0] = 0;
		for (int i = 1; i < customerdate.length; i++) {
			Date d1 = f.parse("2019/"+customers[i].split(" ")[0]+" "+customers[i].split(" ")[1]);
			Date d2 = f.parse("2019/"+customers[i-1].split(" ")[0]+" "+customers[i-1].split(" ")[1]);
			long diff = d1.getTime() - d2.getTime();
			long sec = diff / 1000;
			
//			System.out.println(sec);
			customerdate[i]=sec;
		}
		int time = 0;
		while(time!=customerdate[customerdate.length]) {
			
			
			time++;
		}
		
	}

}
