# coding: utf-8

from dataclasses import dataclass


def not_negative_integer(func):
    def wrapper(self, index, *args):
        if index < 0:
            raise IndexError("index 不得小于0")
        func(self, index, *args)
    return wrapper


@dataclass
class Node:
    data: str = ""
    next: "Node" = None


class SingleLinkList:
    def __init__(self) -> None:
        self._header: Node = None
        self._length: int = 0

    def __len__(self) -> int:
        return self._length

    def is_empty(self) -> bool:
        return self._header is None

    def add(self, node: Node) -> None:
        """ 头部插入 """
        if self.is_empty():
            self._header = node
        else:
            node.next = self._header
            self._header = node
        self._length += 1

    def append(self, node: Node) -> None:
        """ 尾部插入 """
        if self.is_empty():
            self.add(node)
        else:
            current_node = self._header
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
            self._length += 1

    @not_negative_integer
    def insert(self, index: int, node: Node) -> None:
        if index > self._length:
            raise IndexError("index值太大，目前支持最大值：%d" % self._length)

        if index == 0:
            self.add(node)

        else:
            current_node = self._header
            for i in range(1, self._length):
                if index == i:
                    node.next = current_node.next
                    current_node.next = node
                    self._length += 1
                    break
                current_node = current_node.next

    def travel(self) -> None:
        nodes = []
        current_node = self._header
        for _ in range(self._length):
            nodes.append(current_node.data)
            current_node = current_node.next
        print(nodes)

    @not_negative_integer
    def delete(self, index):
        if index >= self._length:
            raise IndexError("index 的值不得大于 %d" % (self._length-1))

        if index == 0:
            self._header = self._header.next
            self._length -= 1

        else:
            current_node = self._header
            for i in range(1, self._length):
                if index == i:
                    current_node.next = current_node.next.next
                    self._length -= 1
                    break
                current_node = current_node.next


if __name__ == '__main__':
    ll = SingleLinkList()
    ll.travel()
    print(len(ll))
    ll.add(Node("a"))
    ll.travel()
    print(len(ll))
    ll.append(Node("b"))
    print(len(ll))
    for i in range(3):
        ll.append(Node(str(i)))
    ll.travel()
    print(len(ll))
    try:
        ll.insert(10, Node("xx"))
    except IndexError as e:
        print(e)

    ll.insert(2, Node("xx"))
    ll.travel()
    print(len(ll))

    ll.delete(2)
    ll.travel()
    print(len(ll))
