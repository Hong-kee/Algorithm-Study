const input = '<int><max>2147483647<long long><max>9223372036854775807';

const solution = (input) => {
  const stringArr = input.split('');
  let tempArr = [];
  const answerArr = [];
  let index = 0;

  while (index < stringArr.length) {
    if (stringArr[index] === '<') {
      tempArr.push(stringArr[index]);
      while (stringArr[index] !== '>') {
        index++;
        tempArr.push(stringArr[index]);
      }
      answerArr.push(tempArr.join(''));
      tempArr = [];
      index++;
    } else {
      tempArr.push(stringArr[index]);
      index++;
      if (
        stringArr[index] === ' ' ||
        stringArr[index] === '<' ||
        index === stringArr.length
      ) {
        if (stringArr[index] === ' ') {
          answerArr.push(tempArr.reverse().join(''));
          answerArr.push(' ');
          tempArr = [];
          index++;
        } else if (stringArr[index] === '<' || index === stringArr.length) {
          answerArr.push(tempArr.reverse().join(''));
          tempArr = [];
        }
      }
    }
  }
  console.log(answerArr.join('').trim());
};

solution(input);
