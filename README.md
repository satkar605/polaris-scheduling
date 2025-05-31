# Polaris Scheduling Optimization

This project provides a staff scheduling optimization tool for Polaris, built using the AMPL modeling language and Python. The tool determines the optimal number and mix of full-time and part-time employees required to meet hourly staffing demands while minimizing total workforce size or full-time headcount.

---

## 🚀 Project Objectives

1. **Primary Goal**: Minimize the total number of employees required to meet hourly demand.
2. **Secondary Goal**: Minimize the number of full-time employees without increasing total staff count.
3. Provide a user-adjustable interface to configure:

   * Hourly staffing demand
   * Shift rules and part-time caps
   * Lunch breaks and custom shift hours

---

## 🧮 Optimization Setup

### Shift Definitions

* **Full-Time (FT)**: 7:00 AM – 4:00 PM (1-hour lunch at 11:00 AM)
* **Part-Time (PT)**: Six 4-hour shifts

  * PT1: 7–11 AM
  * PT2: 8–12 PM
  * PT3: 9–1 PM
  * PT4: 10–2 PM
  * PT5: 11–3 PM
  * PT6: 12–4 PM

### Constraints

* Each hour must be staffed by enough employees.
* A maximum of 3 workers allowed per part-time shift.
* Full-time workers are unavailable from 11–12 PM due to lunch.

---

## 📁 Directory Structure

```
polaris-scheduling/
├── data/
│   └── demand_template.csv        # Editable hourly demand file
├── notebooks/
│   └── polaris_shift_optimizer.py # Core optimization script
├── app/                           # (optional future) Streamlit interface
├── ampl_models/                   # (optional backup of .mod file)
├── README.md
└── requirements.txt
```

---

## 🧾 How to Use

### Step 1: Clone and Set Up Environment

```bash
conda create -n polaris_opt python=3.10 numpy=1.24 amplpy pandas matplotlib -y
conda activate polaris_opt
pip install amplpy seaborn
```

### Step 2: Run the Optimizer

Use Spyder or VS Code to open `polaris_shift_optimizer.py`. Run the script.

* First solve: Minimizes total employees.
* Second solve: Minimizes FT employees under a fixed total cap.

### Step 3: Customize Demand

Edit `data/demand_template.csv` to adjust per-hour requirements.

---

## 📊 Example Output

```
=== Optimization Result ===
Minimum Total Employees Required: 17

Shift Assignment:
FT: 8 workers
PT2: 3 workers
PT4: 3 workers
PT5: 3 workers
```

```
=== Secondary Optimization Result ===
Minimum Full-Time Employees (with ≤17 total): 6

Shift Assignment:
FT: 6 workers
PT1: 2 workers
PT3: 3 workers
PT4: 3 workers
PT6: 3 workers
```

---

## 📌 Next Steps

* [ ] Add demand visualizations
* [ ] Deploy interactive Streamlit app
* [ ] Add support for custom shift patterns

---

## 🧠 Author

**Satkar Karki**
Graduate Student – Business Analytics
GitHub: [satkar605](https://github.com/satkar605)

---

## 📄 License

MIT License
