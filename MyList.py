#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MyNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Mylist:
    def __init__(self, head):
        self.head = head


    def add_head(self, n):
        node = MyNode(n)
        node.next = self.head
        self.head = node

    def to_string(self):
        result = '['
        node = self.head
        while node:
            result = result + str(node.value) + ','
            node = node.next
        result = result + ']'
        return result
    
    def length(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count
        
    def add_tail(self, n):
        # if the list is empty, then this is the same as add_head
        if not self.head:
            self.add_head(n)
            return

        # first find the last Node in the list
        last = None
        node = self.head
        while node:
            # if head.next is None, then head is the last one
            if not node.next:
                last = node
                break
            else:
                node = node.next
        node = MyNode(n)
        last.next = node

    def get(self, i):
        # return the value the ith node in the list
        # if i is not a valid index( <0 or >=length), then return None
        pass
    
    def find(self, n):
        # return the idex of n in the list if found, otherwise return -1
        pass

    def remove(self, i):
        # remove the ith node in the list,
        # return True if the remove is sussesful, othereise return False
        pass

    
# Test code:
list1 = Mylist(None)
list1.add_head(2)
list1.add_head(3)
list1.add_head(100)
list1.add_tail(9)
print(list1.to_string())
# get [3, 2, 100]
print(list1.length())
