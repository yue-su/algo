def commaSeparate(names):
    res = []
    for i in range(len(names)):
        if res:
            if i == len(names) - 1:
                res.append(" and ")
            else:
                res.append(", ")
        res.append(names[i])

    return "".join(res)

#before handle each item, check if it's index is already the last one
#also check if there is a item before it


print(commaSeparate([]) == "")
print(commaSeparate(["Sophie"]) == "Sophie")
print(commaSeparate(["Daniel", "Craig"]) == "Daniel and Craig")
print(commaSeparate(["Oliver", "Pixel", "Fido"]) == "Oliver, Pixel and Fido")
print(commaSeparate(["Jono", "Paavo", "Tony", "me"]) == "Jono, Paavo, Tony and me")
print(commaSeparate(["John", "John", "John"]) == "John, John and John")
print(commaSeparate(["Sean", "John", "Sean"]) == "Sean, John and Sean")