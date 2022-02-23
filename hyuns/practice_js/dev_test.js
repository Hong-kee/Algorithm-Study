// function solution(research, n, k) {
//     let count_research = []
//     let check_issue = {}
//     let answer = []
//     // 각 일 별 {검색어 종류 : 개수}

//     // count 다 시켜놓기
//     for (var word of research){
//         let count_word = {}
//         for (var chr of word){
//             count_word[chr] = count_word[chr] ? count_word[chr]+1 : 1
//         }
//         count_research.push(count_word)
//     }


//     for (var i=0; i < count_research.length; i++){
//         let count_word = count_research[i]
//         for (var j in count_word){
//             // 검색 횟수 만족
//             if (count_word[j] >= k){
//                 // 연속 n일 차인지 넣어주기
//                 // 이전 검색 + 오늘 검색
//                 if (!check_issue[j]){
//                     check_issue[j] = [1, count_word[j]]
//                 }
//                 else{
//                     check_issue[j] = [check_issue[j][0]+1, check_issue[j][1]+count_word[j]]
//                 }
//             }
//             else{
//                 if (check_issue[j]){
//                     if (check_issue[j][0] >= n && check_issue[j][1]>=2*n*k){
//                         answer.push(j)
//                     }
//                     check_issue[j] = []
//                 }
//             }
//         }
//     }

//     for (var j in check_issue){
//         if (check_issue[j]){
//             if (check_issue[j][0] == n && check_issue[j][1]>=2*n*k){
//                 answer.push(j)
//             }
//         }
//     }
    

//     answer.sort()
//     // answer.sort(function(a, b){
//     //     if (a[1] > b[1]){
//     //         return -1
//     //     }
//     //     if (a[1] === b[1]){
//     //         if (a[0] < b[0]){
//     //             return -1
//     //         }
//     //     }
//     // })
//     if (answer.length===0){
//         return "none"
//     };
//     return answer[0][0];
// }

// let research =  ["abaaaa","aaa","abaaaaaa","fzfffffffa"]
// let n = 2
// let k = 2

// console.log(solution(research, n, k))


function dfs(node, graph, value, result){
    let answer = 0
    if (graph[node].length === 0){
        return result
    }
    for (var data of graph[node]){
        answer = Math.max(answer, result + dfs(data, graph, value, value[data]))
    }
    return answer
}

function solution(value, projects) {
    let graph = new Array(value.length)

    for (var i=0; i<graph.length; i++){
        graph[i] = new Array;
    }

    for (var node of projects){
        graph[node[0]-1].push(node[1]-1)
    }

    return dfs(0, graph, value, value[0]);
}

value = [10, 11, 8, 5, 9, 15, 17]
projects =[[1, 2], [1, 3], [1, 4], [3, 5], [3, 6], [4, 7]]
console.log(solution(value, projects))