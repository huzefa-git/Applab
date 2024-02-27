import string

# Get all uppercase and lowercase letters
alphabets = string.ascii_uppercase+string.ascii_lowercase

# Get all digits
digits = string.digits

for i in alphabets+digits:
    for j in alphabets+digits:
        for k in alphabets+digits:
            for l in alphabets+digits:
                print(i,j,k,l)
