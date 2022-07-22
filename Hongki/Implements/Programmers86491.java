import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[][] sizes) {
        int maxY = 0, maxX = 0;
        
        for (int i = 0; i < sizes.length; i++) {
            int y = sizes[i][0];
            int x = sizes[i][1];
            
            sizes[i][0] = Math.max(y, x);
            sizes[i][1] = Math.min(y, x);
        }
        
        for (int i = 0; i < sizes.length; i++) {
            maxY = Math.max(maxY, sizes[i][0]);
            maxX = Math.max(maxX, sizes[i][1]);
        }
        return maxY * maxX;
    }
}
