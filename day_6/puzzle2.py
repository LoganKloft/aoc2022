import os

answer = -1
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")) as puzzleInput:
    marker_set = set()
    markers = puzzleInput.readline().strip()
    start_of_message_size = 14
    left_edge = 0
    right_edge = 0

    while right_edge < len(markers):
        if markers[right_edge] in marker_set:
            while markers[left_edge] != markers[right_edge]:
                marker_set.remove(markers[left_edge])
                left_edge += 1
            left_edge += 1
        else:
            marker_set.add(markers[right_edge])
        
        if len(marker_set) == start_of_message_size:
            answer = right_edge + 1
            break

        right_edge += 1

print(answer)