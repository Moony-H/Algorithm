import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        ArrayList<ArrayList<Integer>> reported= new ArrayList<>(id_list.length);
        HashMap<String,Integer> names=new HashMap<>();
        for(int i=0;i<id_list.length;i++){
            names.put(id_list[i],i);
            reported.add(new ArrayList<Integer>());
        }
        for(String i:report){
            String[] user=i.split(" ");
            if(reported.get(names.get(user[1])).contains(names.get(user[0]))){
                continue;
            }
            reported.get(names.get(user[1])).add(names.get(user[0]));
        }

        for(ArrayList<Integer> i:reported){
            if(i.size()>=k){
                for(int j:i){
                    answer[j]+=1;
                }
            }
        }


        return answer;
    }
}