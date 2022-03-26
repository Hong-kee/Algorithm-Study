let count = 0;
let answerArr = [];
let temp;

const solution = (n, k) => {
  let arr = Array.from({ length: n }, (v, i) => i + 1);
  while (arr.length > 0) {
    count += 1;
    temp = arr.shift();
    if (count === k) {
      answerArr.push(temp);
      count = 0;
    } else {
      arr.push(temp);
    }
  }
  console.log(`<${answerArr.join(', ')}>`);
};
//input example)
solution(7, 3);

//expected output)
//<3, 6, 2, 7, 5, 1, 4>
