# A Node class is provided for you in the editor. A Node object has an integer data field, data, and a Node instance pointer,
# next , pointing to another node (i.e.: the next node in a list).A removeDuplicates function is declared in your editor, which
# takes a pointer to the head node of a linked list as a parameter. Complete removeDuplicates so that it deletes any duplicate nodes
#  from the list and returns the head of the updated list.

def removeDuplicates(self,head):
        #Write your code here
        current = head
        while current.next is not None: 
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
        return head 
