/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let arraySum =0
    for(let i=0 ;i<nums.length;i++){
        arraySum =arraySum+ nums[i]
    }
 
 return (nums.length*(nums.length+1)/2)-arraySum   
};