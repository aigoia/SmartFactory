import statistics

score = {"korean":  [83, 90, 88], "english": [92, 79, 86], "math":  [88, 86, 94]}

mean_korean = 0
for i in score["korean"]:
    mean_korean = mean_korean + i
mean_korean = mean_korean / len(score["korean"]) 

mean_english = sum(score["english"]) / len(score["english"])

mean_math = statistics.mean(score["math"])

print(f"korean mean {mean_korean}")
print(f"english mean {mean_english}")
print(f"korean mean {mean_math}")