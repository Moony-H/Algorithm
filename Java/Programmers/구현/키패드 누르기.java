import java.util.*;
import java.lang.*;
class Solution {
    public String solution(int[] numbers, String hand) {
        String answer = "";
        int[][] pad={{1,3},{0,0},{1,0},{2,0},{0,1},{1,1},
                {2,1},{0,2},{1,2},{2,2},{0,3},{2,3}};

        int lx=0,ly=3,rx=2,ry=3;
        for(int num:numbers){
            if(num==1|| num==4|| num==7){
                answer+="L";
                lx=pad[num][0];
                ly=pad[num][1];
                continue;
            }
            if(num==3|| num==6|| num==9){
                answer+="R";
                rx=pad[num][0];
                ry=pad[num][1];
                continue;
            }
            int lDiff=Math.abs(lx-pad[num][0])+Math.abs(ly-pad[num][1]);
            int rDiff=Math.abs(rx-pad[num][0])+Math.abs(ry-pad[num][1]);
            System.out.println(Integer.toString(lDiff)+" "+Integer.toString(rDiff));
            if (lDiff<rDiff){
                answer+="L";
                lx=pad[num][0];
                ly=pad[num][1];
                continue;
            }
            if (rDiff<lDiff){
                answer+="R";
                rx=pad[num][0];
                ry=pad[num][1];
                continue;
            }
            System.out.println("same");
            if("left".equals(hand)){
                answer+="L";
                lx=pad[num][0];
                ly=pad[num][1];
                continue;
            }
            answer+="R";
            rx=pad[num][0];
            ry=pad[num][1];

        }
        return answer;
    }
}