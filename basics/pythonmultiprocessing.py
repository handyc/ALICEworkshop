import multiprocessing
import os
import datetime

start = datetime.datetime.now()
start = datetime.datetime.now()

timeformat = "%Y%m%dT%H%M%S.%f"
displayformat = "%Y-%m-%dT%H:%M:%S.%f"

fstart = start.strftime(timeformat)
fstartdisplay = start.strftime(displayformat)

def agent(a, b):
    """thread worker function"""
    print("hello")

numcores = int(os.environ['SLURM_JOB_CPUS_PER_NODE'])
if numcores < 1:
    numcores = int(1)

####
maxagents = 1000

print("started at " + str(fstartdisplay))
print("comparing performance of " + str(maxagents) + " agents on " + str(numcores) + " threads")

########################################################
with multiprocessing.Pool(processes=numcores) as pool:
    argument1 = 0
    argument2 = 4
    args = [(argument1, argument2,) for x in range(0,maxagents)]
    results = pool.starmap(agent, args)
########################################################

#print(results)

# various ways of displaying the time
finish = datetime.datetime.now()
ffinish = finish.strftime(timeformat)
ffinishdisplay = finish.strftime(displayformat)

totaltime = finish - start

####
print("ran " + str(fstartdisplay) + " to " + str(ffinishdisplay))
print("execution time: " + str(totaltime))
print("comparing performance of " + str(maxagents) + " agents on " + str(numcores) + " threads")
