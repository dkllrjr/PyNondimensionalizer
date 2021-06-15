from pynondimensionalizer import __version__
from pynondimensionalizer.pynondimensionalizer import nullspace_solve
import os


test_data_path = os.path.dirname(__file__)


def test_version():
    assert __version__ == '0.1.0'


def test_nullspace_solve():
    input_file = os.path.join(test_data_path, 'in_test.csv')
    output_file = os.path.join(test_data_path, 'out_test.csv')

    output_str = nullspace_solve(input_file)

    with open(output_file, 'r') as file:
        exp_output_str = file.read()

    assert exp_output_str == output_str
