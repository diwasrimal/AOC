# Get the datastream from file
with open("input.txt") as file:
    data = file.read().rstrip()

def find_marker_pos(data):

    marker_buffer = []
    for i in range(len(data)):
        char = data[i]
        # print(marker_buffer)
        if len(marker_buffer) == 4:
            return i
        if char in marker_buffer:
            char_idx = marker_buffer.index(char)
            marker_buffer = marker_buffer[char_idx + 1:]
        marker_buffer.append(char)


print(find_marker_pos(data))
            

