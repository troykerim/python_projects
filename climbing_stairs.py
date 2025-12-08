def minCostRecur(i, cost):

    if i == 0 or i == 1:
        return cost[i]
    return cost[i] + min(minCostRecur(i - 1, cost), 
                         minCostRecur(i - 2, cost))

def minCostClimbingStairs(cost):
    n = len(cost)
    
    if n == 1:
        return cost[0]
    
    return min(minCostRecur(n - 1, cost), 
               minCostRecur(n - 2, cost))


if __name__ == "__main__":
    n = int(input("Enter the number of steps: "))
    cost = []

    print("Enter the cost for each step:")
    for i in range(n):
        val = int(input(f"  Step {i + 1} cost: "))
        cost.append(val)

    print("\nCost list:", cost)
    print("Minimum cost to climb stairs:", minCostClimbingStairs(cost))
