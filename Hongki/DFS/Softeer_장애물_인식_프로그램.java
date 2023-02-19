import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {

    static int[][] map;
    static boolean[][] visited;
    static int inputSize;
    static int[][] dir = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    static int countSection = 0;
    static int countPerSection = 1;
    static List<Integer> countPerSections = new ArrayList<>();

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        inputSize = Integer.parseInt(br.readLine());

        map = new int[inputSize][inputSize];
        visited = new boolean[inputSize][inputSize];

        for (int i = 0; i < inputSize; i++) {
            String inputMapValue = br.readLine();
            for (int j = 0; j < inputMapValue.length(); j++) {
                map[i][j] = Integer.parseInt(String.valueOf(inputMapValue.charAt(j)));
            }
        }

        for (int i = 0; i < inputSize; i++) {
            for (int j = 0; j < inputSize; j++) {
                if (!visited[i][j] && map[i][j] == 1) {
                    searchingMap(i, j);
                    countSection++;
                    countPerSections.add(countPerSection);
                    countPerSection = 1;
                }
            }
        }

        Collections.sort(countPerSections);

        System.out.println(countSection);
        for (int i = 0; i < countPerSections.size(); i++) {
            System.out.println(countPerSections.get(i));
        }
    }

    static boolean isBound(int y, int x) {
        return y < inputSize && y >= 0 && x < inputSize && x >= 0;
    }

    static void searchingMap(int y, int x) {
        visited[y][x] = true;

        for (int i = 0; i < 4; i++) {
            int dy = y + dir[i][0];
            int dx = x + dir[i][1];

            if (isBound(dy, dx) && map[dy][dx] == 1 && !visited[dy][dx]) {
                countPerSection++;
                searchingMap(dy, dx);
            }
        }
    }

}
