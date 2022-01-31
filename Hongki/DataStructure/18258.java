/**
* 추후 추가 예정
*/
package baekjoon.datastructure;

import java.io.*;
import java.util.*;

public class Main18258 {

    static int[] q = new int[2000000];

    static int size = 0;
    static int front = 0;
    static int rear = 0;

    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int commandCnt = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < commandCnt; i++) {
            if (st.nextToken() == "push") {}
            else if (st.nextToken() == "pop") {}
            else if (st.nextToken() == "size") {}
            else if (st.nextToken() == "empty") {}
            else if (st.nextToken() == "front") {}
            else if (st.nextToken() == "back") {}
        }
    }
}
