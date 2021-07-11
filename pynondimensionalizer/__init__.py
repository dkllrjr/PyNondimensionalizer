r"""
# What it is

**PyNondimensionalizer** is a simple little command line program in python to help find nondimensional numbers, such as the Reynold's number, Rossby number, and more.

# Installation

To install **PyNondimensionalizer**, use `pip`:

```
$ pip install pynondimensionalizer
```

# Basic Usage

## Fundamentals

This program is based off the [essay by Dr. James Price](https://www.whoi.edu/science/PO/people/jprice/class/DA_SSSA.pdf) but also takes from dimensional analysis in general. Dimensional analysis allows you to remove units and scales from the process you're studying, so that you may understand it in a universal way that does not depend upon scale.

To use this program, we will use the pendulum example from Price's essay, where we want to find dimensionless numbers to represent the 2nd order differential equation of a simple, inviscid pendulum, so that the resulting solution is independent of scale.

First, we want to make a matrix with the variables of the problem and the dimensions:

$$
\\begin{matrix}
& \\begin{matrix}\\phi & t & M & L & g & \\phi_0\\end{matrix} \\\
\\begin{matrix}m \\\ l \\\ t\end{matrix} &
\\begin{bmatrix}
0 & 0 & 1 & 0 & 0 & 0 \\\
0 & 0 & 0 & 1 & 1 & 0 \\\
0 & 1 & 0 & 0 & -2 & 0
\\end{bmatrix}
\\end{matrix}
$$

The top row contains the variables of the problem. In the case of the pendulum example, $\\phi$ is the angle of the line, with length $L$, swinging a weight of mass $M$. $t$ is time and $g$ is gravity. $\\phi_0$ is the initial angle of the pendulum at $t=0$. The first column contains the dimensions: $m$ for mass, $l$ for length, and $t$ for time. The matrix holds the corresponding dimensions for each variable. For example, $\\phi$ and $\\phi_0$ don't have units and can be represented by the dimensions of $m^0l^0t^0$, whereas $g$ has 1 dimension of length, $l$, and -2 dimensions of time, $t$, and can be represented as $m^0l^1t^{-2}$. The remaining variables can be represented in a similar way.

The dimensional matrix is the above matrix, minus the labeling:

$$
\\mathbb{D} =
\\begin{bmatrix}
0 & 0 & 1 & 0 & 0 & 0 \\\ 
0 & 0 & 0 & 1 & 1 & 0 \\\ 
0 & 1 & 0 & 0 & -2 & 0
\\end{bmatrix}
$$

To find the dimensionless numbers for this example, we want to find the nullspace, $\\mathbb{S}$, of the dimensional matrix. Any linear combinations of the $N$ vectors that make up the nullspace can be used to find dimensionless numbers. For example, if we visualize the nullspace, $\\mathbb{S}$:

$$
\\mathbb{S} = \left[ S_1, S_2, S_3, ...,S_N \right]
$$

$S_1 + S_2$ is still in the nullspace, as well as $S_1 + a S_2$, where $a$ is some constant being multiplied to $S_2$. $N$ will be equal to the number of dimensions, in accordance with the [Buckingham $\\Pi$ theorem](https://en.wikipedia.org/wiki/Buckingham_%CF%80_theorem).

The nullspace for our pendulum dimensional matrix looks like this (from Price):

$$
\\mathbb{S} = 
\\begin{bmatrix}
1 & 0 & 0 \\\
0 & 1 & 0 \\\
0 & 0 & 0 \\\
0 & -1/2 & 0 \\\
0 & 1/2 & 1 \\\
\\end{bmatrix} =
\\begin{bmatrix}
\\left[ \\begin{matrix}1 \\\ 0 \\\ 0 \\\ 0 \\\ 0 \\\ 0\\end{matrix} \\right], &
\\left[ \\begin{matrix}0 \\\ 1 \\\ 0 \\\ -1/2 \\\ 1/2 \\\ 0\\end{matrix} \\right], &
\\left[ \\begin{matrix}0 \\\ 0 \\\ 0 \\\ 0 \\\ 0 \\\ 1\\end{matrix} \\right]
\\end{bmatrix}
$$

which, when labeled, looks like this:

$$
\\mathbb{S} = 
\\begin{matrix}
\\begin{matrix}\\phi \\\ t \\\ M \\\ L \\\ g \\\ \\phi_0\end{matrix} &
\\begin{bmatrix}
\\left[ \\begin{matrix}1 \\\ 0 \\\ 0 \\\ 0 \\\ 0 \\\ 0\\end{matrix} \\right], &
\\left[ \\begin{matrix}0 \\\ 1 \\\ 0 \\\ -1/2 \\\ 1/2 \\\ 0\\end{matrix} \\right], &
\\left[ \\begin{matrix}0 \\\ 0 \\\ 0 \\\ 0 \\\ 0 \\\ 1\\end{matrix} \\right]
\\end{bmatrix}
\\end{matrix}
$$

Each vector gives us a nondimensional parameter, $\\Pi_n$:

$$
S_1 = \\left[ \\begin{matrix}1 \\\ 0 \\\ 0 \\\ 0 \\\ 0 \\\ 0\\end{matrix} \\right] \\Rightarrow \\Pi_1 = \\phi^1 t^0 M^0 L^0 g^0 \\phi_0^0 = \\phi
$$

$$
S_2 = \\left[ \\begin{matrix}0 \\\ 1 \\\ 0 \\\ -1/2 \\\ 1/2 \\\ 0\\end{matrix} \\right] \\Rightarrow \\Pi_2 = \\phi^0 t^1 M^0 L^{-1/2} g^{1/2} \\phi_0^0 = \\frac{t}{\\sqrt{L/g}}
$$

$$
S_3 = \\left[ \\begin{matrix}0 \\\ 0 \\\ 0 \\\ 0 \\\ 0 \\\ 1\\end{matrix} \\right] \\Rightarrow \\Pi_3 = \\phi^0 t^0 M^0 L^0 g^0 \\phi_0^1 = \\phi_0
$$

In Price, $\\Pi_3$ is used as the nondimensional parameter of time to collapse all variations of the period due to the length of the line, $L$. With another nondimensional number (not shown here) to nondimensionalize the tension of the string with respect to time, the different possible time series of tension collapse onto one time series that only changes with different initial angles of $\\phi_0$. This "collapsing" is the removal of the scale's effect from affecting the resulting solution.

## Using **PyNondimensionalizer**

A `csv` file containing the dimensional matrix, in this case for the above pendulum example, is the input file for **PyNondimensionalizer**, and should look like this:

```
 ,phi,  t,  M,  L,  g,  phi0
m,  0,  0,  1,  0,  0,  0
l,  0,  0,  0,  1,  1,  0
t,  0,  1,  0,  0, -2,  0
```

**The variables and dimensions should be included!**

On the command line, enter the following, with the proper input file and output file location in place of `input_file.csv` and `output_file.txt`:

```
$ pynondim -i input_file.csv -o output_file.txt
```

The following output will be saved to the output file:

```
Dimensions: m l t
Variables: phi t M L g phi0

D = 

⎡0  0  1  0  0   0⎤
⎢                 ⎥
⎢0  0  0  1  1   0⎥
⎢                 ⎥
⎣0  1  0  0  -2  0⎦

S = 

⎡⎡1⎤  ⎡0 ⎤  ⎡0⎤⎤
⎢⎢ ⎥  ⎢  ⎥  ⎢ ⎥⎥
⎢⎢0⎥  ⎢2 ⎥  ⎢0⎥⎥
⎢⎢ ⎥  ⎢  ⎥  ⎢ ⎥⎥
⎢⎢0⎥  ⎢0 ⎥  ⎢0⎥⎥
⎢⎢ ⎥, ⎢  ⎥, ⎢ ⎥⎥
⎢⎢0⎥  ⎢-1⎥  ⎢0⎥⎥
⎢⎢ ⎥  ⎢  ⎥  ⎢ ⎥⎥
⎢⎢0⎥  ⎢1 ⎥  ⎢0⎥⎥
⎢⎢ ⎥  ⎢  ⎥  ⎢ ⎥⎥
⎣⎣0⎦  ⎣0 ⎦  ⎣1⎦⎦
```

*If no output file is given, the result is printed in the terminal.*

You may notice that $S_2$ here is different from $S_2$ above. However, recall that any linear combination of the nullspace vectors is also in the nullspace and, therefore, another nullspace vector. In this case, $S_2$ is just the $S_2$ above multiplied by 2.
"""

__docformat__ = 'numpy'
__version__ = '0.1.0'
