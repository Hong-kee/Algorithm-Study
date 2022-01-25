package baekjoon.math;

import java.io.*;
import java.util.*;

public class Main2869 {

    static int up, down, height;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        up = Integer.parseInt(st.nextToken());
        down = Integer.parseInt(st.nextToken());
        height = Integer.parseInt(st.nextToken());

        if ((height - down) % (up - down) == 0) System.out.println((height - down) / (up - down));
        else System.out.println((height - down) / (up - down) + 1);
    }
}
