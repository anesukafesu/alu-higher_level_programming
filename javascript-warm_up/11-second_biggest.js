#!/usr/bin/node

const nums = process.argv.slice(2).map(n => Number(n));

if (nums.length === 0 || nums.length === 1) {
  console.log(0);
} else {
  let biggestNum = Math.max(nums[0], nums[1]);
  let secondBiggestNum = Math.min(nums[0], nums[1]);

  for (let i = 2; i < nums.length; i++) {
    if (nums[i] > biggestNum) {
      // Bigger than the biggest number so far
      // Which means it's bigger than the second biggest as well
      // So we replace both
      secondBiggestNum = biggestNum;
      biggestNum = nums[i];
    } else if (nums[i] > secondBiggestNum) {
      // Not bigger than the biggest number
      // But bigger than the second biggest
      // So we replace just the second biggest
      secondBiggestNum = nums[i];
    }
  }

  console.log(secondBiggestNum);
}
