from flask import Flask, request, jsonify, render_template
import sys, os, random, string

app = Flask(__name__)

# ── Inline versions of your modules so Flask can import them cleanly ──────────

def check_password(password: str) -> str:
    has_upper = has_lower = has_digit = has_symbol = False
    for ch in password:
        if ch.isupper():   has_upper  = True
        if ch.islower():   has_lower  = True
        if ch.isdigit():   has_digit  = True
        if not ch.isalnum() and not ch.isspace(): has_symbol = True

    score = 0
    if has_upper:          score += 1
    if has_lower:          score += 1
    if has_digit:          score += 1
    if has_symbol:         score += 1
    if len(password) >= 8: score += 1

    if score <= 2:           return "Weak"
    elif 3 <= score <= 4:    return "Medium"
    else:                    return "Strong"


def generate_password(length: int, exclude_similar: bool) -> str:
    char_pool = string.ascii_letters + string.digits + string.punctuation
    my_list   = list(char_pool)

    if exclude_similar:
        unwanted = set(['O', '0', 'l', '1'])
        my_list  = [ch for ch in my_list if ch not in unwanted]

    password = "".join(random.choice(my_list) for _ in range(length))

    # Persist to file (mirrors original behaviour)
    with open("Password_Files.txt", "a") as f:
        f.write(password + "\n")

    return password


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/check", methods=["POST"])
def api_check():
    data     = request.get_json(silent=True) or {}
    password = data.get("password", "")
    if not isinstance(password, str):
        return jsonify({"error": "Invalid input"}), 400
    strength = check_password(password)
    return jsonify({"strength": strength})


@app.route("/api/generate", methods=["POST"])
def api_generate():
    data            = request.get_json(silent=True) or {}
    length          = data.get("length", 12)
    exclude_similar = data.get("exclude_similar", False)

    try:
        length = int(length)
        if length < 8:  length = 8
        if length > 64: length = 64
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid length"}), 400

    password = generate_password(length, bool(exclude_similar))
    return jsonify({"password": password})


if __name__ == "__main__":
    app.run(debug=True, port=5000)