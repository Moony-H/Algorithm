import java.util.Scanner


var max:Int=0
fun readln():String = readLine()?:throw IllegalStateException();

fun abs(num:Int):Int= if(num<0) -num else num

fun allCase(list:List<Int>, pickedList:ArrayList<Int>,picked:HashMap<Int,Boolean>,depth:Int){
	if(depth==0){
		val total=abs(pickedList[0]-pickedList[1])+abs(pickedList[2]-pickedList[3])
		max=if(max<total) total else max
		return
	}
	list.forEach{
		picked[it]?.let{return@forEach}
		picked[it]=true
		pickedList.add(it)
		allCase(list,pickedList,picked,depth-1)
		picked.remove(it)
		pickedList.removeLast()
	}
}

fun main(args: Array<String>) {
	val numbers=readln().split(" ").map{it.toInt()}
	allCase(numbers,arrayListOf<Int>(),HashMap<Int,Boolean>(),4)
	println(max)
}