import java.util.Scanner

fun readln():String = readLine()?:throw IllegalStateException("input not exist")

fun sortProblems(problems:Array<ArrayList<Int>>){
	problems.forEach{
		it.sort()
	}
}

fun findMinMinute(list:ArrayList<Int>,range:Int):Int{
	var l=0
	var r=range-1
	val size=list.size
	var sum=0
	var result=0
	//초기 값 구하기
	for(i in 0 until range){
		sum+=list[i]
		if(i!=0){
			sum+=list[i]-list[i-1]
		}
	}
	result=sum
	while(r<size){
		l+=1
		r+=1
		if(r>=size){
			break
		}
		//끝만 더하고 빼기
		sum-=list[l-1]
		sum+=list[r]
		
		//차이 빼기
		sum-=list[l]-list[l-1]
		
		//새로운 차이 더하기
		sum+=list[r]+list[r-1]
		
		//최대값 갱신
		if(result>sum){
			result=sum
		}
	}
	return result
}

fun main(args: Array<String>) {
	//저장할 공간 만들기
	val problems=Array(5){
		ArrayList<Int>()
	}
	
	//입력받기
	val n=readln().toInt()
	val toDoLevelNumList=readln().split(" ").map{it.toInt()}
	
	//난이도 별로 정리하기
	for(i in 0 until n){
		val input=readln().split(" ").map{it.toInt()}
		val level=input[0]-1
		val minute=input[1]
		problems[level].add(minute)
	}

	
	//난이도 별 sorting
	sortProblems(problems)
	//난이도 별 슬라이딩 윈도우로 최소 값 구하기
	var result=0
	for(i in 0 until problems.size){
		val range=toDoLevelNumList[i]
		val problemList=problems[i]
		result+=findMinMinute(problemList,range)
	}
	
	//단계 올리는 값 60분 더하기(p가 항상 1보다 크니까 항상 60*4를 더하면 됨.)
	result+=60*4
	println(result)
	
}