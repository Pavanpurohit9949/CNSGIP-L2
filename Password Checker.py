import re

def password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    
    # Check for digits
    if re.search(r'[0-9]', password):
        score += 1
    
    # Check for special characters
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1

    return score

def main():
    password = input("Enter your password: ")
    strength = password_strength(password)

    if strength == 5:
        print("Very Strong")
    elif strength >= 3:
        print("Strong")
    elif strength >= 2:
        print("Moderate")
    elif strength >= 1:
        print("Weak")
    else:
        print("Very Weak")

if __name__ == "__main__":
    main()
