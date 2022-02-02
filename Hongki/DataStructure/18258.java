import java.io.*;
import java.util.*;

public class Main {

    static int[] q = new int[2000000];
    static StringBuilder sb = new StringBuilder();
    static int size = 0;
    static int front = 0;
    static int back = 0;

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int commandCnt = Integer.parseInt(br.readLine());

        while(commandCnt --> 0) {
            st = new StringTokenizer(br.readLine());
            String str = st.nextToken();

            if (str.equals("push")) push(Integer.parseInt(st.nextToken()));
            else if (str.equals("pop")) pop();
            else if (str.equals("size")) size();
            else if (str.equals("empty")) empty();
            else if (str.equals("front")) front();
            else if (str.equals("back")) back();
        }
        System.out.println(sb);
    }

    static void push(int num) {
        q[back] = num;
        ++back;
        ++size;
    }

    static void pop() {
        if (size == 0) sb.append(-1).append('\n');
        else {
            sb.append(q[front]).append('\n');
            front++;
            size--;
        }
    }

    static void size() {
        sb.append(size).append('\n');
    }

    static void empty() {
        if (size == 0) sb.append(1).append('\n');
        else sb.append(0).append('\n');
    }

    static void front() {
        if(size == 0) sb.append(-1).append('\n');
        else sb.append(q[front]).append('\n');
    }

    static void back() {
        if (size == 0) sb.append(-1).append('\n');
        else sb.append(q[back - 1]).append('\n');
    }
}
