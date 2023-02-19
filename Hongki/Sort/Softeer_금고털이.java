import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

public class Main {

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] bagWeightAndJewelCounts = br.readLine().split(" ");
        List<JewelInformation> jewelInformations = new ArrayList<>();

        int bagWeight = Integer.parseInt(bagWeightAndJewelCounts[0]);
        int answer = 0;

        for (int i = 0; i < Integer.parseInt(bagWeightAndJewelCounts[1]); i++) {
            JewelInformation jewelInformation = new JewelInformation();
            String[] jewelInput = br.readLine().split(" ");

            jewelInformation.setJewelPrice(Integer.parseInt(jewelInput[1]));
            jewelInformation.setJewelSize(Integer.parseInt(jewelInput[0]));

            jewelInformations.add(jewelInformation);
        }

        Collections.sort(jewelInformations);

        for (int i = 0; i < jewelInformations.size(); i++) {
            if (bagWeight == 0) break;
            
            if (bagWeight > jewelInformations.get(i).getJewelSize()) {
                bagWeight -= jewelInformations.get(i).getJewelSize();
                answer += jewelInformations.get(i).getJewelSize() * jewelInformations.get(i).getJewelPrice();
            } else {
                if (bagWeight != 0) {
                    answer += bagWeight * jewelInformations.get(i).getJewelPrice();
                    bagWeight = 0;
                }
            }
        }

        System.out.println(answer);
    }

    static class JewelInformation implements Comparable<JewelInformation> {
        int jewelPrice;
        int jewelSize;

        public int getJewelPrice() {
            return jewelPrice;
        }

        public void setJewelPrice(int jewelPrice) {
            this.jewelPrice = jewelPrice;
        }

        public int getJewelSize() {
            return jewelSize;
        }

        public void setJewelSize(int jewelSize) {
            this.jewelSize = jewelSize;
        }

        @Override
        public int compareTo(JewelInformation o) {
            return o.getJewelPrice() - getJewelPrice();
        }

    }

}
