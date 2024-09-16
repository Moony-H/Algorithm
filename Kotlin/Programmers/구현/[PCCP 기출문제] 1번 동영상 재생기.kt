class Solution {
    
    fun toSecInt(time:String):Int{
        val timeList=time.split(":").map{it.toInt()}
        return timeList[0]*60+timeList[1]
    }
    
    fun toTimeString(timeInt:Int):String=
        "${(timeInt/60).toString().padStart(2, '0')}:${(timeInt%60).toString().padStart(2,'0')}"
    
    fun commandToTime(command:String):Int{
        return when(command){
            "prev"-> -10
            "next"->10
            else -> -1
        }
    }
    
    fun limit(time:Int,len:Int):Int= if(time<0) 0 else if(time>len) len else time
    
    fun skipOp(start:Int,end:Int,num:Int):Int = if(num in start..end) end else num
    
    
    fun solution(video_len: String, pos: String, op_start: String, op_end: String, commands: Array<String>): String {
        var answer: String = ""
        val vLen=toSecInt(video_len)
        var posInt=toSecInt(pos)
        val opStart=toSecInt(op_start)
        val opEnd=toSecInt(op_end)
        
        posInt=skipOp(opStart,opEnd,posInt)
        
        commands.forEach{
            posInt+=commandToTime(it)
            posInt=limit(posInt,vLen)
            posInt=skipOp(opStart,opEnd,posInt)
        }
        
        return toTimeString(posInt)
    }
}