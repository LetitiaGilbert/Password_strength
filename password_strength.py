import re

def check_password_strength(password):
    feedback = []
    score = 0

    # Criteria
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r"[A-Z]", password) is not None
    lower_criteria = re.search(r"[a-z]", password) is not None
    digit_criteria = re.search(r"\d", password) is not None
    special_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Scoring
    if length_criteria:
        score += 1
    else:
        feedback.append(" Password should be at least 8 characters long.")

    if upper_criteria:
        score += 1
    else:
        feedback.append(" Add at least one uppercase letter.")

    if lower_criteria:
        score += 1
    else:
        feedback.append(" Add at least one lowercase letter.")

    if digit_criteria:
        score += 1
    else:
        feedback.append(" Include at least one number.")

    if special_criteria:
        score += 1
    else:
        feedback.append(" Use at least one special character (!@#$, etc.).")

    # Strength levels
    if score == 5:
        strength = " Strong Password"
    else:
        strength = " Weak Password"

    # Output
    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions to improve:")
        for item in feedback:
            print(item)

# Example usage
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    check_password_strength(user_password)
