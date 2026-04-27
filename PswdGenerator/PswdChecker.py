def check_password(password):

    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch.isdigit():
            has_digit = True
        if not ch.isalnum() and not ch.isspace():
            has_symbol = True

    score = 0

    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1
    if len(password) >= 8:
        score += 1

    if score <= 2:
        return "Weak Password"
    elif 3 <= score <= 4:
        return "Medium Password"
    else:
        return "Strong Password"