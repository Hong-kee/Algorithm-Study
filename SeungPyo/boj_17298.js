//input example
const input = ['4', '9 5 4 8'];

const solution = (input) => {
  const arr = input[1].split(' ').map((el) => Number(el));
  const answerArr = Array.from({ length: arr.length }, (v, i) => 0);
  const numStack = [];
  let idx = 0;
  const idxStack = [];
  for (let i = 0; i < arr.length; i++) {
    while (numStack.length > 0 && arr[i] > numStack[numStack.length - 1]) {
      answerArr[idxStack[idxStack.length - 1]] = arr[i];
      numStack.pop();
      idxStack.pop();
    }

    numStack.push(arr[i]);
    idxStack.push(idx);
    idx++;
  }
  if (idxStack.length > 0) {
    for (idx of idxStack) {
      answerArr[idx] = -1;
    }
  }
  console.log(answerArr.join(' '));
};

solution(input);

//expect output
//-1 8 8 -1
