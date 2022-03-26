//input example
const _input = [
  '5 76',
  '5 4',
  '36 25 1 36 36',
  '4 4',
  '30 24 25 20',
  '6 4',
  '36 36 36 36 36 36',
  '2 4',
  '3 7',
  '5 4',
  '27 15 26 8 14',
];

const solution = (input) => {
  const forSortArr = [];
  let answer = 0;
  const classNum = Number(input[0].split(' ')[0]);
  let myPoint = Number(input[0].split(' ')[1]);

  input.shift();
  for (let i = 0; i < classNum * 2; i += 2) {
    const hopeStudent = Number(input[i].split(' ')[0]);
    const validStudent = Number(input[i].split(' ')[1]);
    const pointList = input[i + 1]
      .split(' ')
      .map((el) => Number(el))
      .sort((a, b) => a - b);
    if (hopeStudent < validStudent) {
      forSortArr.push(1);
    } else if (hopeStudent === validStudent) {
      forSortArr.push(pointList[0]);
    } else if (hopeStudent > validStudent) {
      const gap = hopeStudent - validStudent;
      forSortArr.push(pointList[gap]);
    }
  }

  const sortArr = forSortArr.sort((a, b) => a - b);
  for (let point of sortArr) {
    if (myPoint >= point) {
      myPoint -= point;
      answer += 1;
    } else {
      break;
    }
  }

  console.log(answer);
};

solution(_input);

//expect output
//4
