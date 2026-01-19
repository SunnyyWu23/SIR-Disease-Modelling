import csv

simulated_data = open("simulated_Liberia_2014_2016.csv",'r',newline='')
real_data = open("Liberia_2014_2016.csv",'r',newline='')

csv_sim = csv.reader(simulated_data,delimiter=',')
next(csv_sim) # skip headings
csv_real = csv.reader(real_data,delimiter=',')
next(csv_real) # skip headings

simulated_infected = [] #collects all simulated elements for infected people
simulated_dead = [] #collects all simulated elements for dead people
real_infected = [] #collects all real elements for infected people
real_dead = [] #collects all real elements for dead people

tolerance_for_infected_data = []
tolerance_for_dead_data = []

#add the elements to the respective lists
for row in csv_sim:
    simulated_infected.append(int(row[2])) 
    simulated_dead.append(int(row[3]))

for row in csv_real:
    real_infected.append(float(row[2]))
    real_dead.append(float(row[3]))

def calculate_tolerance(simulated_element_infected,real_element_infected,simulated_element_dead,real_element_dead):
    # calculates tolerances
    tolerance_inf = int(simulated_element_infected) - int(real_element_infected)
    tolerance_dead = int(simulated_element_dead) - int(real_element_dead)
    return tolerance_inf, tolerance_dead

#calculates tolerances for all and puts into a list
for i in range(len(simulated_infected)):
    tolerance_inf,tolerance_dead = calculate_tolerance(simulated_infected[i],real_infected[i],simulated_dead[i],real_dead[i])
    tolerance_for_infected_data.append(tolerance_inf)
    tolerance_for_dead_data.append(tolerance_dead)
    
#calculates average tolerances 
sum_inf = 0
sum_dead = 0
for i in range(len(tolerance_for_infected_data)):
    sum_inf += tolerance_for_infected_data[i]
    sum_dead += tolerance_for_dead_data[i]

avg_tolerance_for_infected_data = sum_inf/len(tolerance_for_infected_data)
avg_tolerance_for_dead_data = sum_dead/len(tolerance_for_dead_data)

print("Avg tolerance for infected data: ", avg_tolerance_for_infected_data)
print("Avg tolerance for dead data: ", avg_tolerance_for_dead_data)


simulated_data.close()
real_data.close()
              