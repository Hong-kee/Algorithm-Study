import java.io.*;

public class Main {

	private static int answer = 0, diffInit, diff;
	private static String num;
	private static boolean isSame;
	
	public static void main(String[] args) throws IOException{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		num = br.readLine(); 
		
		while (Integer.parseInt(num) != 0) {
			if (num.length() <= 2) {
				++answer;
				num = Integer.toString(Integer.parseInt(num) - 1);
				continue;
			}
			diffInit = (num.charAt(0) - '0') - (num.charAt(1) - '0');
			isSame = true;
			
			for (int i = 0; i < num.length() - 1; i++) {
				diff = (num.charAt(i) - '0') - (num.charAt(i + 1) - '0');
				if (diff != diffInit) {
					isSame = false;
					break;
				}
			}
			if (isSame) ++answer;
			num = Integer.toString(Integer.parseInt(num) - 1);
		}
		System.out.println(answer);
	}

}
