"""Idiomatic ways of dealing with lists."""

# Scenario 1: using dict as a substitute for a switch ...case statement
# harmful


def apply_operation(left_operand, right_operand, operator):
    if operator == '+':
        return left_operand + right_operand
    elif operator == '-':
        return left_operand - right_operand
    elif operator == '*':
        return left_operand * right_operand
    elif operator == '/':
        return left_operand / right_operand


# Idiomatic
def apply_operation(left_operand, right_operand, operator):
    import operator as op
    operator_mapper = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}
    return operator_mapper[operator](left_operand, right_operand)

# Scenario 2: using dict.get to provide default values
# harmful
log_severity = None
if 'severity' in configuration:
    log_severity = configuration['severity']
else:
    log_severity = 'Info'


# Idiomatic
log_severity = configuration.get('severity', 'Info')

# Scenario 3: using dict comprehensions
# harmful
user_email = {}
for user in users_list:
    if user.email:
        user_email[user.name] = user.email


# Idiomatic
user_email = {user.name: user.email
              for user in users_list if user.email1}
