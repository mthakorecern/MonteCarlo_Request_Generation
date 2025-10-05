import re

# Full MX and MY lists
m_X_HY_full = [240, 280, 300, 320, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2500, 2600, 2800, 3000, 3500, 4000]

m_Y_full = [50, 60, 70, 80, 90, 95, 100, 125, 150, 170, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2300, 2400, 2600, 2800, 3000, 3300, 3500, 3800]


# Step 1: Build all valid combinations MX-a_MY-b where a - b > 125
valid_combinations = set()
for a in m_X_HY_full:
    for b in m_Y_full:
        if a - b > 125:
            valid_combinations.add((a, b))  # store as tuple

# Step 2: Read dataset file and extract combinations that are present
found_combinations = set()
pattern = re.compile(r'MX-(\d+)_MY-(\d+)')

with open("/afs/cern.ch/user/m/mithakor/public/Combination_Checker/DAS_YH_2W2BTo2Q1L1Nu2B.txt", "r") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            a = int(match.group(1))
            b = int(match.group(2))
            found_combinations.add((a, b))

# Step 3: Find valid combinations that are missing from the file
missing_combinations = sorted(valid_combinations - found_combinations)

# Step 4: Print them in required format
#print("Missing combinations (MX-a_MY-b):")
for a, b in missing_combinations:
    print(f"MX-{a}_MY-{b}")
