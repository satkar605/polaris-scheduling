# Polaris Scheduling Optimization - Load Demand Data

# Import necessary libraries
from amplpy import AMPL
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Apply seaborn theme for visualization (safe for scripts)
sns.set_theme(style="whitegrid", palette="husl")

# Initialize AMPL engine
ampl = AMPL()
print("AMPL initialized successfully.")

# Step 1: Load demand data from the specified directory
file_path = "/Users/satkarkarki/Desktop/Data_Analytics_Portfolio/polaris_scheduling/data/demand_template.csv"

# Read the CSV into a DataFrame
demand_df = pd.read_csv(file_path)
print("Loaded demand data:\n")
print(demand_df)

# Step 2: Convert demand to a dictionary format suitable for AMPL
hourly_demand = dict(zip(demand_df["Hour Label"].astype(str), demand_df["Employees Needed"]))
print("\nHourly demand dictionary passed to AMPL:")
print(hourly_demand)

# Step 3: Define Shift Coverage Mappings

# Each shift is assigned to the list of hour labels it covers
shifts = {
    "FT": ["7", "8", "9", "10", "12", "13", "14", "15"],  # lunch at 11am
    "PT1": ["7", "8", "9", "10"],
    "PT2": ["8", "9", "10", "11"],
    "PT3": ["9", "10", "11", "12"],
    "PT4": ["10", "11", "12", "13"],
    "PT5": ["11", "12", "13", "14"],
    "PT6": ["12", "13", "14", "15"]
}

# Extract list of all unique shifts and hours
shift_names = list(shifts.keys())
hour_labels = list(hourly_demand.keys())  # Should match demand dict from previous step

# Create binary coverage matrix as a dictionary for AMPL
cover = {
    (s, h): int(h in shifts[s])
    for s in shift_names
    for h in hour_labels
}

# Preview coverage dictionary
print("\nShift-to-hour coverage matrix:")
for key, val in list(cover.items())[:12]:  # Show first 12 entries
    print(f"{key}: {val}")
    
# Step 4: Define the AMPL Optimization Model

model_text = """
set SHIFTS;
set HOURS;

param demand {HOURS} >= 0;
param cover {SHIFTS, HOURS} binary;
param max_part_time integer >= 0;

var Workers {SHIFTS} >= 0, integer;

minimize TotalEmployees:
    sum {s in SHIFTS} Workers[s];

subject to CoverageConstraint {h in HOURS}:
    sum {s in SHIFTS} cover[s,h] * Workers[s] >= demand[h];

subject to PartTimeCap {s in SHIFTS: s != "FT"}:
    Workers[s] <= max_part_time;
"""

# Load the model into AMPL
ampl.eval(model_text)
print("\nAMPL model loaded successfully.")

# Step 5: Load data into AMPL and solve the optimization model

# Send sets to AMPL
ampl.set["SHIFTS"] = shift_names
ampl.set["HOURS"] = hour_labels

# Send parameters to AMPL
ampl.param["demand"] = hourly_demand
ampl.param["cover"] = cover
ampl.param["max_part_time"] = 3  # default cap for PT shift workers

# Solve using HiGHS solver
ampl.solve(solver="highs")

# Report total employees needed
print("\n=== Optimization Result ===")
print(f"Minimum Total Employees Required: {ampl.obj['TotalEmployees'].value()}")

# Show how many employees are assigned per shift
print("\nShift Assignment Breakdown:")
for shift, count in ampl.var["Workers"].to_dict().items():
    print(f"{shift}: {int(count)} workers")
    



