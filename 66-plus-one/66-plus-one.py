class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number=""
        for s in digits:
            number+=str(s)
        number =str(int(number)+1)
        
        li =[]
        for c in number:
            li.append(int(c))
        return li