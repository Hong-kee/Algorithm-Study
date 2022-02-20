// // let arr = ['사과', '바나나'];
// // let arr_1 = []

// // // 값 그대로 가져오기
// // for (i of arr){
// //     arr_1.push(i)
// // }

// // console.log("*".repeat(20))

// // // 뒤에 추가
// // arr_1.push("오렌지");
// // console.log(arr_1)
// // console.log("*".repeat(10))

// // // 뒤에 삭제
// // arr_1.pop();
// // console.log(arr_1)
// // console.log("*".repeat(10))

// // // 앞에 추가
// // arr_1.unshift("딸기")
// // console.log(arr_1)
// // console.log("*".repeat(10))

// // // 앞에 삭제
// // arr_1.shift()
// // console.log(arr_1)
// // console.log("*".repeat(10))

// // // forEach (enumerate와 비슷)
// // arr.forEach(function(item, index){
// //     console.log(item, index)
// // })

// // console.log("*".repeat(20))

// // let vegetables = ['양배추', '순무', '무', '당근']

// // let pos = 0
// // let n = 2

// // //해당 항목 제거 - pos: 시작 위치, n: 개수
// // let remove_vege = vegetables.splice(pos, n)
// // console.log(remove_vege)
// // console.log(vegetables)

// // console.log("*".repeat(20))
// // console.log("*".repeat(20))

// // // 얕은 복사
// // let vegetables_copy = vegetables
// // vegetables[0] = "토끼"
// // console.log(vegetables)
// // console.log(vegetables_copy)
// // vegetables[0] = "순무"

// // // 깊은 복사 (slice 활용)
// // vegetables_copy = vegetables.slice()
// // vegetables[0] = "토끼"
// // console.log(vegetables)
// // console.log(vegetables_copy)

// // 문자열
// // let arr = ["hi", "my", "name"]
// // let arr_join = arr.join(' ')
// // let arr_split = arr_join.split(' ')

// // console.log(arr_join)
// // console.log(arr_split)
// // for (var a of arr_split){
// //     console.log(a)
// // }

// // forEach()

// // console.log(int_array)
// array = ['one', 'two', 'three', 'four']
// int_array = [-0,-1,-2,-3]
// int_array = [0,1,2,3]
// hash = []
// map_t = new Map()

// // array.forEach((entry, index) => hash[entry]=index)
// join_array = int_array.join('')
// split_array = join_array.split('')
// // for (var i of string_array){
// //     hash.push(i)
// // }

// // array.forEach(function(item, index){
// //     map_t.set(item, index)
// // })

// // console.log(map_t.get('one '))
// console.log(typeof join_array)
// console.log(typeof split_array)


// N = 2
// let st_N = N.toString()
// arr = [0, 1, 2, 3]

// console.log(st_N)
// console.log(String(N))
// console.log(arr.map(x => String(x))) 

// // // array로도 hashmap 이용가능
// // function solution(participant, completion) {
// //     let hashed = []
// //     for(var parti of participant){
// //         if (hashed[parti]){
// //             hashed[parti]++
// //         }
// //         else{
// //             hashed[parti] = 1
// //         }
// //     }
// //     // participant.forEach(entry => {
// //     //     hashed[entry] = hashed[entry] ? hashed[entry] + 1 : 1        
// //     // })
// //     completion.forEach(entry => {
// //         hashed[entry] = hashed[entry] - 1
// //     })

// //     for (var key in hashed) {
// //         if (hashed[key] >= 1) return key
// //     }
// // }

// // console.log(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
// // console.log()


a = [['e', 101], ['b', 99], ['c', 101], ['a', 99]]

a.sort(function(a, b){
    if (a[1] > b[1]){
        return -1
    }
    if (a[1] === b[1]){
        if (a[0] < b[0]){
            return -1
        }
    }
})
console.log(a)