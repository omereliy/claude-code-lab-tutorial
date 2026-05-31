#!/bin/bash
# ----------------------------------------------------------------------------
# Example SLURM batch script. Treat every value below as a PLACEHOLDER until
# you've checked it against the BGU cluster's own conventions — wrong partition
# or account names fail late or queue forever.
#
# OMER REVIEW: replace <PARTITION>, <ACCOUNT>, and the module/conda lines with
# the lab's real values, or point students at the cluster docs. (PENDING.md.)
# ----------------------------------------------------------------------------

#SBATCH --job-name=pyval-demo
#SBATCH --partition=<PARTITION>        # e.g. the lab's GPU partition
#SBATCH --account=<ACCOUNT>            # billing/allocation account, if required
#SBATCH --gres=gpu:1                   # drop this line for CPU-only jobs
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=04:00:00                # walltime cap — job is killed past this
#SBATCH --output=logs/%x-%j.out        # %x=job-name, %j=job-id
#SBATCH --error=logs/%x-%j.err

set -euo pipefail
mkdir -p logs

# --- environment ------------------------------------------------------------
# Use ONE of these patterns; delete the other. Don't echo secrets here —
# anything you print lands in the log file (and in Claude's transcript if it
# reads the log).
# module load <python-module>
# source ~/envs/pyval/bin/activate

echo "host=$(hostname) job=${SLURM_JOB_ID:-NA} started=$(date -Iseconds)"

# --- the actual work --------------------------------------------------------
srun python -m your_package.run --config configs/demo.yaml

echo "finished=$(date -Iseconds)"
