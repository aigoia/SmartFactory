score = {"korean":  [83, 90, 88], "english": [92, 79, 86], "math":  [88, 86, 94]}

mean_korean = 0
for i in score["korean"]:
    mean_korean = mean_korean + i
mean_korean = mean_korean / len(score["korean"]) 

mean_english = 0
for i in score["english"]:
    mean_english = mean_english + i
mean_english = mean_english / len(score["english"])

mean_math = 0
for i in score["math"]:
    mean_math =   mean_math + i
mean_math = mean_math / len(score["math"])

print(f"math mean {mean_korean}")
print(f"english mean {mean_english}")
print(f"korean mean {mean_math}")