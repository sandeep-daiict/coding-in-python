class ListNode():
    data = 0
    next = None


class LinkedList():
    head = None

    def insert(self, val):
        new_node = ListNode()
        new_node.data = val
        if self.head is None:
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = new_node

    def print_linked_list(self):
        ptr = self.head
        count = 1
        while ptr is not None and count < 20:
            print str(ptr.data),
            if ptr.next is not None:
                print "->",
            ptr = ptr.next
            count = count + 1
        print ""

    def reverse_linked_list_recursive(self):
        node = self.reverse_linked_list_recursive_util(self.head)
        node.next = None

    def reverse_linked_list_recursive_util(self, node):
        if node is None:
            return
        if node.next is None:
            self.head = node
            return node
        temp = self.reverse_linked_list_recursive_util(node.next)
        temp.next = node
        return node

    def reverse_linked_list(self):
        if self.head is None:
            return
        prevptr = None
        ptr = self.head
        while ptr is not None:
            temp = ptr.next
            ptr.next = prevptr
            prevptr = ptr
            ptr = temp

        self.head = prevptr

    def reverse_linked_list_other(self, list_node):
        if list_node is None:
            return
        prevptr = None
        ptr = list_node
        while ptr is not None:
            temp = ptr.next
            ptr.next = prevptr
            prevptr = ptr
            ptr = temp
        return (prevptr, list_node)

    def reverse_linked_list_in_block(self, k):
        if self.head is None:
            return
        ptr = self.head
        prevptr = self.head
        t = 1
        last_end = None
        start = None
        end = None
        while ptr is not None:


            if t % k == 0:
                temp = ptr.next
                ptr.next = None
                start, end = self.reverse_linked_list_other(prevptr)

                #end.next = temp
                if last_end is None:
                    self.head = start
                else:
                    last_end.next = start
                last_end = end
                prevptr = ptr = temp
            else:

                ptr = ptr.next

            t = t + 1

        start, end = self.reverse_linked_list_other(prevptr)
        if last_end is None:
            self.head = start
        else:
            last_end.next = start

def main():
    ll = LinkedList()
    for i in range(10):
        ll.insert(i)
    ll.print_linked_list()
    ll.reverse_linked_list_recursive()
    ll.print_linked_list()
    #ll.reverse_linked_list_in_block(9)
    #ll.print_linked_list()


if __name__ == '__main__':
    main()
