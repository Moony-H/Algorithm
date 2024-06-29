fun main() {
    val n= readln().toInt()
    val starNum=1+((n-1)*2)
    var nowStar=starNum
    for(i in 0 until n){
        println(" ".repeat((starNum-nowStar)/2)+"*".repeat(nowStar))
        nowStar-=2
    }
    nowStar+=4
    for(i in 0 until n-1){
        println(" ".repeat((starNum-nowStar)/2)+"*".repeat(nowStar))
        nowStar+=2
    }

}