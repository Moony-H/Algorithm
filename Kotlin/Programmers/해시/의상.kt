class Solution {
    fun solution(clothes: Array<Array<String>>): Int {
        var answer = 0
        val hash=HashMap<String,ArrayList<String>>()
        clothes.forEach{cloth->
            hash[cloth[1]]?.add(cloth[0])?:run{
                hash[cloth[1]]=arrayListOf(cloth[0])
            }
        }
        var result=1
        hash.forEach{item->
            result*=(item.value.size+1)
            
        }
        return result-1
    }
}