# map

n = "3"
testcase = "40 80 60"

N = int(n)
scores = list(map(int, testcase.split(" ")))
max_score = max(scores)


def edit(score) -> float:
    global max_score
    return float(score) / float(max_score) * 100


edited_score = list(map(edit, scores))
avg = sum(edited_score)/N
print("{:.2f} is my new average acore".format(avg))
print("{:.2f} is another way to get the answer".format(sum(scores)/max_score/N*100))
