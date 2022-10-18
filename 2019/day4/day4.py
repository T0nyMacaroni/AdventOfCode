input = open("input", "r")

named_range = input.readline().split("-")
start_range = int(named_range[0])
end_range = int(named_range[1])

counter = 0
full_range = []
possible_passwords = []

for i in range(start_range, end_range+1):
    full_range.append(i)

for number in full_range:
    good_number = True
    double = False
    while good_number:
        for i in range(1, len(str(number))):
            snumber = str(number)
            num1 = int(snumber[i - 1])
            num2 = int(snumber[i])
            if num1 <= num2:
                good_number = True
            else:
                good_number = False
            if num1 == num2:
                double = True
    if good_number and double:
        possible_passwords.append(number)

print(len(possible_passwords))

