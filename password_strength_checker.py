# KH, period 2, password checker 

# Ask the user for a password
password = input("Enter a password: ")

validity = True
# Start score at 0
score = 0

# Check if password is at least 8 characters
# print yes or no and print yes if valid and add point
if len(password) >= 8:
    print("Length (8+ characters): Yes") # print yes or no 
    score += 1 # add point if yes
else:
    print("Length (8+ characters): No") # print yes or no

# Check for uppercase letters
# print yes or no and print yes if valid and add point
# do variable equals flase for every thing
# do if for everything
upper = False
for letter in password:
    if letter >= 'A' and letter <= 'Z':
        upper = True
if upper:
    print("Contains uppercase: Yes") # print yes or no 
    score += 1
else:
    print("Contains uppercase: No")

# Check for lowercase letters
# print yes or no and print yes if valid and add point

lower = False
for letter in password:
    if letter >= 'a' and letter <= 'z':
        lower = True
if lower:
    print("Contains lowercase: Yes")
    score += 1
else:
    print("Contains lowercase: No")

# Check for numbers
# print yes or no and print yes if valid and add point

has_number = False
for letter in password:
    if letter >= '0' and letter <= '9':
        has_number = True
if has_number:
    print("Contains numbers: Yes")
    score += 1
else:
    print("Contains numbers: No")

# Check for special characters
# print yes or no and print yes if valid and add point

special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
has_special = False
for letter in password:
    if letter in special:
        has_special = True
if has_special:
    print("Contains special characters: Yes")
    score += 1
else:
    print("Contains special characters: No")

# Show score
print("-------------------------------")
print("Strength score:", score, "/ 5")

# Give feedback
if score <= 2:
    print("Password strength: Weak")
    vallidity = False
elif score == 3:
    print("Password strength: Moderate")
    validity = False
elif score == 4:
    print("Password strength: Strong")
    validity = True
elif score == 5:
    print("Password strength: Very Strong")
    validity = True