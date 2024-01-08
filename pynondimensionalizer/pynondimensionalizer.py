__docformat__ = "numpy"

import click
from sympy import Matrix, pretty
from pandas import read_csv
from pathlib import Path

#  ──────────────────────────────────────────────────────────────────────────

def nullspace_solve(input_file, width=None):
    """Solves for the nullspace matrix, with the given dimensions matrix.

    Parameters
    ----------
    input_file : str
        Path to the input file with the dimensions matrix.

    Returns
    -------
    output_str : str
        String that contains the nullspace matrix, with headers.
    D : Matrix
        Dimensional matrix.
    S : List
        List of matrices comprising the nullspace matrix.
    dim : list
        List of strings of the dimensions.
    var : list
        List of strings of the variables.
    """

    D_in = read_csv(Path(input_file), index_col=0)

    # building dimensional matrix and getting nullspace
    D = Matrix(D_in)
    S = D.nullspace()

    dim = D_in.index.tolist()
    var = list(map(str.strip, D_in.columns.tolist()))

    dim_str = ' '.join(dim)
    var_str = ' '.join(var)

    # building string
    output_str = 'Dimensions = \n\n' + dim_str + '\n\nVariables = \n\n' + var_str + '\n\nD = \n\n' + pretty(D, num_columns=width) + '\n\nS = \n\n' + pretty(S, num_columns=width) + '\n\n'

    # getting non dimensional numbers
    output_str += '𝚷 = \n' 

    for i, Si in enumerate(S):
        output_str += '\n𝚷 ' + str(i) + '\t= '
        for j, Sij in enumerate(Si):
            if Sij != 0:
                output_str += var[j] + '^(' + str(Sij) + ') '


    return output_str, D, S, dim, var


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

#  ──────────────────────────────────────────────────────────────────────────
# cli

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-i', '--input', help='Input csv file containing the dimensional matrix', required=True, type=str)
@click.option('-o', '--output', help='Output file path and name', type=str, default=None)
@click.option('-w', '--width', help='Column width for output', type=int, default=None)
def pynondim(input, output, width):
    """Find the nullspace of a dimensional matrix and the nondimensional variables.
    """

    output_str, S, D, dim, var = nullspace_solve(input, width=width)

    if output:
        output_write(output_str, output)
    else:
        print(output_str)
