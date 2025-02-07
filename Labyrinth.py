import random
import os
import keyboard

def generate_maze(width, height):
    directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
    wall = "|"
    path = " "
    maze = [[wall for _ in range(width)] for _ in range(height)]
    start_x = random.randrange(1, height, 2)
    start_y = random.randrange(1, width, 2)
    maze[start_x][start_y] = path
    frontier = []
    for dx, dy in directions:
        nx, ny = start_x + dx, start_y + dy
        if 1 <= nx < height - 1 and 1 <= ny < width - 1:
            frontier.append((nx, ny, start_x, start_y))
    while frontier:
        index = random.randint(0, len(frontier) - 1)
        new_x, new_y, from_x, from_y = frontier.pop(index)
        if maze[new_x][new_y] == wall:
            maze[(new_x + from_x) // 2][(new_y + from_y) // 2] = path
            maze[new_x][new_y] = path
            for dx, dy in directions:
                nx, ny = new_x + dx, new_y + dy
                if 1 <= nx < height - 1 and 1 <= ny < width - 1:
                    frontier.append((nx, ny, new_x, new_y))
    return maze

def display_playground(maze):
    for i in maze:
        print("".join(i))

def place_gameobject(maze, width, height):
    random_x, random_y = random.randrange(1, height, 2), random.randrange(1, width, 2)
    while maze[random_x][random_y] != " ":
        random_x, random_y = random.randrange(1, height, 2), random.randrange(1, width, 2)
    return random_x, random_y

def move_player(direction_x, direction_y):
    global player_x, player_y, maze
    if maze[player_x + direction_x][player_y + direction_y] != "|":
        maze[player_x][player_y] = " "
        player_x += direction_x
        player_y += direction_y
        maze[player_x][player_y] = "@"

def check_win():
    global player_x, player_y, door_x, door_y, win
    if player_x == door_x and player_y == door_y:
        win = True

def choose_difficulty():
    while True:
        try:
            difficulty = int(input("Выберите уровень сложности (1 - Легкий, 2 - Средний, 3 - Сложный): "))
            if difficulty == 1:
                return 19, 7
            elif difficulty == 2:
                return 61, 7
            elif difficulty == 3:
                return 81, 7 
            else:
                print("Введите число от 1 до 3.")
        except ValueError:
            print("Некорректный ввод. Введите число от 1 до 3.")

def main():
    global player_x, player_y, door_x, door_y, maze, win
    while True:
        width, height = choose_difficulty()
        player = "@"
        exit_door = "E"
        win = False
        maze = generate_maze(width, height)
        player_x, player_y = place_gameobject(maze, width, height)
        door_x, door_y = place_gameobject(maze, width, height)
        maze[door_x][door_y] = "E"
        keyboard.add_hotkey("w", lambda: move_player(-1, 0))
        keyboard.add_hotkey("a", lambda: move_player(0, -1))
        keyboard.add_hotkey("s", lambda: move_player(1, 0))
        keyboard.add_hotkey("d", lambda: move_player(0, 1))
        while not win:
            os.system('cls' if os.name == 'nt' else 'clear')
            maze[player_x][player_y] = "@"
            display_playground(maze)
            check_win()
        print("Поздравляем! Вы дошли до конца лабиринта!")
        again = input("Хотите сыграть снова? (y/n): ").strip().lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
12
