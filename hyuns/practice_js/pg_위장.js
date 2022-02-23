function solution(clothes) {
    var answer = 1;
    let obj = {};

    for (var cloth of clothes){
        obj[cloth[1]] = obj[cloth[1]] ? obj[cloth[1]]+1 : 1
    }
    console.log(obj[0])
    for (var i in obj){
        console.log(i)
        // answer *= (obj[i] + 1)
    }
    return answer - 1;
}

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
console.log(solution(clothes))