function solution(numbers, target) {
    var answer = 0;

    if (numbers.length === 0){
        if (target===0){
            return 1
        }
        else{
            return 0
        }
    }
    return solution(numbers.slice(1), target-numbers[0]) + solution(numbers.slice(1), target+numbers[0])
}