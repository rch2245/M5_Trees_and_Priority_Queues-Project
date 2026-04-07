"""Driver for the BinaryExpressionTree class."""

from binary_expression_tree import BinaryExpressionTree


postfix_expressions = [
    "5 3 +",
    "8 2 - 3 +",
    "5 3 8 * +",
    "6 2 / 3 +",
    "5 8 + 3 -",
    "5 3 + 8 *",
    "8 2 3 * + 6 -",
    "5 3 8 * + 2 /",
    "8 2 + 3 6 * -",
    "5 3 + 8 2 / -",
]


def main():
    print("----- Binary Expression Tree -----")
    tree = BinaryExpressionTree()
    for postfix in postfix_expressions:
        tree.build_from_postfix(postfix)
        print(f"Infix Expression:   {tree.infix_traversal()}")
        print(f"Postfix Expression: {tree.postfix_traversal()}")
        print(f"Evaluated Result:   {tree.evaluate_tree()}")


if __name__ == "__main__":
    main()
