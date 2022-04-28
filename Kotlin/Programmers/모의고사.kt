class Solution {
    fun solution(answers: IntArray): IntArray {
        var answer = mutableListOf<Int>()
        val people=arrayOf(
            arrayOf(1,2,3,4,5),
            arrayOf(2,1,2,3,2,4,2,5),
            arrayOf(3,3,1,1,2,2,4,4,5,5)
        )
        var max=0
        people.forEachIndexed{people:Int,pattern:Array<Int>->
            val length=pattern.size
            var matched=0
            answers.forEachIndexed{index:Int,num:Int->
                if(num==pattern[index%length]){
                    matched+=1
                }

            }
            if(matched>max){
                max=matched
                answer=mutableListOf<Int>(people+1)
            }
            else if (matched==max){
                answer.add(people+1)
            }

        }

        return answer.toIntArray()
    }
}