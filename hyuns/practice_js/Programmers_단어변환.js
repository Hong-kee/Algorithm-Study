function counts(w1, w2){
    let hash = {}
    let sums = 0
    for (var i of w1){
        hash[i] = hash[i] ? hash[i]+1 : 1
    }

    for (var i of w2){
        if (hash[i]){
            sums += 1
            continue;
        }
    }
    
    if (sums === 2){
        return true
    }
    else{
        return false
    }
}

function bfs(index, words){
    
    let q = []
    let answer = 1
    let result = words.length
    let visit = new Array(words.length).fill(false)
    visit[index] = true
    q.push([index, answer, visit])
    while (q.length !== 0){
        let [q_index, q_answer, q_visit] = q.shift();
        if (q_index === words.length-1){
            result = Math.min(q_answer, result)
        }
        else{
            for (var i=0; i<words.length; i++){
                if (q_visit[i] === false){
                    if (counts(words[i], words[q_index])){
                        q_visit[i] = true
                        q.push([i, q_answer+1, q_visit])
                    }
                }
                
            }
        }
        
    }
    return result
}

function solution(begin, target, words) {
    let answer = words.length;
    
    if (!words.includes(target)){
        return 0
    }

    for (var index in words){
        if (counts(begin, words[index])){
            answer = Math.min(answer, bfs(index, words))
        }
    }
    return answer;
}

begin = "htt"
target = "cog"
words = ["hot", "tbt", "dog", "lot", "log", "cog"]

console.log(solution(begin, target, words))