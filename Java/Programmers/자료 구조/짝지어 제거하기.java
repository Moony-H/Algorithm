import java.util.*;
class Solution
{
    public int solution(String s)
    {
        Stack<Character> stack=new Stack<>();
        for(char i:s.toCharArray()){
            if(!stack.isEmpty()&&stack.peek()==i){
                stack.pop();
            }
            else{
                stack.push(i);
            }
        }
        if(stack.isEmpty()){
            return 1;
        }
        return 0;
    }
}