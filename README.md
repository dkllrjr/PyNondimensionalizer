# PyNondimensionalizer

A simple little python program to help find nondimensional numbers, such as the Reynold's number, Rossby number, etc.

## Installation

To install PyNondimensionalizer, use :code:`pip`::

$ pip install PyNondimensionalizer

# Basic Usage

# Fundamentals

This program is based off the work of James Price but contains a lot of general ideas. First, you want to make a matrix with the variables of the problem and the dimensions. Using the pendulum example from `Price`:

.. math::
    \begin{matrix}
    & \phi & t & M & L & g & \phi_0 \\
    m & 0 & 0 & 1 & 0 & 0 & 0 \\
    l & 0 & 0 & 0 & 1 & 1 & 0 \\
    t & 0 & 1 & 0 & 0 & -2 & 0
    \end{matrix}

Then build the dimension matrix from this matrix:

.. math::
    \mathbb{D} =
    \begin{bmatrix}
    0 & 0 & 1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 1 & 1 & 0 \\
    0 & 1 & 0 & 0 & -2 & 0
    \end{bmatrix}
