import os
import csv
import argparse
import re

#without 350
MX_VALUES = [4500]
MY_VALUES = [50, 60, 70, 80, 90, 95, 100, 125, 150, 170, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2300, 2400, 2600, 2800, 3000, 3300, 3500, 3800]

FRAGMENT = "genFragments/Hadronizer/13TeV/ResonanceDecayFilter_example_HY_XToYH_HTo2B_YTo2WTo2Q1L1Nu.py"
EVENTS = 100000
GENERATOR = "madgraph"

def find_gridpack(gridpack_dir, mx, my):
    """
    Search the gridpack directory for a file where MX and MY match exactly using regex.
    """
    mx_pattern = f"MX_{mx}(?:_|\\b)"
    my_pattern = f"MY_{my}(?:_|\\b)"

    for root, _, files in os.walk(gridpack_dir):
        for file in files:
            if re.search(mx_pattern, file) and re.search(my_pattern, file):
                return os.path.join(root, file)
    return None

def main(gridpack_dir, output_csv):
    rows = []
    table = {mx: {my: "" for my in MY_VALUES} for mx in MX_VALUES}


    for mx in MX_VALUES:
        for my in MY_VALUES:
            if mx - my > 125:
                dataset = f"NMSSM_XToYHTo2W2BTo2Q1L1Nu2B_MX-{mx}_MY-{my}_TuneCP5_13TeV-madgraph-pythia8"
                #dataset = f"NMSSM_XToYHTo2V2BTo2L2Nu2B_MX-{mx}_MY-{my}_TuneCP5_13TeV-madgraph-pythia8"
                gridpack = find_gridpack(gridpack_dir, mx, my)
                if gridpack:
                    rows.append([dataset, FRAGMENT, EVENTS, GENERATOR, gridpack])
                    table[mx][my] = "x"
                else:
                    print(f"Gridpack not found for MX={mx}, MY={my}. Skipping this sample.")

    # Write to CSV
    with open(output_csv, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["dataset", "fragment", "events", "generator", "gridpack"])
        writer.writerows(rows)

    print(f"\n CSV written to {output_csv} with {len(rows)} entries.")

    print("Combination table (x = written to CSV):\n")
    header = "MX\\MY".ljust(8) + "".join(f"{my:>6}" for my in MY_VALUES)
    print(header)
    print("-" * len(header))
    for mx in MX_VALUES:
        row = f"{mx:<8}" + "".join(f"{table[mx][my]:>6}" for my in MY_VALUES)
        print(row)

# === CLI ===
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate NMSSM CSV file for gridpacks.")
    parser.add_argument("--gridpack_dir", help="Path to the directory containing gridpacks")
    parser.add_argument("--output", default="nmssm_datasets.csv", help="Output CSV file name")
    args = parser.parse_args()

    main(args.gridpack_dir, args.output)
