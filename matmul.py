import sys
import numpy as np
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix_file1", help="file containing rows of space-seperated integers")
    parser.add_argument("matrix_file2", help="file containing rows of space-seperated integers")
    args = parser.parse_args()

    matrix1 = np.loadtxt(args.matrix_file1, dtype=int)
    matrix2 = np.loadtxt(args.matrix_file2, dtype=int)

    if matrix1.shape[0] != matrix2.shape[1]:
        print("The number of rows in the first matrix must equal the number of columns in the second matrix")
        sys.exit()

    print(matrix1.dot(matrix2))

if __name__ == "__main__":
    main()
