

maze = [
    "###########",
    "#S........#",
    "#.#######.#",
    "#.........#",
    "#.#######.#",
    "#.........#",
    "#.#######.#",
    "#.........E",
    "###########"
]

player_row = 1
player_col = 1

def display_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if row == player_row and col == player_col:
                print("P", end="")
            else:
                print(maze[row][col], end="")
        print()


def can_move(new_row, new_col):
    if maze[new_row][new_col] == "#":
        return False
    return True


def move_player(direction):
    global player_row, player_col

    new_row = player_row
    new_col = player_col

    if direction == "W":
        new_row -= 1
    elif direction == "S":
        new_row += 1
    elif direction == "A":
        new_col -= 1
    elif direction == "D":
        new_col += 1

    if can_move(new_row, new_col):
        player_row = new_row
        player_col = new_col
        return True
    else:
        print("You hit a wall!")
        return False


def check_win():
    if maze[player_row][player_col] == "E":
        return True
    return False


def play_game():
    while True:
        display_maze()

        print("\nW = Up | S = Down | A = Left | D = Right")

        direction = input("Enter your move: ").upper()

        if direction not in ["W", "A", "S", "D"]:
            print("Invalid move!")
            continue

        move_player(direction)

        if check_win():
            display_maze()
            print("\n🎉 Congratulations!")
            print("You escaped the maze!")
            break


play_game()