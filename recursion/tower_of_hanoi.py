def move(n, fromm, to, buf):
    # Move a tower of height-1 to an intermediate pole, using the final pole.
    # Move the remaining disk to the final pole.
    # Move the tower of height-1 from the intermediate pole to the final pole using the original pole.
    if n == 0:  # Base case: no disk to move
        return
    move(n - 1, fromm, buf, to)
    to.append(fromm.pop())
    move(n - 1, buf, to, fromm)
