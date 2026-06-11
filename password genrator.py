import random
import string

# ── All character pools ────────────────────────────────
LETTERS  = string.ascii_letters   # a-z  A-Z
DIGITS   = string.digits          # 0-9
SYMBOLS  = string.punctuation     # !@#$% etc.

# ── Core function ──────────────────────────────────────
def generate_password(length, use_digits=True, use_symbols=True):
    """Build a password from the selected character pools."""
    pool = LETTERS
    if use_digits:
        pool += DIGITS
    if use_symbols:
        pool += SYMBOLS

    # Guarantee at least 1 char from each chosen pool
    guaranteed = [random.choice(LETTERS)]
    if use_digits:
        guaranteed.append(random.choice(DIGITS))
    if use_symbols:
        guaranteed.append(random.choice(SYMBOLS))

    # Fill the rest randomly, then shuffle everything
    rest = [random.choice(pool) for _ in range(length - len(guaranteed))]
    password_list = guaranteed + rest
    random.shuffle(password_list)

    return "".join(password_list)

# ── User input ─────────────────────────────────────────
def get_yes_no(prompt):
    """Ask a yes/no question and return True/False."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"): return True
        if answer in ("n", "no"):  return False
        print("  Please enter y or n.")

def get_length():
    """Ask for password length (8–64), with validation."""
    while True:
        try:
            n = int(input("Password length (8-64): "))
            if 8 <= n <= 64: return n
            print("  Must be between 8 and 64.")
        except ValueError:
            print("  Please enter a number.")

# ── Main loop ──────────────────────────────────────────
def main():
    print("=== Password Generator ===")
    while True:
        length      = get_length()
        use_digits  = get_yes_no("Include numbers?  (y/n): ")
        use_symbols = get_yes_no("Include symbols?  (y/n): ")

        password = generate_password(length, use_digits, use_symbols)
        print(f"\n  ✔  Your password: {password}\n")

        again = get_yes_no("Generate another? (y/n): ")
        if not again:
            print("Bye!")
            break

if __name__ == "__main__":
    main()