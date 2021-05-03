fun main() {
    while(true){
        val n = readLine()!!.toInt()
        print("${solution(n)}\n")
    }
}

fun solution(n : Int): ArrayList<Int> {
    var num = 2 //현재 번호
    val result = arrayListOf<Int>()
    var currentLayer = 2 //현재 층
    var index = 1
    for(i in 0 until lenOfN(n)){
        result.add(0)
    }
    result[0] = 1
    var currentMove = "왼쪽 밑" //"왼쪽 밑", "오른쪽", "왼쪽 위"
    for(i in 1 until lenOfN(n)) {
        when(currentMove) {
            "왼쪽 밑" -> {
                if (index + currentLayer < result.size && result[index + currentLayer] == 0) {
                    currentMove = "왼쪽 밑"
                    result[index] = num
                    index += currentLayer
                    currentLayer++
                    num++
                }
                else if (index + 1 < result.size && result[index + 1] == 0) {
                    currentMove = "오른쪽"
                    result[index] = num
                    index++
                    num++
                }
                else if (index - currentLayer > 0 && result[index - currentLayer] == 0) {
                    currentMove = "왼쪽 위"
                    result[index] = num
                    index -= currentLayer
                    currentLayer--
                    num++
                }
            }
            "오른쪽" -> {
                if (index + 1 < result.size && result[index + 1] == 0) {
                    currentMove = "오른쪽"
                    result[index] = num
                    index++
                    num++
                }
                else if (index - currentLayer > 0 && result[index - currentLayer] == 0) {
                    currentMove = "왼쪽 위"
                    result[index] = num
                    index -= currentLayer
                    currentLayer--
                    num++
                }
                else if (index + currentLayer < result.size && result[index + currentLayer] == 0) {
                    currentMove = "왼쪽 밑"
                    result[index] = num
                    index += currentLayer
                    currentLayer++
                    num++
                }
            }
            "왼쪽 위" -> {
                if (index - currentLayer > 0 && result[index - currentLayer] == 0) {
                    currentMove = "왼쪽 위"
                    result[index] = num
                    index -= currentLayer
                    currentLayer--
                    num++
                }
                else if (index + currentLayer < result.size && result[index + currentLayer] == 0) {
                    currentMove = "왼쪽 밑"
                    result[index] = num
                    index += currentLayer
                    currentLayer++
                    num++
                }
                else if (index + 1 < result.size && result[index + 1] == 0) {
                    currentMove = "오른쪽"
                    result[index] = num
                    index++
                    num++
                }
            }
        }
    }
    for(i in 0 until result.size) {
        if(result[i] == 0) result[i] = num
    }
    return result
}

fun lenOfN(n : Int) : Int{
    if(n == 1) return 1
    return n + lenOfN(n-1)
}
