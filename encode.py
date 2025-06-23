import parameters

amountPass = 0

newText = ""

with open(parameters.outputFile,"r") as file:
    text = file.read()

def compress_binary_image(binary_string):
    if not binary_string:
        return ""

    result = []
    current_char = binary_string[0]
    count = 1

    for bit in binary_string[1:]:
        if bit == current_char:
            count += 1
        else:
            if current_char == '1':
                result.append(f"|{count}|")
            else:
                result.append(f"{{{count}}}")
            current_char = bit
            count = 1

    # Append the last run
    if current_char == '1':
        result.append(f"|{count}|")
    else:
        result.append(f"{{{count}}}")

    return ''.join(result)

compressed_output = compress_binary_image(text)
print(compressed_output)

with open(parameters.outputFile,"w") as file:
    file.write(compressed_output)