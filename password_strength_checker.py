# KH, period 2, password checker 

# Ask the user for a password
password = input("Enter a password: ")

validity = True
# Start score at 0
score = 0

# Check if password is at least 8 characters
# print yes or no and print yes if valid and add point
def length_check(password):
    if len(password) >= 8:
        print("Length (8+ characters): Yes") # print yes or no 
        return 1 # add point if yes
    else:
        print("Length (8+ characters): No") # print yes or no
        return 0

score += length_check(password)

# Check for uppercase letters
# print yes or no and print yes if valid and add point
# do variable equals flase for every thing
# do if for everything
def uppercase_check(password):
    upper = False
    for letter in password:
        if letter >= 'A' and letter <= 'Z':
            upper = True
    if upper:
        print("Contains uppercase: Yes") # print yes or no 
        return 1
    else:
        print("Contains uppercase: No")
        return 0
# Check for lowercase letters
# print yes or no and print yes if valid and add point
def lowercase_check(password):
    lower = False
    for letter in password:
        if letter >= 'a' and letter <= 'z':
            lower = True
    if lower:
        print("Contains lowercase: Yes")
        return 1
    else:
        print("Contains lowercase: No")
        return 0

# Check for numbers
# print yes or no and print yes if valid and add point
def number_check(password):
    has_number = False
    for letter in password:
        if letter >= '0' and letter <= '9':
            has_number = True
    if has_number:
        print("Contains numbers: Yes")
        return 1
    else:
        print("Contains numbers: No")
        return 0

# Check for special characters
# print yes or no and print yes if valid and add point
def special_check(password):
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    has_special = False
    for letter in password:
        if letter in special:
            has_special = True
    return 1 if has_special else 0
if special_check(password) == 1:
    print("Contains special characters: Yes")
    score += 1
else:
    print("Contains special characters: No")

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
