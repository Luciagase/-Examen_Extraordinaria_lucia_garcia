from ast import main

def dots_and_boxes_score(player1_moves, player2_moves):
    grid = [[0 for _ in range(3)] for _ in range(3)]
    player1_score = 0
    player2_score = 0
    for move in player1_moves:
        if is_valid_move(move, grid):
            grid[move[0]][move[1]] = 1
            player1_score += check_surrounding(move, grid)
    for move in player2_moves:
        if is_valid_move(move, grid):
            grid[move[0]][move[1]] = 2
            player2_score += check_surrounding(move, grid)
    return (player1_score, player2_score)


if __name__ == "__main__":
  main()