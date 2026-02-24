# KH, period 2, password checker 

# Ask the user for a password
password = input("Enter a password: ")

validity = True
# Start score at 0
score = 0

# Check if password is at least 8 characters
# print yes or no and print yes if valid and add point
def length_check(password):
    ok = len(password) >= 8
    print(f"Length (8+ characters): {'yes' if ok else 'no'}") # print yes or no 
    return 1 if ok else 0

# Check for uppercase letters
# print yes or no and print yes if valid and add point
# do variable equals flase for every thing
# do if for everything
def uppercase_check(password):
    ok = any('A' <= letter <= 'Z' for letter in password)
    print(f"Contains uppercase: {'Yes' if ok else 'No'}")
    return 1 if ok else 0
# Check for lowercase letters
# print yes or no and print yes if valid and add point
def lowercase_check(password):
    ok = any('a' <= letter <= 'z' for letter in password)
    print(f"Contains lowercase: {'Yes' if ok else 'No'}")
    return 1 if ok else 0
# Check for numbers
# print yes or no and print yes if valid and add point
def number_check(password):
    ok = any('0' <= letter <= '9' for letter in password)
    print(f"Contains numbers: {'Yes' if ok else 'No'}")
    return 1 if ok else 0
# Check for special characters
# print yes or no and print yes if valid and add point
def special_check(password):
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    ok = any(letter in special for letter in password)
    print(f"Contains special characters: {'Yes' if ok else 'No'}")
    return 1 if ok else 0
# Show score
def calculate_score(password):
    score = 0
    score += length_check(password)
    score += uppercase_check(password)
    score += lowercase_check(password)
    score += number_check(password)
    score += special_check(password)
    return score
score = calculate_score(password)
print("Strength score:", score, "/ 5")

# Give feedback
if score <= 2:
    print("Password strength: Weak")
    validity = False
elif score == 3:
    print("Password strength: Moderate")
    validity = False
elif score == 4:
    print("Password strength: Strong")
    validity = True
elif score == 5:
    print("Password strength: Very Strong")
    validity = True
