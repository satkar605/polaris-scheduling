✅ Project Title
Polaris Staff Scheduler – Shift Optimization App

✅ Project Scenario
Suppose Polaris needs to ensure employee coverage for the following times between 7am and 4pm.
7am-8am=7; 8am-9am=7; 9am-10am=8; 10am-11am=8; 11am-12pm=9; 12pm-1pm=10; 1pm-2pm=10; 2pm-3pm=9; 3pm-4pm=8

Employees available for these times include full-time workers, working 7am-4pm, and part time workers who can work one of the following, 4-hour shifts.
7am-11am; 8am-12pm; 9am-1pm; 10am-2pm; 11am-3pm; 12pm-4pm

All full-time employees take their one-hour lunch break at 11am.  To ensure part-time shifts can be covered, Polaris management limits the number of workers in each of the shifts to no more than 3.

Determine the how many of each type of shift need to be hired to minimize the number of total employees.  The optimal solution will be 17.

Suppose Polaris is looking to cut costs and wants to minimize the number of full-time employees to help reduce benefit expenditures without increasing the total number of employees.  Resolve this problem with the new goal and constraint.  Discuss both the original and secondary goal recommendations and outcomes.  A less than or equal to constraint will make your model more robust for ST.

Use Solvertable to see what happens to total employees and FT employees when the required number of workers needed from 11am-12pm ranges from 6-12. Think about what increments would be most helpful if you were the manager when building ST.

✅ Goal
Build an interactive, data-driven optimization tool that allows managers to:

Input or adjust hourly staffing requirements

Modify shift caps and rules

Solve for the minimal number of employees needed

Understand tradeoffs between full-time and part-time coverage

Eventually deploy via a Streamlit or Gradio interface

✅ Project Workflow
Phase 1: Modeling and Core Logic
✔️ Define hourly demand and shift structure
✔️ Build AMPL model in amplpy
✔️ Allow user-configurable inputs (demand, PT limits)
✔️ Solve and output optimized staffing

Phase 2: Feature Enhancements
🔲 Add constraints toggle (e.g., no FT lunch break vs. lunch at 11am)
🔲 Visualize hourly coverage and shift assignments
🔲 Allow dynamic shift creation (via GUI or JSON input)
🔲 Add second objective: minimize FT count without increasing total

Phase 3: Interface & Deployment
🔲 Convert to interactive web interface (Streamlit/Gradio)
🔲 Add CSV import/export for demand templates
🔲 Package as reusable notebook app or Dockerized service
🔲 Include solver toggle (HiGHS vs. Gurobi if available)

Phase 4: Documentation & Publishing
🔲 Create README with examples
🔲 Explain optimization goals (total staff vs. FT preference)
🔲 Include screenshot of output + interactive guide
🔲 Publish on GitHub or internal scheduling portal

✅ Suggested Folder Structure (if working locally or in GitHub)
bash
Copy
Edit
polaris-scheduler/
│
├── notebooks/
│   └── polaris_shift_optimizer.ipynb     # Core notebook
│
├── ampl_models/
│   └── scheduling.mod                    # (optional backup .mod file)
│
├── data/
│   └── demand_template.csv               # Example hourly demand
│
├── app/
│   └── streamlit_app.py                  # Web interface
│
├── requirements.txt                      # dependencies
├── README.md                             # project overview
└── LICENSE
✅ Next Steps for You
Confirm scope: Are we only solving Phase 1 right now?

Do you want help structuring the .ipynb file with markdown cells and headers?

Should we begin versioning a README and Streamlit app template now or finish the modeling logic first?

Let me know how you want to proceed, and I'll prepare that next.