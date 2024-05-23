class Solution {
    val percentage=arrayListOf(10,20,30,40)
    var emoPlus=0
    var totalPrice=0
    
    //fun 
    fun dfs(users:Array<IntArray>,emoticons:IntArray,depth:Int,list:MutableList<Int>){
        if(depth==0){
            var resultPrice=0
            var resultEmoPlus=0
            val l=list.mapIndexed{i,item->
                Pair((((100f-item)/100)*emoticons[i]).toInt(),item)
            }
            
            users.forEach{user->
                val userPercent=user[0]
                val userPrice=user[1]
                var userPriceSum=0
                l.forEach{pair->
                    val price=pair.first
                    val percent=pair.second
                    if(percent>=userPercent){
                        userPriceSum+=price
                    }
                }
                if(userPrice>userPriceSum){
                    resultPrice+=userPriceSum
                }else{
                    resultEmoPlus+=1
                }
                
            }
            
            if(resultEmoPlus>emoPlus){
                emoPlus=resultEmoPlus
                totalPrice=resultPrice
            }else if(resultEmoPlus==emoPlus&& totalPrice<resultPrice){
                totalPrice=resultPrice
            }
            
            return
        }
        percentage.forEach{
            list.add(it)
            dfs(users,emoticons,depth-1,list)
            list.removeAt(list.size-1)
        }
            
    }
    fun solution(users: Array<IntArray>, emoticons: IntArray): IntArray {
        
        dfs(users,emoticons,emoticons.size,mutableListOf())
        return intArrayOf(emoPlus,totalPrice)
    }
}