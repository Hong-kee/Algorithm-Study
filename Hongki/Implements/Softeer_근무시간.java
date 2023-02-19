import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        SimpleDateFormat sdf = new SimpleDateFormat("HH:mm");
        long answer = 0;

        for (int i = 0; i < 5; i++) {
            List<String> workingTimes = new ArrayList<>();
            String inputTimes = br.readLine();
            st = new StringTokenizer(inputTimes," ");

            while (st.hasMoreTokens()) {
                workingTimes.add(String.valueOf(st.nextToken()));
            }

            Date startTime = sdf.parse(workingTimes.get(0));
            Date endTime = sdf.parse(workingTimes.get(1));

            answer += endTime.getTime() - startTime.getTime();
        }
        
        answer /= 1000 * 60;
      
        System.out.println(answer);
    }

}
