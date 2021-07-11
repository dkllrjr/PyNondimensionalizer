##############################################################################
#           By
#                  ___                  _  __    _ _
#                 |   \ ___ _  _ __ _  | |/ /___| | |___ _ _
#                 | |) / _ \ || / _` | | ' </ -_) | / -_) '_|
#                 |___/\___/\_,_\__, | |_|\_\___|_|_\___|_|
#                               |___/
#                 
#           Please follow the licensing this work is under! Cheers!
##############################################################################

__docformat__ = "numpy"

from sympy import Matrix, pretty
from pandas import read_csv
from pathlib import Path
import argparse

##############################################################################

def nullspace_solve(input_file):
    """Solves for the nullspace matrix, with the given dimensions matrix.

    Parameters
    ----------
    input_file : str
        Path to the input file with the dimensions matrix.

    Returns
    -------
    output_str : str
        String that contains the nullspace matrix, with headers.
    """

    D_in = read_csv(Path(input_file), index_col=0)

    D = Matrix(D_in)
    S = D.nullspace()

    dim = D_in.index.tolist()
    var = map(str.strip, D_in.columns.tolist())

    dim_str = ' '.join(dim)
    var_str = ' '.join(var)

    output_str = 'Dimensions: ' + dim_str + '\nVariables: ' + var_str + '\n\nD = \n\n' + pretty(D) + '\n\nS = \n\n' + pretty(S) + '\n'

    return output_str


def output_write(output_str, output_file):
    """Writes the nullspace matrix to the output file.

    Parameters
    ----------
    output_file : str
        Path to the output file.
    output_str : str
        String containing the nullspace matrix.
    """

    with open(Path(output_file), 'w') as file:
        file.write(output_str)


def main():
    """Argument parser for the command line.
    """

    parser = argparse.ArgumentParser('pynondim', description='Find the nullspace of a dimensional matrix')  # pynondim instead of pynondimensionalizer because the latter is too bloody long
    parser.add_argument('--input', '-i', help='Input csv file containing the dimensional matrix', required=True)
    parser.add_argument('--output', '-o', help='Output file path and name')

    args = parser.parse_args()

    output_str = nullspace_solve(args.input)

    if args.output:
        output_write(output_str, args.output)
    else:
        print(output_str)


if __name__ == "__main__":
    main()

##############################################################################
