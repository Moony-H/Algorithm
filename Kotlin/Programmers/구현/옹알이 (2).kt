class Solution {
    
    private val words=arrayOf("aya","ye","woo","ma")
    
    fun canSay(word:String):Boolean{
        var wordStack=""
        var before=""
        word.forEach{
            wordStack+=it
            if(before==wordStack)
                return@forEach
            if(words.contains(wordStack)){
                before=wordStack
                wordStack=""
            }
        }
        return wordStack.isEmpty()
    }
    
    fun solution(babbling: Array<String>): Int {
        return babbling.count{println(canSay(it));canSay(it)}
    }
}