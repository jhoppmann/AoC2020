with open('input.txt') as file:
    input_content = file.read().splitlines()

values = [x.split(' ', 1) for x in input_content]

correct_passwords = 0

for password_info in values:
    positions = [int(x) for x in password_info[0].split('-')]
    character = password_info[1].split(':')[0]
    password = password_info[1].split(':')[1].strip()

    print(character, password, positions, positions[0]-1, positions[1]-1)
    if (password[positions[0]-1] == character) ^ (password[positions[1]-1] == character):
        correct_passwords += 1

print(correct_passwords)
