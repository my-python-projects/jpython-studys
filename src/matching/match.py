import re

class ExpressionEvaluator:
    """
        Simple mathematical expression interpreter supporting:
        +, -, *, /, ^, parentheses, and negative numbers.

        Uses:
        - Regular expressions for validation and subexpression detection.
        - Structural pattern matching (match-case) for operation handling.
    """

    def __init__(self, expression: str):
        self.original = expression.strip()
        # Normalize: remove spaces and replace ^ with ** (Python's exponent operator)
        self.expr = self.original.replace(" ", "").replace("^", "**")

    # --- Basic validation ---
    def validate(self) -> bool:
        """
            Validates that the expression only contains allowed characters.
        """
        return bool(re.fullmatch(r"[0-9+\-*/^().\s]+", self.original))


    # --- Simplify parentheses from inside out ---
    def simplify_parentheses(self) -> str | float | str:
        """
            Finds and evaluates the innermost parentheses recursively
            until there are none left.
        """
        expr = self.expr
        while "(" in expr:
            # Match the innermost parentheses content
            sub_expr = re.search(r"\([^()]+\)", expr)
            if not sub_expr:
                return "Invalid expression"

            # Extract content without parentheses
            inner = sub_expr.group()[1:-1]
            # Recursively evaluate the subexpression
            result = ExpressionEvaluator(inner).evaluate()

            if isinstance(result, str):  # Error message propagation
                return result

            # Replace the parentheses with its numeric result
            expr = expr.replace(sub_expr.group(), str(result))

        return expr

    #  Apply a single operation
    def apply_operation(self, a: float, op: str, b: float) -> float | str:
        match op:
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case '/':
                return "Error: division by zero" if b == 0 else a / b
            case '**':
                return a ** b
            case _:
                return "Invalid operator"
            

    # --- Evaluate an expression without parentheses ---
    def evaluate_flat(self, expr: str) -> float | str:

        # Operator precedence (highest to lowest)
        ops = ['**', '*', '/', '+', '-']

        # Evaluate each operation type by order of precedence
        for op in ops:
            # Regex that captures "number operator number"
            # Example:  2*3, 4.5**2, -5+3
            pattern = re.compile(rf'(-?\d+(?:\.\d+)?){re.escape(op)}(-?\d+(?:\.\d+)?)')

            # Repeatedly apply this operation type until none left
            while True:
                m = pattern.search(expr)
                if not m:
                    break

                a_str, b_str = m.groups()
                a, b = float(a_str), float(b_str)

                # Perform the operation via pattern matching
                result = self.apply_operation(a, op, b)
                if isinstance(result, str):  # If an error message
                    return result

                # Replace "a op b" with its computed result
                expr = expr[:m.start()] + str(result) + expr[m.end():]

        try:
            return float(expr)
        except ValueError:
            return "Invalid expression"


    # --- Main evaluation method ---
    def evaluate(self) -> float | str:

        if not self.validate():
            return "Invalid expression"

        simplified = self.simplify_parentheses()

        # If parentheses simplification already gave a number, return it
        if isinstance(simplified, (int, float)):
            return simplified

        # Otherwise, evaluate the remaining flat expression
        return self.evaluate_flat(str(simplified))


# --- TESTS ---
def test():
    e = ExpressionEvaluator

    print("========= TESTS =========\n")

    print(e("5 + 3").evaluate())         # 8.0
    print(e("10 - 2").evaluate())        # 8.0
    print(e("4 * 6").evaluate())         # 24.0
    print(e("8 / 2").evaluate())         # 4.0
    print(e("2 ^ 3").evaluate())         # 8.0
    print(e("10 / 0").evaluate())        # "Error: division by zero"
    print(e("abc").evaluate())           # "Invalid expression"
    print(e("5+*3").evaluate())          # "Invalid expression"
    print(e("(2+3)*4").evaluate())       # 20.0
    print(e("2^(3+1)").evaluate())       # 16.0
    print(e("-5 + 3").evaluate())        # -2.0
    print(e("(-5 + 3) * 2").evaluate())  # -4.0


if __name__ == "__main__":
    test()

    print("\n=== Simple Math Calculator ===")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter an expression: ").strip()
        if user_input.lower() == "exit":
            print("Calculator closed.")
            break

        evaluator = ExpressionEvaluator(user_input)
        result = evaluator.evaluate()
        print(f"-> Result: {result}\n")
