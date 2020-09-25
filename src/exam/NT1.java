package exam;

public class NT1 {

	public static void main(String[] args) {
		 int[][] flowers = {{2, 5}, {3, 12}, {10, 11}};
//		  int day = 0;
//          Arrays.sort(flowers, (o1, o2) -> {
//              if(o1[0] == o2[0]) {
//                  return Integer.compare(o1[1], o2[1]);
//              }else {
//                  return Integer.compare(o1[0], o2[0]);
//              }
//          });
          int day2=0;
          for (int i = 0; i < flowers.length; i++) {
              if(flowers[i][0] > day2) {
                  day2 = flowers[i][0];
              }
              if(flowers[i][1] > day2) {
                  day2 = flowers[i][1];
              }
          }
          System.out.println(day2);

//          day = flowers[flowers.length - 1][flowers[0].length - 1];
//          System.out.println(day);

	}

}
