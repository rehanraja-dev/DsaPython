def optimal_merge(files):

    total_cost = 0

    while len(files) > 1:

        files.sort()

        first = files.pop(0)
        second = files.pop(0)

        merge_cost = first + second

        total_cost += merge_cost

        files.append(merge_cost)

    return total_cost


files = [20, 15, 10, 5, 25, 30,45]

print("Minimum Merge Cost =", optimal_merge(files))