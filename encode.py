import parameters

with open(parameters.outputFile,"r") as file:
    text = file.read()

def compress_binary_image(binary_string):
    
    result : list = []
    if binary_string[-1] == "1":
        binary_string += "0"
    else:
        binary_string += "1"

    if binary_string[0] == "1":
        currentChar = "1"
    else:
        currentChar = "0"
        
    count = 1
        
    for bit in binary_string[1:]:
        if bit == currentChar:
            count += 1
        else:
            result.append(f"{count}|")
            count = 1
            if currentChar == "1":
                currentChar = "0"
            else:
                currentChar = "1"
                              
    if text[0] == "0":
        return "0" + ''.join(result)
    else:
        return ''.join(result)

compressed_output = compress_binary_image(text)
print(compressed_output)

with open(parameters.outputFile,"w") as file:
    file.write(compressed_output)
