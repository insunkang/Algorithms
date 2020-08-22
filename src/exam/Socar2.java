package exam;

public class Socar2 {

	public static void main(String[] args) {
		String[] drum = {"######",">#*###","####*#","#<#>>#",">#*#*<","######"};
		int num = drum.length;
		String[][] target = new String[num][num];
		
		for (int i = 0; i < drum.length; i++) {
			for (int j = 0; j < drum.length; j++) {
				target[i][j]=drum[i].split("")[j];
			}
		}
		int result = 0;
		for (int i = 0; i < target.length; i++) {
			int star =0;
			int m=0;
			int n=i;
			while(true) {
				if (target[m][n].equals("#")) {
					if (m==num-1) {
						result++;
						break;
					}else {
						m++;
					}
				}else if (target[m][n].equals(">")) {
					n++;
				}else if (target[m][n].equals("<")) {
					n--;
				}else {
					star++;
					m++;
				}
				if (star==2) {
					break;
				}
				
			}
		}
		System.out.println(result);
	}

}
