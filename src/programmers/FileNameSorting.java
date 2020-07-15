package programmers;

public class FileNameSorting {

	public static void main(String[] args) {
		 String[] files = {"img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"};
		 int fileLength = files.length;
	        
	        String[][] test = new String[fileLength][3];
	        
	        //2중 배열의 첫행의 첫열에 각 files들 넣어주기
	        for(int i =0; i<fileLength; i++){ 
	            test[i][0]=files[i];
	            
	        }
	        
	        //첫번째 분할(숫자 찾기)
	        for(int i =0; i<test.length; i++){ 
	            for(int j=0; j<test[i][0].length();j++){
	                
	                if(test[i][0].charAt(j)>=48&&test[i][0].charAt(j)<=57){
	                	char first = test[i][0].charAt(j);
	                    String[] splited = test[i][0].split(Character.toString(test[i][0].charAt(j)),2);
	                    test[i][0]= splited[0];
	                    test[i][1]= first+splited[1];
	                    break;
	                }
	                
	            }   
	        }
	        //두번째 분할(숫자 끝나는 부분 찾기)
	        for(int i =0; i<test.length; i++){ 	        
	            for(int j=0; j<test[i][1].length();j++){
	                
	                if(test[i][1].charAt(j)<48||test[i][1].charAt(j)>57){
	                	String second ="";
	                	if(test[i][1].charAt(j)=='.') {
	                		second = Character.toString(test[i][1].charAt(j-1));
	                		String[] splited = test[i][1].split(second,2);
     	                   
		                    test[i][1]= splited[0]+second;
		                    test[i][2]= splited[1];
	                	}else {
	                		second = Character.toString(test[i][1].charAt(j));
	                		String[] splited = test[i][1].split(second,2);
	     	                   
		                    test[i][1]= splited[0];
		                    test[i][2]= second+splited[1];
	                	}	                		                		               
	                	
	                    break;
	                }
	                
	            }   
	        }	        	        	       
	        
	        //code test
	        for (int i = 0; i < test.length; i++) {
				for (int j = 0; j < 3; j++) {
					if(j==2) {
					System.out.println(test[i][j]);
					}else {
					System.out.print(test[i][j]+" ");
					}
				}
			}
	        //첫번째 항으로 비교 
	        for (int i = 0; i < test.length; i++) {
	        	
	        	for (int j = 0; j < test.length; j++) {
	        		
	        		if (test[i][0].toLowerCase().compareTo(test[j][0].toLowerCase())>0) {
	        			String a = files[i];
	        			String b = files[j];
	        			
	        			files[i]= b;
	        			files[j]= a;
	        		}
	        	
					
				}
			}
	        
	        //확인
	        System.out.println("---");
	        for (int i = 0; i < files.length; i++) {
				System.out.println(files[i]);
			}
	        //두번째 항으로 비교 
	        for (int i = 0; i < test.length; i++) {
	        	
	        	for (int j = 0; j < test.length; j++) {
	        		
	        		if (Integer.parseInt(test[i][1])>Integer.parseInt(test[j][1])) {
	        			String a = files[i];
	        			String b = files[j];
	        			
	        			files[i]= b;
	        			files[j]= a;
	        			
	        		}
	        	
					
				}
			}
	        
	        //확인
	        System.out.println("---");
	        for (int i = 0; i < files.length; i++) {
				System.out.println(files[i]);
			}

	}

}
