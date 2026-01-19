# command for terminal: python run_py_files.py

import subprocess

# indicate which python files to run
files = ["N_generating_simulated_data.py", "calculate_tolerance_of_simulated_data.py", "L_generating_simulated_data.py"]

for f in files:
    print(f"Running {f}...")
    subprocess.run(["python3", f])
