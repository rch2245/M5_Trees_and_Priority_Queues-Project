"""Binary Expression Tree implementation.
"""

from stack import Stack


class TreeNode:
    """A single node in a binary expression tree.

    Leaf nodes hold operands (numeric strings); internal nodes hold one
    of the operators '+', '-', '*', '/' and have exactly two children.
    """

    def __init__(self, value, left=None, right=None):
        self.value = value  # stored as a string per the ADT
        self.left = left
        self.right = right

    def is_leaf(self):
        """Return True if this node has no children."""
        return self.left is None and self.right is None


class BinaryExpressionTree:
    """Binary expression tree built from a postfix expression string."""

    _OPERATORS = {"+", "-", "*", "/"}

    def __init__(self):
        """Create an empty expression tree (root is None)."""
        self.root = None

    #Core operations

    def is_empty(self):
        """Return True if the tree has no root node."""
        return self.root is None

    def clear_tree(self):
        """Reset the tree to empty."""
        self.root = None

    def build_from_postfix(self, postfix):
        """Build the expression tree from a whitespace-separated postfix string.
        """
        if not isinstance(postfix, str):
            raise ValueError("postfix expression must be a string")

        self.clear_tree()
        stack = Stack()
        tokens = postfix.split()

        for token in tokens:
            if self._is_number(token):
                stack.push(TreeNode(token))
            elif token in self._OPERATORS:
                node = TreeNode(token)
                if stack.is_empty():
                    raise ValueError(
                        f"Malformed postfix expression: missing right operand for '{token}'"
                    )
                node.right = stack.top()
                stack.pop()
                if stack.is_empty():
                    raise ValueError(
                        f"Malformed postfix expression: missing left operand for '{token}'"
                    )
                node.left = stack.top()
                stack.pop()
                stack.push(node)
            else:
                raise ValueError(f"Unsupported token in postfix expression: {token!r}")

        if stack.is_empty():
            raise ValueError("Empty postfix expression")

        self.root = stack.top()
        stack.pop()
        if not stack.is_empty():
            raise ValueError("Malformed postfix expression: unused operands left on stack")

    def evaluate_tree(self):
        """Recursively evaluate the expression tree and return the result."""
        if self.is_empty():
            raise ValueError("Cannot evaluate an empty expression tree")
        return self._evaluate(self.root)

    def infix_traversal(self):
        """Return an infix string representation with parentheses."""
        if self.is_empty():
            raise ValueError("Cannot traverse an empty expression tree")
        out = []
        self._inorder(self.root, out)
        return "".join(out)

    def postfix_traversal(self):
        """Return a space-separated postfix string representation."""
        if self.is_empty():
            raise ValueError("Cannot traverse an empty expression tree")
        out = []
        self._postorder(self.root, out)
        return " ".join(out)

    #  Recursive helpers

    def _inorder(self, node, out):
        """Append an infix representation of the subtree rooted at node."""
        if node is None:
            return
        if node.is_leaf():
            out.append(node.value + " ")
            return
        out.append("(")
        self._inorder(node.left, out)
        out.append(node.value + " ")
        self._inorder(node.right, out)
        out.append(")")

    def _postorder(self, node, out):
        """Append a postfix representation of the subtree rooted at node."""
        if node is None:
            return
        self._postorder(node.left, out)
        self._postorder(node.right, out)
        out.append(node.value)

    def _evaluate(self, node):
        """Recursively compute the numeric value of the subtree at node."""
        if node.is_leaf():
            return float(node.value)

        left_val = self._evaluate(node.left)
        right_val = self._evaluate(node.right)
        op = node.value

        if op == "+":
            return left_val + right_val
        if op == "-":
            return left_val - right_val
        if op == "*":
            return left_val * right_val
        if op == "/":
            if right_val == 0:
                raise ZeroDivisionError("Division by zero in expression tree")
            return left_val / right_val
        raise ValueError(f"Unsupported operator at internal node: {op!r}")

    @staticmethod
    def _is_number(token):
        """Return True if token parses as a numeric literal."""
        try:
            float(token)
            return True
        except ValueError:
            return False
