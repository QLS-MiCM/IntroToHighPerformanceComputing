# Exercises: Making Frozen Dumplings on DRAC

In these exercises you will send a small Python "cooking" job to a DRAC cluster, run it with slurm, fix whatever goes wrong, and bring the results back to your laptop.

## What's in this folder

| Folder | Contents |
|---|---|
| `Scripts/` | `make_frozen_dumplings.sh` (the slurm batch script you will edit and submit) and `make_frozen_dumplings.py` (the code it runs) |
| `Data/` | Three dumpling fillings (`dumpling_filling1.txt` to `dumpling_filling3.txt`), one ingredient per line |
| `Outputs/Results/` | Finished bags of dumplings are written here. An example result is already included |
| `Outputs/Logs/` | slurm writes each job's `.out` and `.err` files here |

## Module II: Deliver your files to DRAC

1. Log in to your cluster (Fir, Narval, Nibi or Rorqual) from your terminal.
2. In Globus, create a destination folder on the cluster called `IntroToHighPerformanceComputing`.
3. Set the source to this `Exercises` folder on your laptop, select **all folders inside it**, and click **Start**.
4. On DRAC, use `cd`, `ls` and `cat` to find and print the file in `Outputs/Results/`. This confirms the transfer worked.

On DRAC your folder should now look like this:

```
IntroToHighPerformanceComputing/
├── Data/
├── Outputs/
│   ├── Logs/
│   └── Results/
└── Scripts/
```

## Module III: Submit your job

1. On DRAC, print the current batch script: `cat Scripts/make_frozen_dumplings.sh`
2. On your laptop, open `Scripts/make_frozen_dumplings.sh` in your code editor and edit the lines ending in `# CHANGE`:
   - `--account`: your DRAC allocation (for example `def-yoursupervisor`)
   - `--chdir`: the full path to your `IntroToHighPerformanceComputing` folder on DRAC (run `pwd` inside it to find it)
   - `--mail-user`: your email address
3. Change the input data to `dumpling_filling2.txt` or `dumpling_filling3.txt`.
4. Save the file and sync it to DRAC with Globus. Print it again on DRAC to confirm the update arrived.
5. From your `IntroToHighPerformanceComputing` folder, submit the job:
   ```bash
   sbatch Scripts/make_frozen_dumplings.sh
   ```
6. Check on it with `sq` (or `squeue -u $USER`). Cancel it with `scancel <jobID>` if needed.

## Module IV: Debug your job

Jobs don't always work the first time.

1. When your job ends, read its log files in `Outputs/Logs/` (`dumplings_<jobID>.out` and `dumplings_<jobID>.err`) and any email slurm sent you.
2. Run `seff <jobID>` to see its final state and how much time and memory it used.
3. Work out what type of error occurred (not enough time or memory, a wrong file path, or a missing module), then fix it in the batch script on your laptop.
4. Sync the fixed script to DRAC with Globus and resubmit with `sbatch`. Repeat until the job completes.

## Retrieve your results

In Globus, go to `Outputs/Results/` on the cluster, select your new dumplings file, and transfer it to the `Outputs/Results/` folder on your laptop. Open it to check your dumplings.
