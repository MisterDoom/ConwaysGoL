import sys
import argparse
import cProfile
import pstats
from pstats import SortKey
from CellLife import CellLife


def main():
    parser = argparse.ArgumentParser(
        description="Conway's Game of Life simulation")
    # add arguments
    parser.add_argument('--grid-size', dest='gridSize', required=False)
    parser.add_argument('--saving-file', dest='savingfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--gen-random', dest='genrandom', required=False)
    args = parser.parse_args()
    cProfile.run(simulate.__code__, "pStats", SortKey.CUMULATIVE)
    p = pstats.Stats("pStats")
    p.strip_dirs().sort_stats(SortKey.TIME).print_stats(10)


def simulate():
    Conway = CellLife(None, None, 0, None)
    Conway.addGosperGun(1, 1)
    Conway.startSimulation()


# call main
if __name__ == '__main__':
    main()
