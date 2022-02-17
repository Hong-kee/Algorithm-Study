//input exapmle
const s = [
  '4',
  '1 2 3 4 5 6 7 8 9 1000',
  '338 304 619 95 343 496 489 116 98 127',
  '931 240 986 894 826 640 965 833 136 138',
  '940 955 364 188 133 254 501 122 768 408',
];

const solution = (S) => {
  const count = Number(S[0]);
  for (let i = 1; i <= count; i++) {
    const arr = S[i].split(' ').map((el) => Number(el));
    const answer = arr.sort((a, b) => b - a)[2];
    console.log(answer);
  }
};

solution(s);

//expected output
//8
//489
//931
//768
