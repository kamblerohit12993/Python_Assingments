# Password Strength Checker

password = input("Enter your password: ")

has_uppercase = False
has_lowercase = False
has_digit = False
has_special = False

for ch in password:
    if ch.isupper():
        has_uppercase = True
    elif ch.islower():
        has_lowercase = True
    elif ch.isdigit():
        has_digit = True
    elif not ch.isspace():
        has_special = True

score = 0

if len(password) >= 8:
    score += 1

if has_uppercase:
    score += 1

if has_lowercase:
    score += 1

if has_digit:
    score += 1

if has_special:
    score += 1

print("\n--- Password Analysis ---")
print("Password Length:", len(password))
print("Contains Uppercase:", has_uppercase)
print("Contains Lowercase:", has_lowercase)
print("Contains Digit:", has_digit)
print("Contains Special Character:", has_special)

if len(password) < 8:
    print("Password Strength: Weak")
elif score <= 3:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")


