#!/usr/bin/python
# coding:utf-8
# @software: PyCharm
# @file: 二叉树.py
# @time: 2019/12/9


class BinaryTree(object):
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root(self, obj):
        self.key = obj

    def get_root(self):
        return self.key

    # 树的前序遍历
    def pre_order(self):
        print(self.key)

        if self.left_child:
            self.left_child.pre_order()

        if self.right_child:
            self.right_child.pre_order()

    # 树的中序遍历

    # 树的后续遍历


'''
以下为测试数据, 去掉 # 即可
'''
r = BinaryTree('a')
print(r.get_root())
print(r.get_left_child())
r.insert_left('b')
print(r.get_left_child())
print(r.get_left_child().get_root())
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_root())
r.get_right_child().set_root('hello')
print(r.get_right_child().get_root())

r.pre_order()
