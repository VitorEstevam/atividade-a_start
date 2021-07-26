from a_star import *

def draw_table(_table):
    for row in _table:
        print(row)

def update_table_by_path(_path,_table):
    for coords in _path:
        _table[coords[0]][coords[1]] = 2

def update_table_step_by_step(_path,_weights,_table):
    print("step -1")
    draw_table(_table) 
    print("")

    for i in range(len(_path)):
        coords = _path[i]
        print(f"step {i}")

        _table[coords[0]][coords[1]] = 4

        if(i>0):
            prev_coords = _path[i-1]
            _table[prev_coords[0]][prev_coords[1]] = 2
        
        draw_table(_table)
        print("node head: " + str(_weights[i]))
        print("")


def main():

    maze = [[0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]]

    start = (0, 0)
    end = (0, 3)

    astar_data= astar(maze, start, end)
    path = astar_data[0]
    weights = astar_data[1]

    maze[start[0]][start[1]] = 3
    maze[end[0]][end[1]] = 3
    
    update_table_step_by_step(path,weights, maze)

if __name__ == '__main__':
    main()