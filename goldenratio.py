def get_golden_ratio(num):
    list_fibo = sorted(get_fibo_num(num), reverse=True)
    sum = 0
    for i in range(len(list_fibo)):
        if list_fibo[i] <= num:
            num = num - list_fibo[i]
            sum += list_fibo[i+1]
    return sum
