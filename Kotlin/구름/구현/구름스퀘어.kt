import java.util.Scanner
import java.util.Stack

fun readln():String = readLine()?: throw IllegalStateException("input not exist")
fun main(args: Array<String>) {
	
	val schedule=arrayListOf<Pair<Int,Int>>()
	val stack=Stack<Pair<Int,Int>>()
	for(i in 0 until readln().toInt()){
		val input=readln().split(" ").map{
			it.toInt()
		}
		val s=input[0]
		val e=input[1]
		schedule.add(s to e)
	}
	schedule.sortWith(compareBy<Pair<Int,Int>>{it.first})
	
	schedule.forEach{
		if(stack.isEmpty()){
			stack.push(it)
			return@forEach
		}
		if(stack.peek().second>it.second){
			stack.pop()
			stack.push(it)
			return@forEach
		}
		if(stack.peek().second<it.first)
			stack.push(it)
	}
	
	println(stack.size)
}