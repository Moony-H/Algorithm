fun main() {
    val stringList = ArrayList<String>()
    var maxLength = 0
    for (i in 0 until 5) {
        stringList.add(readln())
        maxLength = if (stringList[i].length > maxLength) stringList[i].length else maxLength
    }
    var charIndex = 0
    while (charIndex<maxLength) {
        for (i in 0 until 5) {
            if(charIndex>=stringList[i].length)
                continue
            print(stringList[i][charIndex])
        }
        charIndex++
    }
}
