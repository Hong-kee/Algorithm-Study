function dfs(i, visit, computers){
    for (var j=0; j<computers.length; j++){
        if (i===j){
            continue;
        }
        if (computers[i][j]==1 && visit[j] === false){
            visit[j] = true;
            dfs(j, visit, computers);
        }
    }
    
}
function solution(n, computers) {
    var answer = 0;
    let visit = []
    for (var i=1; i<=n; i++){
        visit.push(false)
    }

    
    for (var i=0; i<n; i++){
        if (visit[i] === false){
            visit[i] = true
            dfs(i, visit, computers)
            answer += 1
        }
    }
    return answer;
}

numbers = [1,1,1,1,1]
target = 3

console.log(solution(numbers, target))