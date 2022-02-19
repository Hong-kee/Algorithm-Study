const input = ['3', '12 2', '200', '50', '300', '100'];

const solution = (input) => {
  const topingNum = Number(input[0]);
  const [doughPrice, topingPrice] = input[1].split(' ').map((el) => Number(el));
  const doughCal = Number(input[2]);
  const topingCalArr = [];
  const sortArr = [];

  for (let i = 3; i < input.length; i++) {
    topingCalArr.push(Number(input[i]));
  }
  topingCalArr.sort((a, b) => b - a);
  topingCalArr.unshift(0);

  for (let j = 0; j <= topingNum; j++) {
    let cal = doughCal;
    let price = doughPrice + topingPrice * j;
    for (let k = 0; k <= j; k++) {
      cal += topingCalArr[k];
    }
    let calPerPrice = cal / price;
    sortArr.push(calPerPrice);
  }
  sortArr.sort((a, b) => b - a);

  console.log(Math.floor(sortArr[0]));
};

solution(input);

//expect output
//37
