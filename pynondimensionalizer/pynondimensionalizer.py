from sympy import Matrix, pretty
from pandas import read_csv
import argparse


def nullspace_solve(input_file):

    D_in = read_csv(input_file, index_col=0)

    D = Matrix(D_in)
    S = D.nullspace()

    dim = D_in.index.tolist()
    var = map(str.strip, D_in.columns.tolist())

    dim_str = ' '.join(dim)
    var_str = ' '.join(var)

    output_str = 'Dimensions: ' + dim_str + '\nVariables: ' + var_str + '\n\nD = \n\n' + pretty(D) + '\n\nS = \n\n' + pretty(S) + '\n'

    return output_str


def output_write(output_file, output_str):

    with open(output_file, 'w') as file:
        file.write(output_str)


def main():

    parser = argparse.ArgumentParser('pynondimensionalizer', description='Find the nullspace of a dimensional matrix')
    parser.add_argument('--input', '-i', help='Input csv file containing the dimensional matrix', required=True)
    parser.add_argument('--output', '-o', help='Output file')

    args = parser.parse_args()

    output_str = nullspace_solve(args.input)

    if args.output:
        output_file = args.output
        output_write(output_file, output_str)

    else:
        print(output_str)


if __name__ == "__main__":
    main()
