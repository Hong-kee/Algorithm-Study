import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Integer> transmission = new ArrayList<>();
        boolean isLevel = false;

        while (st.hasMoreTokens()) {
            transmission.add(Integer.parseInt(st.nextToken()));
        }

        if (transmission.get(0) < transmission.get(1)) {
            isLevel = true;
        }

        for (int i = 2; i < transmission.size(); i++) {
            if (transmission.get(i - 1) < transmission.get(i) && !isLevel || transmission.get(i - 1) > transmission.get(i) && isLevel) {
                System.out.println("mixed");
                return;
            }
        }

        if (isLevel) System.out.println("ascending");
        else System.out.println("descending");
    }

}
