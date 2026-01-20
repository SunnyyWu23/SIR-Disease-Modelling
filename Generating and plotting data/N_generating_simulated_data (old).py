import csv
import math
import matplotlib.pyplot as plot
import numpy as np
# Adjustments:
# much flatter infected and thus death rate and numbers then Liberia, better response
# PIECEWISE BETA, beta switches after a certain time to reflect changes in public health responses

# SIR initial values for Nigeria
# Population ≈ 185,000,000, initial cumulative cases = 19, deaths = 7
S = 1850000 - 19 - 7   # susceptible
I = 19.0                 # currently infected at start of data
D = 7.0                  # cumulative deaths so far
R = 0.0                  # recovered (non-fatal removals)
N = S + I + D + R

# Parameters tuned to match "fast then slow" growth and ~10k cases, ~5k deaths
beta_fast = 0.023      # infection rate (EARLY)
beta_slow = 1e-7      # infection rate (AFTER CONTAINMENT)
T_switch = 7          # day at which containment kicks in

v = 0.20              # total removal rate from I (recovered + dead)
fatality_frac = 0.053   # proportion of removed people who die

h = 1.0           # data collect time per step
t = 0             # data collection time from start (1 t ~ 2.5 days)

# Cumulative infected counter (included to match data set)
cumulative_infected = I  # start with initial cumulative cases = 1378

# Plotting simulated points 
# Gather all points for plotting
S_list = [] # this may not be useful 
I_list = [] # this may not be useful
R_list = []
D_list = []
t_list = []
cumulative_infected_list = []  

months = [
    "Sep 2014", "Oct 2014", "Nov 2014", "Dec 2014",
    "Jan 2015", "Feb 2015", "Mar 2015", "Apr 2015",
    "May 2015", "Jun 2015"
]

with open("simulated_Nigeria_2014_2016.csv", 'w', newline='') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow([
        "Country",
        "Data points collected from the beginning of data set",
        "Cumulative number of infected people",
        "Cumulative number of dead people"
    ])

    # perform exactly 121 iterations
    while t < 121:
        # New infections (S → I)
        beta = beta_fast if t < T_switch else beta_slow
        dSdt = -beta * S * I / N

        # New infections this step
        new_infected = -dSdt * h
        cumulative_infected += new_infected

        # Rate of removals (I → R)
        dIdt =  (dSdt - v * I) if t < T_switch else (-dSdt - v * I) # MODIFICATION TO SIR

        # Split removals into recovered and dead
        dRdt = (1.0 - fatality_frac) * v * I
        dDdt = fatality_frac * v * I

        # Euler updates
        S += dSdt * h
        I += dIdt * h
        R += dRdt * h
        D += dDdt * h

        t += h

        # Add stuff to list for plotting
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
        D_list.append(D)
        t_list.append(t)
        cumulative_infected_list.append(cumulative_infected) 

        # Write simulated cumulative cases & cumulative deaths
        csvwriter.writerow([
            "Nigeria",
            int(t),
            math.trunc(float(cumulative_infected)),  # cumulative infected people
            math.trunc(float(D))                     # cumulative dead people
        ])


tick_positions = np.linspace(0, 121, len(months))

# Replace x-axis ticks with month names
plot.xticks(tick_positions, months, rotation=0, fontsize=6)

# plot.plot(t,S_list, label = "Susceptible") MAY NOT BE NECESSARY TO PLOT
plot.plot(t_list,cumulative_infected_list, label = "Simulated_Infected") # Plot cumulative infected not infected on a given day
# plot.plot(t_list,R_list, label = "Simulated_Removed") # MAY NOT BE NECESSARY TO PLOT
plot.plot(t_list,D_list, label = "Simulated_Dead") 

# Scatter real data points for Nigeria on top of existing data
L_cumulative_infected_list = []
L_cumulative_deaths_list = []
with open("Nigeria_2014_2016.csv", 'r', newline='') as file:
    csv_file = csv.reader(file)
    next(csv_file) # Skip header
    i = 0
    csv_file = list(csv_file) # Convert csv iterator into list that can be indexed
    limited_rows = csv_file[:121] # Only want 121 rows
    for row in limited_rows:
        L_cumulative_infected_list.append(float(row[2]))
        L_cumulative_deaths_list.append(float(row[3]))

plot.scatter(t_list,L_cumulative_infected_list, c="Red", label = "Real_Infected")
plot.scatter(t_list,L_cumulative_deaths_list, c="Black", label = "Real_Dead")

plot.title("Nigeria - Plots for I and D")
plot.xlabel("Months")
plot.ylabel("Number of People")
plot.legend()
plot.show()
