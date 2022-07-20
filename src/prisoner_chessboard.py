import numpy as np

# this is the specified target position on the board to be uncovered
# it can be any integer from 0 to 63
target_pos = np.random.randint(0, 64)

# randomize the board with 0 and 1
board = np.random.randint(0, 2, 64)

# Use Hamming code to calculate the current board error position
cur_error_pos = np.bitwise_xor.reduce(np.flatnonzero(board))

# this is the position we need to flip the coin
flip_pos = cur_error_pos ^ target_pos

# flip the coin
board[flip_pos] ^= 1

# Use Hamming code to calculate the new error position after flip, done by the second prisoner
new_error_pos = np.bitwise_xor.reduce(np.flatnonzero(board))

# the new error position should be the same as the target position
print(f'The target and predicted positions are: {target_pos} and {new_error_pos}')
assert new_error_pos == target_pos
