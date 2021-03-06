package baekjoon;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class DfsExample {
   static int result;
   public static int check(int[][] target, int m, int n) {
      int result =0;
      for (int i = 0; i < m; i++) {
         for (int j = 0; j < n; j++) {
            if (target[i][j]==0) {
               result++;
            }
         }
      }
      return result;
   }
   
   public static void surveil(int[][] target,int[][] origin, int m, int n, Queue<int[]> key, Queue<Integer> value) {      
      int[] left = {-1,0,1,0};
      int[] right = {0,1,0,-1};
      while(!key.isEmpty()) {          
         int[] k = key.poll();		//카메라 좌표
         int v = value.poll();		//카메라 번호
         if (v==1) {		//1번 카메라
        	 for (int l = 0; l < m; l++) {		
                 for (int l2 = 0; l2 < n; l2++) {
                    origin[l][l2]=target[l][l2];
                 }
              }
            for (int j = 0; j < 4; j++) {
            	//target에 origin 복사 필요
               int a =k[0]+left[j];					//1번 방향 감시 시작
               int b =k[1]+right[j];
               while(a>=0&&b>=0&&a<m&&b<n&&target[a][b]!=6) {
                  target[a][b]=8;		//복사된 origin에서 감시 필요
                  a+=left[j];
                  b+=right[j];
                  
               }									//1번 방향 감시 끝
//               for (int fd = 0; fd < m; fd++) {
//                  for (int j2 = 0; j2 < n; j2++) {
//                     if (j2==n-1) {
//                        System.out.println(target[fd][j2]);
//                     }else {
//                        System.out.print(target[fd][j2]);
//                     }
//                  }
//               }
//               System.out.println("---------------------");
//               if (check(target, m, n)<result) {	//최소값 체크는 재귀함수 들어오자마자! 여기서는 필요 없음!
//                  result = check(target, m, n);
//               }
               surveil(target,origin,m,n,key,value);	//1번 카메라 -> 1번 방향 탐색 후 재귀(O)
               System.out.println(1);
               for (int l = 0; l < m; l++) {		//target에 origin복사하는건 맨 마지막이 아니라 for문 맨 앞으로 이동!
                  for (int l2 = 0; l2 < n; l2++) {
                     target[l][l2]=origin[l][l2];
                  }
               }
               
            }
            
         }else if (v==2) {
        	 for (int l = 0; l < m; l++) {		
                 for (int l2 = 0; l2 < n; l2++) {
                    origin[l][l2]=target[l][l2];
                 }
              }
            for (int j = 0; j < 2; j++) {
               int a = k[0]+left[j];
               int b = k[1]+right[j];
               
               while(a>=0&&b>=0&&a<m&&b<n&&target[a][b]!=6) {
                  target[a][b]=8;
                  a+=left[j];
                  b+=right[j];
               }
                              
               int c = k[0]+left[j+2];
               int d = k[1]+right[j+2];
               
               while(c>=0&&d>=0&&c<m&&d<n&&target[c][d]!=6) {
                  target[c][d]=8;
                  c+=left[j+2];
                  d+=right[j+2];
               }
//               for (int fd = 0; fd < m; fd++) {
//                  for (int j2 = 0; j2 < n; j2++) {
//                     if (j2==n-1) {
//                        System.out.println(target[fd][j2]);
//                     }else {
//                        System.out.print(target[fd][j2]);
//                     }
//                  }
//               }System.out.println("---------------------");
               if (check(target, m, n)<result) {
                  result = check(target, m, n);
               }
               System.out.println(2);
               surveil(target,origin,m,n,key,value);
               for (int l = 0; l < m; l++) {
                  for (int l2 = 0; l2 < n; l2++) {
                     target[l][l2]=origin[l][l2];
                  }
               }
               
               
            }
            
         }else if (v==3) {
        	 for (int l = 0; l < m; l++) {		
                 for (int l2 = 0; l2 < n; l2++) {
                    origin[l][l2]=target[l][l2];
                 }
              }
            for (int j = 0; j < 4; j++) {
               int a = k[0]+left[j];
               int b = k[1]+right[j];
               
               while(a>=0&&b>=0&&a<m&&b<n&&target[a][b]!=6) {
                  target[a][b]=8;
                  a+=left[j];
                  b+=right[j];
               }
               
               
               int c = k[0]+left[(j+1)%4];
               int d = k[1]+right[(j+1)%4];
               
               
               
               while(c>=0&&d>=0&&c<m&&d<n&&target[c][d]!=6) {
                  target[c][d]=8;
                  c+=left[(j+1)%4];
                  d+=right[(j+1)%4];
               }
               for (int fd = 0; fd < m; fd++) {
                  for (int j2 = 0; j2 < n; j2++) {
                     if (j2==n-1) {
                        System.out.println(target[fd][j2]);
                     }else {
                        System.out.print(target[fd][j2]);
                     }
                  }
               }System.out.println("---------------------");
               System.out.println(3);
               if (check(target, m, n)<result) {
                  result = check(target, m, n);
               }
               
               surveil(target,origin,m,n,key,value);
               
               for (int l = 0; l < m; l++) {
                  for (int l2 = 0; l2 < n; l2++) {
                     target[l][l2]=origin[l][l2];
                  }
               }
            }
            
         }else if (v==4) {
        	 for (int l = 0; l < m; l++) {		
                 for (int l2 = 0; l2 < n; l2++) {
                    origin[l][l2]=target[l][l2];
                 }
              }
            for (int j = 0; j < 4; j++) {
               int a = k[0]+left[j];
               int b = k[1]+right[j];
               
               while(a>=0&&b>=0&&a<m&&b<n&&target[a][b]!=6) {
                  target[a][b]=8;
                  a+=left[j];
                  b+=right[j];
               }
                              
               int c = k[0]+left[(j+2)%4];
               int d = k[1]+right[(j+2)%4];
               
               while(c>=0&&d>=0&&c<m&&d<n&&target[c][d]!=6) {
                  target[c][d]=8;
                  c+=left[(j+2)%4];
                  d+=right[(j+2)%4];
               }
               
               int e = k[0]+left[(j+3)%4];
               int f = k[1]+right[(j+3)%4];
               
               while(e>=0&&f>=0&&e<m&&f<n&&target[e][f]!=6) {
                  target[e][f]=8;
                  e+=left[(j+3)%4];
                  f+=right[(j+3)%4];
               }
               System.out.println(4);
               for (int fd = 0; fd < m; fd++) {
                  for (int j2 = 0; j2 < n; j2++) {
                     if (j2==n-1) {
                        System.out.println(target[fd][j2]);
                     }else {
                        System.out.print(target[fd][j2]);
                     }
                  }
               }System.out.println("---------------------");
               if (check(target, m, n)<result) {
                  result = check(target, m, n);
               }
               
               surveil(target,origin,m,n,key,value);
               
               for (int l = 0; l < m; l++) {
                  for (int l2 = 0; l2 < n; l2++) {
                     target[l][l2]=origin[l][l2];
                  }
               }
            }
         }else if(v==5){
        	 for (int l = 0; l < m; l++) {		
                 for (int l2 = 0; l2 < n; l2++) {
                    origin[l][l2]=target[l][l2];
                 }
              }
            for (int j = 0; j < 4; j++) {
               int a = k[0]+left[j];
               int b = k[1]+right[j];
               
               while(a>=0&&b>=0&&a<m&&b<n&&target[a][b]!=6) {
                  target[a][b]=8;
                  a+=left[j];
                  b+=right[j];
               }
                  
               
            }
            for (int fd = 0; fd < m; fd++) {
               for (int j2 = 0; j2 < n; j2++) {
                  if (j2==n-1) {
                     System.out.println(target[fd][j2]);
                  }else {
                     System.out.print(target[fd][j2]);
                  }
               }
            }System.out.println("---------------------");
            System.out.println(5);
            if (check(target, m, n)<result) {
               result = check(target, m, n);
            }
            surveil(target,origin,m,n,key,value);
            
         }
         
         if (check(target, m, n)<result) {
            result = check(target, m, n);
         }
      
    if (key.isEmpty()) {
		System.out.println("end");
	}
   }
      
   }
   public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      int m = scan.nextInt();
      int n = scan.nextInt();
      
      int[][] target = new int[m][n];
      int[][] origin = new int[m][n];
      result = m*n;
      Queue<int[]> key = new LinkedList<int[]>();
      Queue<Integer> value = new LinkedList<Integer>();
      
      for (int i = 0; i < m; i++) {
         for (int j = 0; j < n; j++) {
            
            int[] mn = {i,j};
            int put = scan.nextInt();
            target[i][j]= put;
            origin[i][j]= put;
            if (put>0&&put<6) {
               key.add(mn);
               value.add(put);
            }
            
            
         }
      }
      
//      for (int i = 0; i < key.size(); i++) {
//         System.out.println(value.peek());
//      }
      
      
      surveil(target, origin, m, n, key, value);
      
      
      System.out.println(result);
      
      
      
      
      
      
      
      
      
      
      
   }

}