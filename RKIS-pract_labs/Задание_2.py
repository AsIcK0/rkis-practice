def find_combinations(candidates, target):
    candidates.sort()
    result = []
    def find(start, target, current):
        if target == 0:
            result.append(current[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            find(i + 1, target - candidates[i], current + [candidates[i]])
    find(0, target, [])
    return result
candidates = [2, 5, 2, 1, 2]
target = 5
combinations = find_combinations(candidates, target)
for comb in combinations:
    print(comb)