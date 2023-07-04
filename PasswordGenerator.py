import random
import string

# Ask user for level of security for the password
    # level easy: random letters for passwords of length 8 characters
    # level medium: password must contain at least one uppercase letter, one lowercase letter, and one number for passwords of 8 characters
    # level hard: password must contain at least one uppercase letter, one lowercase letter, one number, and one special character
        # for passwords of at least 8 characters and maximum of 16 characters
    # level ultra: password must containt at least one uppercase letter, one lowercase letter, one number, and one special character
        # for passwords of at least 16 characters and maximum of 32 characters

def password_generator_easy():
    password = "".join(random.choice(string.ascii_letters) for _ in range(8))
    return password

def password_generator_medium():
    password = [random.choice(string.ascii_uppercase), 
                random.choice(string.ascii_lowercase), 
                random.choice(string.digits)]
    while len(password) < 8:
        password.append(random.choice(string.ascii_letters + string.digits))
    random.shuffle(password)
    return "".join(password)

def password_generator_hard():
    length = random.randint(8,16)
    password = [random.choice(string.ascii_uppercase), 
                random.choice(string.ascii_lowercase), 
                random.choice(string.digits), 
                random.choice(string.punctuation)]
    while len(password) < length:
        password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
    random.shuffle(password)
    return "".join(password)

def password_generator_ultra():
    length = random.randint(16,32)
    password = [random.choice(string.ascii_uppercase), 
                random.choice(string.ascii_lowercase), 
                random.choice(string.digits), 
                random.choice(string.punctuation)]
    while len(password) < length:
        password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
    random.shuffle(password)
    return "".join(password)

# Ask user for level of security for the password
level = input("What level of security do you want for your password? (easy, medium, hard, ultra) ")
if level == "easy":
    # Generate password
    print(password_generator_easy())
elif level == "medium":
    # Generate password
    print(password_generator_medium())
elif level == "hard":
    # Generate password
    print(password_generator_hard())
elif level == "ultra":
    # Generate password
    print(password_generator_ultra())
else:
    # Invalid input
    print("Invalid input. Please try again.")
