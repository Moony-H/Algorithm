class Solution {
    fun solution(order: Array<String>) =
        order.count{"americano" in it || "anything"==it}*4500 + order.count{"cafelatte" in it}*5000
}