import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static int answer = 987654321;

    static int money;

    static int fiveCount;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        money = Integer.parseInt(br.readLine());
        fiveCount = money / 5;

        for (int i = fiveCount; i >= 0; i--) {
            if ((money - i * 5) % 2 == 0) answer = Math.min(i + (money - i * 5) / 2, answer);
        }

        System.out.println(answer == 987654321 ? -1 : answer);

    }

}
