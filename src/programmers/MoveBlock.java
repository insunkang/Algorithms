package programmers;

public class MoveBlock {
	static int answer;
	
	public static void move(int[][] target, int m, int[] left, int[] right, int check) {
		if(check>=answer) {
			return;
		}
		if(left[0]==m-1&&left[1]==m-1||right[0]==m-1&&right[1]==m-1) {
			if(check<answer) {
				answer=check;
			}
			return;
		}
		
		System.out.println(check);
		int[] nextLeft = new int[2];
		int[] nextRight = new int[2];
		if (left[0]==right[0]) { // 수평 상황					
			if (right[1]+1<m&&target[right[0]][right[1]+1]!=1) {//  우  
				nextLeft[0]=left[0];
				nextLeft[1]=left[1]+1;
				nextRight[0]=right[0];
				nextRight[1]=right[1]+1;
				System.out.println("up");
				move(target, m, nextLeft, nextRight, check+1);
			}
			else if(left[0]+1<m&&right[0]+1<m&&target[left[0]+1][left[1]]!=1&&target[right[0]+1][right[1]]!=1) { //하
				nextLeft[0]=left[0]+1;
				nextLeft[1]=left[1];
				nextRight[0]=right[0]+1;
				nextRight[1]=right[1];
				
				System.out.println("down");
				move(target,m,nextLeft,nextRight,check+1);
				
//				horizon90
				nextLeft[0]=right[0]+1;  
				nextLeft[1]=right[1];
				nextRight[0]=right[0];
				nextRight[1]=right[1];
				System.out.println("horizon90");
				move(target,m,nextLeft,nextRight,check+1);
//				horizon90
				nextLeft[0]=left[0];  
				nextLeft[1]=left[1];
				nextRight[0]=left[0]+1;
				nextRight[1]=left[1];
				System.out.println("horizon90");
				move(target,m,nextLeft,nextRight,check+1);
				
			}else {
				return;
			}
			
		}else if(left[1]==right[1]){ // 수직 상황
			if(left[1]+1<m&&right[1]+1<m&&target[left[0]][left[1]+1]!=1&&target[right[0]][right[1]+1]!=1) { //우
				nextLeft[0]=left[0];
				nextLeft[1]=left[1]+1;
				nextRight[0]=right[0];
				nextRight[1]=right[1]+1;
				move(target,m,nextLeft,nextRight,check+1);
				
//				vertical90
				nextLeft[0]=left[0];
				nextLeft[1]=left[1];
				nextRight[0]=left[0];
				nextRight[1]=left[1]+1;
				move(target,m,nextLeft,nextRight,check+1);
			}
			else if(left[0]+1<m&&target[left[0]+1][left[1]]!=1) {
				nextLeft[0]=left[0]+1;
				nextLeft[1]=left[1];
				nextRight[0]=left[0];
				nextRight[1]=left[1];
				System.out.println("down");
				move(target, m, nextLeft, nextRight, check+1);
			}else {
				return;
			}
//			if(left[1]-1>=0&&target[left[0]][left[1]-1]!=1&&right[1]-1>=0&&target[right[0]][right[1]-1]!=1) {
//				nextLeft[0]=left[0];
//				nextLeft[1]=left[1]-1;
//				nextRight[0]=left[0];
//				nextRight[1]=left[1];
////				System.out.println("down");
//				move(target, m, nextLeft, nextRight, check+1);
//			}
		}
	}

	public static void main(String[] args) {
		int[][] board = {{0, 0, 0, 1, 1},{0, 0, 0, 1, 0},{0, 1, 0, 1, 1},{1, 1, 0, 0, 1},{0, 0, 0, 0, 0}};
		
		int m=board.length;
		answer = m*m;
		int[] left = new int[2];
		int[] right = new int[2];
		
		left[0]=0;
		left[1]=0;
		right[0]=0;
		right[1]=1;
		move(board,m,left,right,0);
		System.out.println(answer);
	}

}
