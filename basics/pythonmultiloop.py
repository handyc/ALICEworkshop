import multiprocessing
import os

def agent(a, b):
    """thread worker function"""
    print("hello")
    return "hi"

numcores = int(os.environ['SLURM_JOB_CPUS_PER_NODE'])
if numcores < 1:
    numcores = int(1)

########################################################
maxagents = 1000
########################################################
with multiprocessing.Pool(processes=numcores) as pool:
    argument1 = 0
    argument2 = 4
    args = [(argument1, argument2,) for x in range(0,maxagents)]
    results = pool.starmap(agent, args)
########################################################

print(results)

