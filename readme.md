# Atividade a_* em python - Vitor Braga Estevam - 414571

O algoritmo de a* usado pode ser encontrado no arquivo a_star.py

# Funcionamento

O algoritimo recebe uma tabela e duas coordenadas referentes ao ponto de inicio e destino

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

A função retorna as coordenadas referentes ao caminho a ser seguido.

A função a seguir desenha o path na tabela passo a passo para podermos analisar o funcionamento.

``` python
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
```

# Funcionamento 
0 = vazio / 1 = parede / 2 = caminho / 3 = inicio/objetivo

<table>
<td>

```bash
step 1
[3, 0, 1, 3]
[0, 0, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 0]

step 2      
[2, 0, 1, 3]
[0, 0, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 0]

step 3
[2, 0, 1, 3]
[0, 2, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 0]

step 4
[2, 0, 1, 3]
[0, 2, 1, 0]
[0, 2, 1, 0]
[0, 0, 0, 0]
```

</td>
<td>

```bash
step 5
[2, 0, 1, 3]
[0, 2, 1, 0]
[0, 2, 1, 0]
[0, 0, 2, 0]

step 6
[2, 0, 1, 3]
[0, 2, 1, 0]
[0, 2, 1, 2]
[0, 0, 2, 0]

step 7
[2, 0, 1, 3]
[0, 2, 1, 2]
[0, 2, 1, 2]
[0, 0, 2, 0]

step 8
[2, 0, 1, 2]
[0, 2, 1, 2]
[0, 2, 1, 2]
[0, 0, 2, 0]
```

</td>
</tr>
</table>
