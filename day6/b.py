# Get the datastream from file
with open("input.txt") as file:
    data = file.read().rstrip()

def find_message_pos(data):

    marker_buffer = []
    for i in range(len(data)):
        char = data[i]
        print(marker_buffer)
        if len(marker_buffer) == 14:
            return i
        if char in marker_buffer:
            char_idx = marker_buffer.index(char)
            marker_buffer = marker_buffer[char_idx + 1:]
        marker_buffer.append(char)


print(find_message_pos(data))
            

