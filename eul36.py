def is_double_pali(x):
    a = str(x)
    b = str(bin(x))[2:]
    if a[-1: :-1] == a and b[-1: :-1] == b:
        return True
doubles = [i for i in range(1000001) if is_double_pali(i)]
print(sum(doubles))