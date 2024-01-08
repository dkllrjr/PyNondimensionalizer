from setuptools import setup, find_packages

setup(
        packages=find_packages(),
        install_requires=[
            'click',
            'sympy',
            'pandas',
        ],
        entry_points={
            'console_scripts': [
                'pynondim = pynondimensionalizer.pynondimensionalizer:pynondim',
            ]
        }
)
