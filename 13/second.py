from tools import pairs, in_order


# Add divider packets and a new list of all individual packets
divider = ( [[2]], [[6]] )
packets = list(sum(pairs, divider))

# Sort packets
N = len(packets)
for i in range(N):

    # Find the smallest packet in the list
    smallest_idx = i
    for j in range(i+1, N):
        # Check if current packet comes before smallest
        if in_order( (packets[j], packets[smallest_idx]) ) == 1:
            smallest_idx = j

    # Swap the smallest packet
    curr = packets[i]
    packets[i] = packets[smallest_idx]
    packets[smallest_idx] = curr

decoder_key = 1
for d in divider:
    decoder_key *= packets.index(d) + 1
print(decoder_key)
