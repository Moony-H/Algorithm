import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        ArrayList<Stack<Integer>> stacks=new ArrayList<>(board.length);
        Stack<Integer> store=new Stack<>();
        for(int i=0; i<board.length;i++){
            stacks.add(new Stack<Integer>());
        }

        for(int i=board.length-1;i>=0;i--){

            for(int j=0;j<board.length;j++){
                if (board[i][j]==0){
                    continue;
                }
                stacks.get(j).push(board[i][j]);
            }
        }


        for(int i=0;i<moves.length;i++){
            int pos=moves[i]-1;
            if(stacks.get(pos).size()==0){
                continue;
            }
            store.push(stacks.get(pos).peek());
            stacks.get(pos).pop();
            if(store.size()>1 && store.get(store.size()-1)==store.get(store.size()-2)){
                store.pop();
                store.pop();
                answer+=2;
            }
        }




        return answer;
    }
}