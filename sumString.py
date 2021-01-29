def sum_str(a, b):
    # happy coding !
    if a == None or b == None or (a == "" and b == ""):
        return "0"
    
    if a == "":
        return b
    if b == "":
        return a

    try:
        c = int(a)
        d = int(b)
        return f"{c + d}"
    except:
        return "0"


print(sum_str("4", "5"))
print(sum_str("0", "5"))
print(sum_str("4", "0"))
print(sum_str(None, "5"))
print(sum_str("", ""))
print(sum_str("", "5"))
print(sum_str("4", "a"))