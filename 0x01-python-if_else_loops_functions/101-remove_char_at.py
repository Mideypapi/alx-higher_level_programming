def remove_char_at(str, n):
    new_str = ""
    for x in range(len(str)):
        if x == n:
            continue
        new_str += str[x]
    return (new_str)
