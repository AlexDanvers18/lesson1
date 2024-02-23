
def get_summ(first, second, delimiter='&'):
    first = str(first)
    second = str(second)
    summ = first + delimiter + second
    print(summ.upper())

get_summ("Learn", "python")