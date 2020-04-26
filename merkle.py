
import hashlib

tree = ""


def hash_tree(strs):
    if len(strs) == 1:
        # root
        return strs[0]

    next_layer = []
    # hash in couples
    for i in range(0, len(strs), 2):
        print("hashing %s %s" % (strs[i], strs[i+1]))
        concat = str(strs[i]) + str(strs[i+1])
        next_layer.append(hashlib.sha256(concat.encode('utf-8')))

    print(next_layer)
    return hash_tree(next_layer)


def create_tree(leaves):
    print(hash_tree(leaves))


def create_proof_of_inclusion(leaf):
    "sdf"


def check_proof_of_inclusion(args):
    "sdf"


if __name__ == '__main__':
    inputs = input().split(" ")
    n = int(inputs[0])
    args = inputs[1:]
    print(n)
    print(args)

    if n == 1:
        # create tree for input leaves
        create_tree(args)
    elif n == 2:
        # create proof of inclusion for input leaf
        create_proof_of_inclusion(args[0])
    elif n == 3:
        # check proof of inclusion
        check_proof_of_inclusion(args)
    elif n == 4:
        "sdff"
    elif n == 5:
        "sdf"
    else:
        # illegal input
        exit()
