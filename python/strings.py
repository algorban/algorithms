def lcc(str):
    """
    Longest Consecutive Characters
    :param string: string
    :return: character and length of the substring
    """
    if str:
        prev = str[0]
        count = 1
        max_char = str[0]
        max_count = 1
        for i in range(1,len(str)):
            if str[i] == prev:
                count += 1
                prev = str[i]
            else:
                if count > max_count:
                    max_count = count
                    max_char = prev
                count = 1
                prev = str[i]
        return max_char, max_count
    else:
        return None


char, count = lcc("ABAACDDDBBA")
print("Char is {}, length is {}".format(char, count))