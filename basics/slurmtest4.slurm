#!/bin/bash
#SBATCH --job-name=slurmtest4
#SBATCH --output=%x_%j.out
#SBATCH --mail-user="c.a.handy@hum.leidenuniv.nl"
#SBATCH --mail-type="ALL"
#SBATCH --time=00:01:00
#SBATCH --partition=testing
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=100MB

# load modules (assuming you start from the default environment)
# we explicitly call the modules to improve reproducibility
# in case the default settings change

module load ALICE/default

# Source the Python virtual environment
#source $HOME/workshop/venv/bin/activate

echo "[$SHELL] #### Starting Python test"
echo "[$SHELL] ## This is $SLURM_JOB_USER on $HOSTNAME and this job has the ID $SLURM_JOB_ID"
# get the current working directory
export CWD=$(pwd)
echo "[$SHELL] ## current working directory: "$CWD

# Run the file
echo "[$SHELL] ## Run script"

python3 $HOME/workshop/pythonmultiloop.py

echo "[$SHELL] ## Script finished"

echo "[$SHELL] #### Finished Python test. Have a nice day"

