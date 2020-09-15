package kakaoBlind2020;

public class LineFthQ {
	static int result=0 ;
	public static void leftHand(int[][] maze, int[] presentMN, int[] loc) {
		//왼손 위치  
				// 위  오  아래  왼
		if (loc[0]==maze.length-1&&loc[1]==maze.length-1) {
			return;
		}
		int[] m = {-1,0, 1,0};
		int[] n = { 0,1,0,-1};
		int check = 0;
		for (int i = 0; i < n.length; i++) {		
			if (presentMN[0]==m[i]&&presentMN[1]==n[i]) {
				if (i==3) { //0으로
					check=0;									
				}else {
					
					check=i+1;
				}
			}
		}
		
		int[] handwall = new int[2];
		int[] next = new int[2];
		handwall[0]=loc[0]+presentMN[0];
		handwall[1]=loc[1]+presentMN[1];
		System.out.println(loc[0]+","+loc[1]+"check"+check);
		
//		if (handwall[0]<0||handwall[0]>=maze.length||handwall[1]<0||handwall[1]>=maze.length||maze[handwall[0]][handwall[1]]==1) { //왼손이 1(내부벽), 외부벽 이고
//			System.out.println(0);
//			if (handwall[0]+m[check]==-1||handwall[0]+m[check]==maze.length||handwall[1]+n[check]==-1||handwall[1]+n[check]==maze.length||maze[handwall[0]+m[check]][handwall[1]+n[check]]==1) { //손의 다음 경로가 벽일때
//				if (
//						loc[0]+m[check]<0||loc[0]+m[check]==maze.length||loc[1]+n[check]<0||loc[1]+n[check]==maze.length
//						||maze[loc[0]+m[check]][loc[1]+n[check]]==1) { //회전할때
//					
					
					
				if(maze[handwall[0]+m[check]][handwall[1]+n[check]]==0&&maze[loc[0]+m[check]][loc[1]+n[check]]==0){//손의 다음경로가 0일 때(회전)
					
					System.out.println(4);
					int a=check;
					if (check==0) {
						check=3;
					}else {
						check=check-1;
					}
					next[0]=presentMN[0]+m[check];
					next[1]=presentMN[1]+n[check];
					loc[0]=handwall[0]+m[a];
					loc[1]=handwall[1]+n[a];
					leftHand(maze,next,loc);
					result=result+2;
				}else if(maze[handwall[0]+m[check]][handwall[1]+n[check]]==1&&maze[loc[0]+m[check]][loc[0]+n[check]]==0){												//회전 안할때
					System.out.println(2);
					next[0]=presentMN[0]+m[check];
					next[1]=presentMN[1]+n[check];
					loc[0]=loc[0]+m[check];
					loc[1]=loc[1]+n[check];
					result++;
					leftHand(maze,presentMN,loc);
				}else {
					System.out.println(1);
					next[0]=m[check];
					next[1]=n[check];
					leftHand(maze,next,loc);
				}
//			}else if(maze[handwall[0]+m[check]][handwall[1]+n[check]]==1){ //다음 경로가 내부벽일때
//				
//				loc[0]=loc[0]+m[check];
//				loc[1]=loc[1]+n[check];
//				result++;
//				leftHand(maze,presentMN,loc);
//				System.out.println(3);
//			}
//		}
		
		
	
		
	}
	public static void main(String[] args) {
		int[][] maze = {{0, 1, 0, 1}, {0, 1, 0, 0}, {0, 0, 0, 0}, {1, 0, 1, 0}};
		
		//왼손 위치  
				// 위  아래  왼  오
		int[] m = {-1,1, 0,0};
		int[] n = { 0,0,-1,1};
		
		int[] presentMN = new int[2];
		
		
		if (maze[0][1]==1) {
			presentMN[0]=0;
			presentMN[1]=1;
		}else if (maze[0][1]==0) {
			presentMN[0]=-1;
			presentMN[1]=0;
		}
		int mn[]= new int[2];
		mn[0]=0;
		mn[1]=0;
		leftHand(maze,presentMN,mn);
		System.out.println(result+"result");
		
	}

}
