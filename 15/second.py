from tools import scan 


# List of all positive and negative boundary lines: x-y=a and x+y=a respectively
pos_lines = []
neg_lines = []

# Determine manhattan boundary equations of each of the sensors
for ((sx, sy), (bx, by)) in scan:

    d = abs(sx - bx) + abs(sy - by)

    #         positive boundaries                    negative boundaries
    #                  ╱                                      ╲
    # x-y=sx-sy-d  -> ╱ ╲                                    ╱ ╲ <-  x-y=sx-sy+d
    #                ╱   ╲                                  ╱   ╲
    #               .  S  .                                .  S  .
    #                ╲   ╱                                  ╲   ╱
    #                 ╲ ╱ <-  x-y=sx-sy+d    x+y=sx+sy-d  -> ╲ ╱ 
    #                  ╱                                      ╲
    pos_lines.extend([sx - sy + d, sx - sy - d])
    neg_lines.extend([sx + sy + d, sx + sy - d])

# Find pairs of postive and negative lines that are 2 manhattan away
#  ╲   ╲         ╱   ╱
#   ╲   ╲       ╱   ╱ 
#    ╲   ╲     ╱   ╱  
#     ╲   ╲   ╱   ╱   
#      < 2 >  < 2 >   
pos_pair = None
neg_pair = None
N = len(scan)

for i in range(2 * N):
    for j in range(i + 1, 2 * N):

        # if pos_pair is not None and neg_pair is not None:
        #     break

        p1, p2 = pos_lines[i], pos_lines[j]
        if abs(p1 - p2) == 2:
            pos_pair = (p1, p2)

        n1, n2 = neg_lines[i], neg_lines[j]
        if abs(n1 - n2) == 2:
            neg_pair = (n1, n2)

# The beacon we are looking for is in the middle
#      ╲   ╳   ╱    
#       ╲ ╱ ╲ ╱     
#        ╳ . ╳ <- Beacon   
#       ╱ ╲ ╱ ╲     
#      ╱   ╳   ╲    
#  pos_pair  neg_pair
# Find the two lines that contain beacon
c1 = min(pos_pair) + 1
c2 = min(neg_pair) + 1

# Now solve the two linear equations x-y=c1 and x+y=c2
# This will give x and y co-ordinates of beacon
x = (c1 + c2) // 2
y = (c2 - c1) // 2

ans = x * 4000000 + y
print(ans)
