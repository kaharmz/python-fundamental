
n = input()
arr = list(map(int, input.split()))
if arr:
    top_score = arr[0]
    for i in arr:
        if top_score < i:
            top_score = i
    for j in arr:
        if 'runner_score' not in locals() and j < top_score:
            runner_score = j
        elif top_score > j > runner_score:
            runner_score = j
    if 'runner_score' in locals():
        print(runner_score)

