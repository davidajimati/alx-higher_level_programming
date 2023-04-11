#!/usr/bin/node
const args = process.argv.slice(2);

if (!args[0] | Number(args[0]) === 1) {
  console.log(0);
} else {
  const myArr = args.map((i) => Number(i));
  let ans = 0;
  for (let i = 0; i < myArr.length; i++) {
    if (myArr[i] !== Math.max(...myArr) & myArr[i] > ans) {
      ans = myArr[i];
    }
  }
  console.log(ans);
}
