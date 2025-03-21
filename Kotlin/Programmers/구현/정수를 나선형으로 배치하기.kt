class Solution {
    fun fill(n:Int,r:Int,map:Array<IntArray>,start:Pair<Int,Int>){
        if(r<0) return
        var vN=n
        var x=start.first-1
        var y=start.second
        repeat(r){
            x+=1
            map[y][x] = vN
            vN++
        }
        repeat(r-1){
            y+=1
            map[y][x] = vN
            vN++
        }
        repeat(r-1){
            x-=1
            map[y][x] = vN
            vN++
        }
        repeat(r-2){
            y-=1
            map[y][x]=vN
            vN++
        }
        fill(vN,r-2,map,x+1 to y)
    }
    fun solution(n: Int): Array<IntArray> {
        val answer = Array(n){IntArray(n){0}}
        fill(1,n,answer,0 to 0)
        return answer
    }
}