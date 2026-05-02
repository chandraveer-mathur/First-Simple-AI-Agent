from datetime import datetime


def calculator(expression: str) -> str:
    # Evaluates a mathematical expression and returns the result as a string.
    try:
        # WARNING: eval is unsafe in production, but fine for learning
        result = eval(expression)
        return str(result)
    except Exception:
        return "Error: invalid expression"


def get_date(_: str = "") -> str:
    # Returns the current date as a string.
    # Input is ignored but kept for consistency.
    try:
        today = datetime.now().date()
        return str(today)
    except Exception:
        return "Error: could not get date"


# Tool registry
TOOLS = {
    "calculator": calculator,
    "date": get_date
}