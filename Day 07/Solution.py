import os
import statistics

def load_input(file):
    with open(file, 'r') as lines:
        temp = [str(line).split(',') for line in lines]
        return [int(x) for x in temp[0]]

def find_distances(positions, aim):
    fuel = 0

    for pos in positions:
        fuel += abs(pos-aim)

    return fuel

def find_cost(positions, aim):
    fuel = 0
    dist = 0

    for pos in positions:
        dist = abs(pos-aim)
        fuel += int(dist*(dist+1)/2)

    return fuel

def main():
    # load file
    file_name = os.path.join(os.path.dirname(__file__), "input.txt")
    positions = load_input(file_name)
    
    #part 1
    costs = []
    for i in range(min(positions), max(positions)): #answer is between min and max position
        costs.append(find_distances(positions, i))
    print("Part 1: " + str(min(costs)))

    #part 2  
    mean = int(statistics.mean(positions)) #the aim needs to be there
    cost = find_cost(positions, mean)
    print("Part 2: " + str(cost))
    
if __name__ == '__main__':
    main()