from a_star import *

def draw_table(_table):
    for row in _table:
        print(row)

def update_table_by_path(_path,_table):
    for coords in _path:
        _table[coords[0]][coords[1]] = 2

def update_table_step_by_step(_path,_table):
    i=1
    for coords in _path:
        print(f"step {i}")
        draw_table(_table)
        _table[coords[0]][coords[1]] = 2
        i+=1
        print("")

    print(f"step {i}")
    draw_table(_table)

def main():

    maze = [[0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]]

    start = (0, 0)
    end = (0, 3)

    path = astar(maze, start, end)

    maze[start[0]][start[1]] = 3
    maze[end[0]][end[1]] = 3
    
    update_table_step_by_step(path, maze)

if __name__ == '__main__':
    main()