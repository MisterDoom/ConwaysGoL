import sys
import argparse
from CellLife import CellLife


def main():
    parser = argparse.ArgumentParser(
        description="Conway's Game of Life simulation")
    # add arguments
    parser.add_argument('--grid-size', dest='gridSize', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    args = parser.parse_args()

    Conway = CellLife(genRandom=0)
    Conway.addGosperGun(1, 1)
    Conway.startSimulation()


# call main
if __name__ == '__main__':
    main()
