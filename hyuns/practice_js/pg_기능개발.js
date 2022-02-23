//sol1.
function solution(progresses, speeds) {
    var answer = [];
    let days = [];
    let res = [];

    for (var i=0; i < progresses.length; i++){
        days.push(Math.ceil((100-progresses[i])/speeds[i]))
    }

    while (days.length !== 0){
        res.push(days.shift())
        if (res[0] < days[0] || days.length===0){
            answer.push(res.length)
            res = []
        }
    }
    return answer;
}
progresses = [98, 95, 95]
speeds = [3,3,3]
console.log(solution(progresses, speeds))



// sol2
function solution2(progresses, speeds) {
    let time = 0
    let count = 0
    let index = 0
    let answer = []
    
    while (index !== progresses.length){
        if (progresses[index] + time*speeds[index] >= 100){
            index += 1
            count++
        }
        else{
            if (count === 0){
                time++
            }
            else{
                answer.push(count)
                count = 0
            }
            
        }
    }
    answer.push(count)
    return answer
}

console.log(solution2(progresses, speeds))