import numpy as np
import random

# Define the number of servers and their capacity
N = 10 # Number of servers
Capacity = [random.randint(50, 100) for _ in range(N*N)] # Capacity of each server

# Define the connections between servers
Connections = np.zeros((N*N, N*N)) # Interconnections between the servers

for i in range(N*N):
    for j in range(N*N):
        if i == j:
            Connections[i][j] = 0 # No connection between the same server
        elif (i // N == j // N) and (abs(i - j) == 1 or abs(i - j) == N):
            Connections[i][j] = 1 # Connection between adjacent servers
            
# Initialize the number of migrations and jobs
Migrations = 0
Jobs = 0

# Start the simulation
while Jobs < Capacity[0]:
    # Select a random server
    server_id = random.randint(0, N*N - 1)
    
    # If the server is full, then migrate the jobs to adjacent servers
    if Jobs >= Capacity[server_id]:
        for i in range(N*N):
            if Connections[server_id][i] == 1 and Jobs < Capacity[i]:
                Migrations += 1
                Jobs += 1
                break
    # Else the jobs can be processed on the same server
    else:
        Jobs += 1

# Print the number of migrations
print("Capacity", Capacity)
print("Number of migrations:", Migrations)
# Add the nodes
