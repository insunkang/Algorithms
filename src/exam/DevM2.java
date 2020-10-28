package exam;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class DevM2 {

	public static void main(String[] args) throws ParseException {
		String P = "PM 01:00:00";
		int N = 10;
//		int H = N/3600;
//		N=N%3600;
//		int M = N/60;
//		N=N%60;
//		int S = N;
	
		String a ="";
		String b =Integer.toString( Integer.parseInt(P.split(" ")[1].split(":")[1]));
		String c =Integer.toString( Integer.parseInt(P.split(" ")[1].split(":")[2]));
		if (P.split(" ")[0].equals("PM")) {
			a= Integer.toString(Integer.parseInt(P.split(" ")[1].split(":")[0])+12);
		}else {
			a = Integer.toString(Integer.parseInt(P.split(" ")[1].split(":")[0])) ;
			
		}
		
//		int a =0;
//		int b = Integer.parseInt(P.split(" ")[1].split(":")[1])+M;
//		int c = Integer.parseInt(P.split(" ")[1].split(":")[2])+S;
//		if (P.split(" ")[0].equals("PM")) {
//			a=Integer.parseInt(P.split(" ")[1].split(":")[0])+12+H;
//		}else {
//			a = Integer.parseInt(P.split(" ")[1].split(":")[0])+H;
//			
//		}
//		if (c>=60) {
//			b=b+c/60;
//			c=c%60;
//		}
//		if(b>=60) {
//			a=a+b/60;
//			b=b%60;
//		}
//		if (a>=24) {
//			a=a%24;
//		}
//		
//		String sa= Integer.toString(a);
//		if (sa.length()==1) {
//			sa="0"+sa;
//		}
//		String sb= Integer.toString(b);
//		if (sb.length()==1) {
//			sb="0"+sb;
//		}
//		String sc= Integer.toString(c);
//		if (sc.length()==1) {
//			sc="0"+sc;
//		}
		
		if (b.length()==1) {
			b="0"+b;
		}
		if (c.length()==1) {
			c="0"+c;
		}
		P = a+":"+b+":"+c;
		System.out.println(P);
//		if (P.split(" ")[0].equals("PM")) {
//			P=Integer.toString(Integer.parseInt(P.split(" ")[1].split(":")[0])+12+H)+":"+
//					b+":"+c;
//		}else {
//			String a = Integer.toString(Integer.parseInt(P.split(" ")[1].split(":")[0])+H);
//			if (a.length()==1) {
//				a="0"+a;
//			}
//			P=a+":"+b+":"+c;
//		}
//		P = sa+":"+sb+":"+sc;
		
		SimpleDateFormat day1 = new SimpleDateFormat("HH:mm:ss");
		Date d1 = day1.parse(P);
		long sec = d1.getTime()/1000;
		sec=sec+N;
		System.out.println(sec);
		long f1 = sec/3600;
		f1=f1/24;
		sec=sec%3600;
		long f2 = sec/60;
		sec=sec%60;
		long f3 = sec;
		
		String sf1 ="";
		String sf2 ="";
		String sf3 ="";
		
		if (Long.toString(f1).length()==1) {
			sf1="0"+Long.toString(f1);
		}else {
			sf1=Long.toString(f1);
		}
		if (Long.toString(f2).length()==1) {
			sf2="0"+Long.toString(f2);
		}else {
			sf2=Long.toString(f2);
		}
		if (Long.toString(f3).length()==1) {
			sf3="0"+Long.toString(f3);
		}else {
			sf3=Long.toString(f3);
		}
		P=sf1+":"+sf2+":"+sf3;
		System.out.println(P);
	}

}
