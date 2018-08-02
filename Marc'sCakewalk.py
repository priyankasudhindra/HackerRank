def marcsCakewalk(calorie):
    calorie = sorted(calorie, reverse=True)
    total = 0
    number_of_cupcakes = 0
    for i in calorie:
        total += i * pow(2, number_of_cupcakes)
        number_of_cupcakes += 1
    return total

n = int(input())
calorie = list(map(int, input().rstrip().split()))
result = marcsCakewalk(calorie)
print(result)