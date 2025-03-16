import guitar
from collections import defaultdict

results = defaultdict(int)

for _ in range(10000):
    results[guitar.legato()] += 1
    results[guitar.picking()] += 1
    results[guitar.sweeping()] += 1
    results[guitar.misc_exercise()] += 1

for item in results:
    results[item] = results[item] / 400

results_list = [(key, value) for key, value in results.items()]
results_list = sorted(results_list)

print(results_list)
