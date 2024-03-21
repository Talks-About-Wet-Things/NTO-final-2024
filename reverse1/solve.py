#!/usr/bin/env python3

import angr
import sys


def main():
    path_to_binary = "crackme"
    project = angr.Project(path_to_binary)
    initial_state = project.factory.entry_state()
    simulation = project.factory.simgr(initial_state)

    simulation.explore(find=0x0010139E, avoid=0x001013AF)

    if simulation.found:
        solution_state = simulation.found[0]
        print(solution_state.posix.dumps(sys.stdin.fileno()))

    else:
        raise Exception("Could not find the solution")


if __name__ == "__main__":
    main()
