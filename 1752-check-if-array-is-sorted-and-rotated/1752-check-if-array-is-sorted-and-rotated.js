/**
 * @param {number[]} nums
 * @return {boolean}
 */
var check = function(nums) {
  let counter =0
let flag = true
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > nums[(i + 1)%nums.length] ) { // %nums.length checks return 0 i == nums.length that means it checks first and last element
      counter++

      
    }
      

  }
  return counter<=1
};