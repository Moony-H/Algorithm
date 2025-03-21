class Solution {
    fun sign(board:Array<IntArray>,start:Pair<Int,Int>){
        for(i in 0..2){
            for(j in 0..2){
                val x=start.first-1+j
                val y=start.second-1+i
                if(x<0 || y<0 || x>=board[0].size || y>=board.size || board[y][x]==1)
                    continue
                board[y][x]=2
            }
        }
    }
    fun solution(b: Array<IntArray>): Int {
        for(i in b.indices){
            for(j in b[i].indices){
                if(b[i][j]==1)sign(b,j to i)
            }
        }
        return b.sumOf{it.count{it==0}}
    }
}