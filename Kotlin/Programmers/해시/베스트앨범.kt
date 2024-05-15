class Solution {
    fun solution(genres: Array<String>, plays: IntArray): IntArray {
        var answer = arrayListOf<Int>()
        val playingGenreHash=HashMap<String,Int>()
        val genreNumHash=HashMap<String,ArrayList<Pair<Int,Int>>>()
        for(i in genres.indices){
            playingGenreHash[genres[i]]=(playingGenreHash[genres[i]]?:0)+plays[i]
        }
        val playingList=ArrayList<Pair<String,Int>>(playingGenreHash.map{it.key to it.value })

        playingList.sortByDescending{
            it.second
        }
        for(i in genres.indices){
            genreNumHash[genres[i]]?.add(Pair(i,plays[i]))?:run{
                genreNumHash[genres[i]]=arrayListOf(Pair(i,plays[i]))
            }
        }
        
        genreNumHash.forEach{key,value->
            value.sortWith(compareBy({-it.second},{it.first}))
        }
        
        playingList.forEach{pair->
            val list=genreNumHash[pair.first]?:arrayListOf()
            list.getOrNull(0)?.let{answer.add(it.first)}
            list.getOrNull(1)?.let{answer.add(it.first)}
        }
        
        return answer.toIntArray()
    }
}