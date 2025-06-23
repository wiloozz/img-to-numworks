from kandinsky import *

compressed_input = ""
i = 0
current_char = ''
run_length = 0
stop = False

for x in range(320):
    for y in range(240):
        
        if stop:break
        
        while run_length == 0:
            try:
                if compressed_input[i] == '|':
                    i += 1
                    num_str = ''
                    while compressed_input[i] != '|':
                        num_str += compressed_input[i]
                        i += 1
                    i += 1  # skip closing '|'
                    current_char = '1'
                    run_length = int(num_str)
                elif compressed_input[i] == '{':
                    i += 1
                    num_str = ''
                    while compressed_input[i] != '}':
                        num_str += compressed_input[i]
                        i += 1
                    i += 1  # skip closing '}'
                    current_char = '0'
                    run_length = int(num_str)
            except IndexError:
                stop = True
                break

        run_length -= 1

        if current_char == '0':
           set_pixel(x, y, (0, 0, 0))