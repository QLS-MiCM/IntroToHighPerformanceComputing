# Instructor Notes (answer key)

`Scripts/make_frozen_dumplings.sh` contains **two deliberate errors** for the Module IV "Debug your batch script" activity. Please don't fix them in the repo.

1. **Incorrect path to file.** `input_data="data/..."` uses a lowercase `data`, but the folder is `Data/`, and DRAC filesystems are case-sensitive. The script's path check stops the job with `Error: Input data not found at data/...` in the `.out` file. Fix: `Data/`.
2. **Insufficient memory requested.** `--mem=1G`, but the Python script allocates about 4 GB. slurm kills the job with `OUT_OF_MEMORY`, and the `.err` file shows an `oom_kill` event. A successful run peaks at about 4.2 GB, so the fix is `--mem=5G` or more (`8G` is comfortable). The job also sleeps for 2 minutes, so it fits within `--time=00:05:00`.

Other things that are intentional:

- `--chdir` points at the `IntroToHighPerformanceComputing` folder, not `.../Exercises/`, because participants upload the *contents* of `Exercises/` into that folder with Globus (Module II).
- `Outputs/Results/frozen_pork_and_chive_dumplings.txt` ships with the repo. Participants print it in Module II to confirm their Globus transfer worked.
