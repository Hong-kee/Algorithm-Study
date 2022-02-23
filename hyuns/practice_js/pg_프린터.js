function solution(priorities, location) {
    var answer = 0;
    let print = []
    while (priorities.length !== 0){
        
        var flag = true;
        for (var pri of priorities.slice(1)){
            if(priorities[0] < pri){
                priorities.push(priorities.shift())
                location -= 1
                if(location<0){
                    location=priorities.length-1
                }
                flag = false
                break
            }
        }
        if (flag){
            print.push(priorities.shift())
            location -= 1
            if (location === -1){
                answer = print.length
                break
            }
            
        }
    }
    return answer;
}

priorities = [1, 1, 9, 1, 1, 1]
location = 0
console.log(solution(priorities, location))