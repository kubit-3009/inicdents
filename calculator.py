"""A small command-line calculator for learning Python basics."""


def calculate(first_number, operator, second_number):
    """Return the result of applying operator to two numbers."""
    if operator == "+":
        return first_number + second_number
    if operator == "-":
        return first_number - second_number
    if operator == "*":
        return first_number * second_number
    if operator == "/":
        if second_number == 0:
            raise ValueError("Cannot divide by zero.")
        return first_number / second_number
    raise ValueError("Use one of these operators: +, -, *, /")


def main():
    print("Simple Calculator")
    print("Type 'q' at any prompt to quit.")

    while True:
        first_input = input("First number: ").strip()
        if first_input.lower() == "q":
            break

        operator = input("Operator (+, -, *, /): ").strip()
        if operator.lower() == "q":
            break

        second_input = input("Second number: ").strip()
        if second_input.lower() == "q":
            break

        try:
            first_number = float(first_input)
            second_number = float(second_input)
            result = calculate(first_number, operator, second_number)
            print(f"Result: {result:g}\n")
        except ValueError as error:
            print(f"Error: {error}\n")


if __name__ == "__main__":
    main()
