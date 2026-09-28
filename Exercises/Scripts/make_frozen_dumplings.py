from pathlib import Path
import sys
import time

def make_frozen_dumplings(input_file, output_folder, n_bags=3):
    """
    Read two ingredients (one per line) from input_file and write
    n_bags ASCII frozen dumpling bags to output_file.
    """

    # Read ingredients
    ingredients = [
        line.strip().upper()
        for line in Path(input_file).read_text().splitlines()
        if line.strip()
    ]

    filling = f"{ingredients[0]} & {ingredients[1]}"

    width = 35

    bag = [
        "              ___________________________",
        "           .-'                           '-.",
        "         .'{}'.".format(" " * 31),
        f"        /{'FROZEN DUMPLINGS'.center(width)}\\",
        f"       /{filling.center(width)}\\",
        "      |  _^^^_   _^^^_   _^^^_   _^^^_        |",
        "      | (_____) (_____) (_____) (_____)       |",
        "      |                                       |",
        "      |  _^^^_   _^^^_   _^^^_   _^^^_        |",
        "      | (_____) (_____) (_____) (_____)       |",
        "      |                                       |",
        f"      |{'KEEP FROZEN'.center(width)}|",
        f"      |{'NET WT. 750 g'.center(width)}|",
        "       \\_____________________________________/",
    ]

    output = "\n\n".join("\n".join(bag) for _ in range(n_bags))

    file_name = f"frozen_{ingredients[0].lower()}_and_{ingredients[1].lower()}_dumplings.txt"
    output_file = Path(output_folder) / file_name
    Path(output_file).write_text(output)
    print(f"Completed {output_file.name} with {n_bags} bags of frozen dumplings.")

if __name__ == "__main__":

    # input file and output folder passed from sbatch
    input_file = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])

    output_dir.mkdir(exist_ok=True)

    # generate output filename
    ingredients = [
        line.strip().upper()
        for line in input_file.read_text().splitlines()
        if line.strip()
    ]

    # print the input file name to the console for debugging purposes
    print(f"Working on {input_file.name}...", flush=True)

    # Eat ~4GB of memory to simulate a memory-intensive task
    _ = bytearray(4 * 1024**3)

    # Hang for 2 minutes to simulate a long-running task
    time.sleep(120)

    make_frozen_dumplings(
        input_file=input_file,
        output_folder=output_dir,
        n_bags=5
    )

