import numpy as np
from ortools.algorithms.python import knapsack_solver as pywrapknapsack_solver


def knapsack_ortools(values, weights, items, capacity):
    """0-1 Knapsack problem solver"""
    osolver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.KNAPSACK_DYNAMIC_PROGRAMMING_SOLVER,
        "SummarizationSegmentSelection")

    scale = 1000
    values = np.array(values)
    weights = np.array(weights)
    values = (values * scale).astype(np.int_)
    weights = (weights).astype(np.int_)
    capacity = capacity

    osolver.Init(values.tolist(), [weights.tolist()], [capacity])
    osolver.Solve()
    packed_items = [x for x in range(0, len(weights))
                    if osolver.BestSolutionContains(x)]

    return packed_items
