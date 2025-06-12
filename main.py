def flood_fill_recursive(grid, r, c, target_value, fill_color, n_rows, n_cols):
    if r < 0 or r >= n_rows or c < 0 or c >= n_cols:
        return
    if grid[r][c] != target_value:
        return

    grid[r][c] = fill_color

    flood_fill_recursive(grid, r + 1, c, target_value, fill_color, n_rows, n_cols)
    flood_fill_recursive(grid, r - 1, c, target_value, fill_color, n_rows, n_cols)
    flood_fill_recursive(grid, r, c + 1, target_value, fill_color, n_rows, n_cols)
    flood_fill_recursive(grid, r, c - 1, target_value, fill_color, n_rows, n_cols)

def map_terrain(grid, start_x, start_y):
    n_rows = len(grid)
    if n_rows == 0:
        return []
    n_cols = len(grid[0])

    current_color = 2

    if grid[start_x][start_y] == 0:
        print(f"Iniciando o primeiro preenchimento da região a partir de ({start_x}, {start_y}) com a cor {current_color}...")
        flood_fill_recursive(grid, start_x, start_y, 0, current_color, n_rows, n_cols)
        current_color += 1
    else:
        print(f"A célula inicial ({start_x}, {start_y}) não é navegável (valor {grid[start_x][start_y]}). Não foi possível iniciar o preenchimento a partir dela.")

    print("\nProcurando e preenchendo as próximas regiões navegáveis...")
    for r in range(n_rows):
        for c in range(n_cols):
            if grid[r][c] == 0:
                print(f"Encontrada nova região navegável em ({r}, {c}). Preenchendo com a cor {current_color}...")
                flood_fill_recursive(grid, r, c, 0, current_color, n_rows, n_cols)
                current_color += 1

    print("\nMapeamento concluído!")
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    grid1 = [
        [0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start_x1, start_y1 = 0, 0

    print("--- Exemplo 1: Grid inicial ---")
    print_grid(grid1)
    print(f"Iniciando preenchimento a partir de ({start_x1}, {start_y1})\n")

    mapped_grid1 = map_terrain(grid1, start_x1, start_y1)
    print("\n--- Exemplo 1: Grid Mapeado Final ---")
    print_grid(mapped_grid1)
    print("-" * 30)

    grid2 = [
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    start_x2, start_y2 = 0, 0

    print("\n--- Exemplo 2: Grid inicial ---")
    print_grid(grid2)
    print(f"Iniciando preenchimento a partir de ({start_x2}, {start_y2})\n")

    mapped_grid2 = map_terrain(grid2, start_x2, start_y2)
    print("\n--- Exemplo 2: Grid Mapeado Final ---")
    print_grid(mapped_grid2)
    print("-" * 30)

    grid3 = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    start_x3, start_y3 = 0, 0

    print("\n--- Exemplo 3: Grid inicial ---")
    print_grid(grid3)
    print(f"Tentando iniciar preenchimento a partir de ({start_x3}, {start_y3})\n")

    mapped_grid3 = map_terrain(grid3, start_x3, start_y3)
    print("\n--- Exemplo 3: Grid Mapeado Final ---")
    print_grid(mapped_grid3)
    print("-" * 30)