
package baekjoon;

import java.util.Scanner;

public class Robot {
 //왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
 //왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
 // 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
 // 네 방향 모두 청소가 이미 되어 있거나, 벽이면서 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에 작동 멈춤
 //0 -> 3 -> 2-> 1-> 0->3-> 이순서

	
 public static int cleaning(int[][] can,int x, int y, int news) {
  int room=1;
  int[] back = {2,3,0,1}; 
  can[x][y]=-1; //청소 
  int pandan = 0;  
  int[]	third = {-1,0,1,0};
  int[] fourth = {0,1,0,-1};
  
		  for (int i = 0; i < 4; i++) {
		   int na = x+third[i];
		   int nb = y+fourth[i];
		   if (can[na][nb]==0) {
		    pandan++;    
		   }
		  } 
  if (pandan==0) {
   if (can[x+third[back[news]]][y+fourth[back[news]]]==1) {
    return room;   
   }else {
	   room=room+cleaning(can,x+third[back[news]],y+fourth[back[news]],news)-1;
   }
  }else {
	  if(news==0) {
		  int[] asd = {3,2,1,0};
		  for (int i = 0; i < asd.length; i++) {
			  int nasd = x+third[asd[i]];
			  int nbsd = y+fourth[asd[i]];			  
			if(can[nasd][nbsd]==0) {				
				room=room+cleaning(can,nasd,nbsd,asd[i]);				
				break;
			}
		}		  
	  }else if(news==3) {
		  int[] asd = {2,1,0,3};
		  for (int i = 0; i < asd.length; i++) {
			  int nasd = x+third[asd[i]];
			  int nbsd = y+fourth[asd[i]];
			if(can[nasd][nbsd]==0) {				
				room=room+cleaning(can,nasd,nbsd,asd[i]);				
				break;
			}
		}		  
	  }else if(news==2) {
		  int[] asd = {1,0,3,2};
		  for (int i = 0; i < asd.length; i++) {
			  int nasd = x+third[asd[i]];
			  int nbsd = y+fourth[asd[i]];
			if(can[nasd][nbsd]==0) {				
				room=room+cleaning(can,nasd,nbsd,asd[i]);				
				break;
			}
		}		  
	  }else  {
		  int[] asd = {0,3,2,1};
		  for (int i = 0; i < asd.length; i++) {
			  int nasd = x+third[asd[i]];
			  int nbsd = y+fourth[asd[i]];
			if(can[nasd][nbsd]==0) {				
				room=room+cleaning(can,nasd,nbsd,asd[i]);				
				break;
			}
		}		  
	  }
  }

  return room;
 } 
 public static void main(String[] args) {
  Scanner scan = new Scanner(System.in);
  int a = scan.nextInt();  //
  int b = scan.nextInt();
  
  int x = scan.nextInt(); // 위치 열
  int y = scan.nextInt(); // 위치 행
  
  int news = scan.nextInt(); //방향
  
  int can[][] = new int[a][b];
  
  for (int i = 0; i < a; i++) {
   for (int j = 0; j < b; j++) {
    can[i][j]= scan.nextInt();  
   }
  }
  
  //0 -> 3 -> 2-> 1-> 0->3-> 이순서
  
   int answer = cleaning(can,x,y,news);
  
  
  System.out.println(answer);

 }

}
