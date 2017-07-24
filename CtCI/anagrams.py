def number_needed(a, b):
    an1_dict = {}
    an2_dict = {}

    deletions = 0

    for x in a:
        if x not in an1_dict:
                an1_dict[str(x)] = 1
        else:
                an1_dict[str(x)] += 1

    for y in b:
        if y not in an2_dict:
                an2_dict[str(y)] = 1
        else:
                an2_dict[str(y)] += 1

    for k1, v1 in an1_dict.items():
        if k1 not in an2_dict:
                deletions += v1
        else:
                if an2_dict[k1] != v1:
                     deletions += abs(an2_dict[k1] - v1)

    for k2, v2 in an2_dict.items():
        if k2 not in an1_dict:
            deletions += v2
        else:
            if an2_dict[k2] != v2:
                deletions += abs(an1_dict[k2] - v2)

    return deletions

a = input().strip()
b = input().strip()

print(number_needed(a, b))
