class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null

    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

function lcaDeepestLeaves(root: TreeNode | null): TreeNode | null {
    return helper(root, 0)[0];
}

function helper(root: TreeNode | null, depth: number): [TreeNode, number] {
    if (root.left == null && root.right == null) {
        return [root, depth];
    }

    let leftNode: [TreeNode, number] = null
    let rightNode: [TreeNode, number] = null

    if (root.left != null) {
        leftNode = helper(root.left, depth + 1)
    }

    if (root.right != null) {
        rightNode = helper(root.right, depth + 1)
    }

    if (leftNode == null) {
        return rightNode;
    }

    if (rightNode == null) {
        return leftNode;
    }

    if (leftNode[1] > rightNode[1]) {
        return leftNode;
    } else if (leftNode[1] < rightNode[1]) {
        return rightNode;
    } else {
        return [root, leftNode[1]]
    }
}