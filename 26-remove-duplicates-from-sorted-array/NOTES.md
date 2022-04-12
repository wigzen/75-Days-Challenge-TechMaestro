Given a sorted array and we need to return the length of the unique elements instead of the entire array. There is no need to delete the duplicate elements also.
​
Since, our first element is already present at index 0 (it is a unique element), we quickly run a for loop for the entire array to scan for unique elements.
If the current element and the next element are the same, then we just keep on going till we find a different element
Once we find a different element, it is inserted at index 1, because, index 0 is taken by the first unique element.
Once this is done, the same scanning is done to find out the next unique element and this element is to be inserted at index 2. This process continues until we are done with unique elements.
We use a variable (x = 1) which is incremented to the next index whenever we find a unique element and we insert this element at its corresponding index.
x = 1
for i in range(len(nums)-1):
if(nums[i]!=nums[i+1]):
nums[x] = nums[i+1]
x+=1
return(x)