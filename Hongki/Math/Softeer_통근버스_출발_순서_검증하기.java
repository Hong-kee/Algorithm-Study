import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] busNumbers;
        int answer = 0;
        int busCount = Integer.parseInt(br.readLine());
        int[][] sumCount = new int[busCount + 1][busCount + 1];

        busNumbers = br.readLine().split(" ");

        for (int i = busCount - 1; i > -1; i--) {
            for (int j = 1; j <= busCount; j++) {
                if (Integer.parseInt(busNumbers[i]) < j) {
                    sumCount[j][i] = sumCount[j][i + 1] + 1;
                } else {
                    sumCount[j][i] = sumCount[j][i + 1];
                }
            }
        }

        for (int i = 0; i < busCount; i++) {
            for (int j = i; j < busCount; j++) {
                if (Integer.parseInt(busNumbers[i]) < Integer.parseInt(busNumbers[j])) {
                    answer += sumCount[Integer.parseInt(busNumbers[i])][j];
                }
            }
        }

        System.out.print(answer);
    }

}
