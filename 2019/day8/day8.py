input = open("input", "r")
input_data = input.readline()
width = 25
height = 6
volume = width * height
layers = []

# fill layers
for i in range(0, len(input_data) / volume):
    layer = []
    for j in range(0, volume):
        pointer = (i * volume) + j
        layer.append(input_data[pointer])
    layers.append(layer)

# calc zeros
least_zeros_layer = []
max_count = 9999999
for layer in layers:
    count = 0
    for number in layer:
        if number == '0':
            count += 1
    if count < max_count:
        max_count = count
        least_zeros_layer = layer

count1 = 0
count2 = 0
for number in least_zeros_layer:
    if number == '1':
        count1 += 1
    if number == '2':
        count2 += 1


# part 1
print(count1, count2)
print(count1 * count2)

# part 2
final_layer = []
for i in range(0, volume):
    final_layer.append('2')

for layer in layers:
    for i in range(0, len(layer)):
        if final_layer[i] == '2' and layer[i] != '2':
            final_layer[i] = layer[i]

# plot
counter = 0
for i in range(0, height):
    for j in range(0, width):
        print(final_layer[counter]),
        counter += 1
    print("")

