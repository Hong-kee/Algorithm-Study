import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.PriorityQueue;

/**
 * using heap sort
 */
public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder stringBuilder = new StringBuilder();
        PriorityQueue<Attendee> attendeePriorityQueue;

        int countPerson = Integer.parseInt(br.readLine());
        int[] scorePerson = new int[countPerson];
        int[] grades = new int[countPerson];
        String[] inputScores;

        for (int i = 0; i < 4; i++) {
            attendeePriorityQueue = new PriorityQueue<>();
            int order = 0, pivot = 0;
            int count = 1;
            int standardScore = 987654321;

            if (i != 3) {
                inputScores = br.readLine().split(" ");
                for (String inputScore : inputScores) {
                    attendeePriorityQueue.add(new Attendee(Integer.parseInt(inputScore), order));
                    scorePerson[order] += Integer.parseInt(inputScore);
                    ++order;
                }
            } else {
                attendeePriorityQueue.clear();
                for (int j = 0; j < countPerson; j++) {
                    attendeePriorityQueue.add(new Attendee(scorePerson[j], j));
                }
            }

            for (int j = 0; j < countPerson; j++) {
                if (standardScore > attendeePriorityQueue.peek().getScore()) {
                    grades[attendeePriorityQueue.peek().getOrder()] = pivot + count;
                    standardScore = attendeePriorityQueue.peek().getScore();
                    pivot = grades[attendeePriorityQueue.peek().getOrder()];
                    count = 1;
                } else {
                    grades[attendeePriorityQueue.peek().getOrder()] = pivot;
                    ++count;
                }

                attendeePriorityQueue.poll();
            }

            for (int grade : grades) {
                stringBuilder.append(grade).append(" ");
            }

            stringBuilder.append("\n");
        }

        bw.write(stringBuilder.toString());
        bw.flush();
        bw.close();

    }

    static class Attendee implements Comparable<Attendee> {
        int score;

        int order;

        public Attendee(int score, int order) {
            this.score = score;
            this.order = order;
        }

        public int getScore() {
            return score;
        }

        public void setScore(int score) {
            this.score = score;
        }

        public int getOrder() {
            return order;
        }

        public void setOrder(int order) {
            this.order = order;
        }

        @Override
        public int compareTo(Attendee o) {
            return o.getScore() - getScore();
        }

    }

}
