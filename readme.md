# Atividade a_* em python - Vitor Braga Estevam - 414571

O algoritmo de a* usado pode ser encontrado no arquivo a_star.py

# Funcionamento

O algoritimo recebe uma tabela e duas coordenadas referentes ao ponto de inicio e destino. 

```python
from a_star import *
maze = [[0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]]

start = (0, 0)
end = (0, 3)

path = astar(maze, start, end)
```

Eu fiz uuma pequena modificação para receber além do caminho uma lista com os atributos do a* de cada node do caminho

```python
a_star.py
(...)
    path.append(current.position)
    weight.append({"f":current.f,"g":current.g,"h":current.h})
return [path[::-1], weight[::-1]] # Return reversed path and weight
(...)

main.py
(...)
    astar_data= astar(maze, start, end)
    path = astar_data[0]
    weights = astar_data[1]
(...)
```

A função retorna as coordenadas referentes ao caminho a ser seguido.

A função a seguir desenha o path na tabela passo a passo para podermos analisar o funcionamento.

``` python
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
```

# Funcionamento 
0 = vazio / 1 = parede / 2 = caminho / 3 = inicio/objetivo / 4 node head

<table>
<td>

```bash
step 0
[4, 0, 1, 3]
[0, 0, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 0]
node head: {'f': 0, 'g': 0, 'h': 0}

step 1
[2, 4, 1, 3]
[0, 0, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 0]
node head: {'f': 5, 'g': 1, 'h': 4}

step 2
[2, 2, 1, 3]
[0, 4, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 0]
node head: {'f': 7, 'g': 2, 'h': 5}

step 3
[2, 2, 1, 3]
[0, 2, 1, 0]
[0, 4, 1, 0]
[0, 0, 0, 0]
node head: {'f': 11, 'g': 3, 'h': 8}

step 4
[2, 2, 1, 3]
[0, 2, 1, 0]
[0, 2, 1, 0]
[0, 4, 0, 0]
node head: {'f': 17, 'g': 4, 'h': 13}
```

</td>
<td>

```bash
step 5
[2, 2, 1, 3]
[0, 2, 1, 0]
[0, 2, 1, 0]
[0, 2, 4, 0]
node head: {'f': 15, 'g': 5, 'h': 10}

step 6
[2, 2, 1, 3]
[0, 2, 1, 0]
[0, 2, 1, 0]
[0, 2, 2, 4]
node head: {'f': 15, 'g': 6, 'h': 9}

step 7
[2, 2, 1, 3]
[0, 2, 1, 0]
[0, 2, 1, 4]
[0, 2, 2, 2]
node head: {'f': 11, 'g': 7, 'h': 4}

step 8
[2, 2, 1, 3]
[0, 2, 1, 4]
[0, 2, 1, 2]
[0, 2, 2, 2]
node head: {'f': 9, 'g': 8, 'h': 1}

step 9
[2, 2, 1, 4]
[0, 2, 1, 2]
[0, 2, 1, 2]
[0, 2, 2, 2]
node head: {'f': 9, 'g': 9, 'h': 0}
```

</td>
</tr>
</table>
