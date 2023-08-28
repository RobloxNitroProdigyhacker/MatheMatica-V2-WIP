def parse_expression(expression):
    # Implement your parsing logic to break down the input expression

def shunting_yard(expression_tokens):
    # Implement the Shunting Yard algorithm to convert to postfix notation

def evaluate_expression(postfix_expression):
    # Implement your custom evaluation algorithm

# Example input from user
user_input = "2 + 2 * 3"

# Step 1: Parse input
expression_tokens = parse_expression(user_input)

# Step 2: Convert to postfix
postfix_expression = shunting_yard(expression_tokens)

# Step 3: Evaluate expression
result = evaluate_expression(postfix_expression)

# Step 4: Generate step-by-step explanation
explanation = []

# Display explanation and result
print("Step-by-step explanation:")
for step in explanation:
    print(step)
print("Result:", result)
