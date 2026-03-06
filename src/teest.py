
def passsword_tester():
    password = input("Enter a password: ")
    score = 0
    
    
    if len(password) >= 8:
        print("Length (8+ characters): Yes") # print yes or no 
        score += 1 # add point if yes
    else:
        print("Length (8+ characters): No") # print yes or no
    upper = False
    for letter in password:
        if letter >= 'A' and letter <= 'Z':
            upper = True
    if upper:
        print("Contains uppercase: Yes") # print yes or no 
        score += 1
    else:
        print("Contains uppercase: No")
    lower = False
    for letter in password:
        if letter >= 'a' and letter <= 'z':
            lower = True
    if lower:
        print("Contains lowercase: Yes")
        score += 1
    else:
        print("Contains lowercase: No")
    has_number = False
    for letter in password:
        if letter >= '0' and letter <= '9':
            has_number = True
    if has_number:
        print("Contains numbers: Yes")
        score += 1
    else:
        print("Contains numbers: No")
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
    
    print("Strength score:", score, "/ 5")
    
    if score <= 2:
        print("Password strength: Weak")
    elif score == 3:
        print("Password strength: Moderate")
    elif score == 4:
        print("Password strength: Strong")
    elif score == 5:
        print("Password strength: Very Strong")