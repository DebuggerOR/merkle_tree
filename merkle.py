# ori fogler, 318732484, roi fogler, id 302882527

import hashlib

# DEBUG False is according submission format
DEBUG = True

"""
running examples:
1 a b c d
12a40550c10c6339bf6f271445270e49b844d6c9e8abc36b9b642be532befe94

2 1
l a r 21e721c35a5823fdb452fa2f9f0a612c74fb952e06927489c6b27a43b817bed4

3 b 12a40550c10c6339bf6f271445270e49b844d6c9e8abc36b9b642be532befe94 l a r 21e721c35a5823fdb452fa2f9f0a612c74fb952e06927489c6b27a43b817bed4
True

4 2
296 00038effdfc87247806ade69b932b51697490a9f9479ed43aef31657169e8703
"""


class merkle_tree:
    def __init__(self, tree=[], hash_func = hashlib.sha256):
        self.tree = tree
        self.hash_func = hash_func

    def display_tree(self):
        print("tree is:")
        for i in range(len(self.tree)):
            print(*self.tree[i])
        print("\n")

    def __hash_tree(self, strs):
        if len(strs) == 1:
            # root
            return strs[0]

        next_layer = []
        # hash in couples
        for i in range(0, len(strs), 2):
            if DEBUG:
                print("hashing %s and %s .." % (strs[i], strs[i+1]))
            concat = strs[i] + strs[i+1]
            next_layer.append(self.hash_func(concat.encode('utf-8')).hexdigest())

        self.tree = [next_layer] + self.tree
        return self.__hash_tree(next_layer)

    def create_tree(self, leaves):
        self.tree = [leaves]

        if DEBUG:
            print("root is: %s\n" % self.__hash_tree(leaves))
        else:
            print(self.__hash_tree(leaves))

    def __prove(self, sub_tree, node_num, proof):
        last_layer = sub_tree[len(sub_tree) - 1]

        if len(last_layer) == 1:
            # if root
            return proof

        if node_num % 2 == 0:
            # if even go right
            proof.append("r")
            proof.append(last_layer[node_num + 1])
        else:
            # if odd go left
            proof.append("l")
            proof.append(last_layer[node_num - 1])

        return self.__prove(sub_tree[:-1], round(node_num / 2), proof)

    def create_proof_of_inclusion(self, leaf_num):
        proof = self.__prove(self.tree, leaf_num, [])
        print(*proof)

    def check_proof_of_inclusion(self, leaf, root, moves):
        prev = leaf
        direction = "l"

        for i in range(len(moves)):
            if i % 2 == 0:
                direction = moves[i]
                # according format, must be r or l
                if moves[i] != "r" or moves[i] != "l":
                    exit()
            else:
                if direction == "r":
                    right = moves[i]
                    left = prev
                else:
                    right = prev
                    left = moves[i]

                if DEBUG:
                    print("hashing %s and %s .." % (left,right))
                concat = left + right
                prev = self.hash_func(concat.encode('utf-8')).hexdigest()

        if DEBUG:
            print("comparing %s and %s .." % (prev,root))
        print(prev == root)

    def hardness(self, zeroes):
        "sdf"


if __name__ == '__main__':
    tree = merkle_tree()

    while True:
        inputs = input().split(" ")
        n = int(inputs[0])
        args = inputs[1:]

        if DEBUG:
            print("cmd number: %d" % n)
            print("args are: ")
            print(*args)
            print("\n")

        if n == 1:
            # create tree by input leaves
            tree.create_tree(args)
            if DEBUG:
                tree.display_tree()
        elif n == 2:
            # create proof of inclusion for input leaf index
            tree.create_proof_of_inclusion(int(args[0]))
        elif n == 3:
            # check proof of inclusion
            tree.check_proof_of_inclusion(args[0], args[1], args[2:])
        elif n == 4:
            # ???
            tree.hardness(int(args[1]))
        elif n == 5:
            # exit
            exit()
        else:
            # illegal input
            exit()
