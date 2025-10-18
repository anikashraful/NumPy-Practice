import numpy as np

def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Enter row {i+1} (space-separated): ").split()))
        matrix.append(row)
    return np.array(matrix)

if __name__ == '__main__':
    print('Matrix Operation menu')