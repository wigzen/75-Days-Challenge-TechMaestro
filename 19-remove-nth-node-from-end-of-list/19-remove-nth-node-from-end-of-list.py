class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = ListNode(0, head)
        curr = front = dum
        while n > 0: 
            front = front.next
            n -= 1
        while front.next != None:
            front=front.next
            curr=curr.next
            
        curr.next = curr.next.next
        
        return dum.next