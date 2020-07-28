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
            else:
                if count > max_count:
                    max_count = count
                    max_char = prev
                count = 1
                prev = str[i]
        return max_char, max_count
    else:
        return None


def length_of_longest_substring(s):
        """
        Given a string, find the length of the longest consecutive substring without repeating characters.
        :type s: str
        :rtype: int
        """
        idx = 0
        cache ={}
        maxlength = 0
        current_length = 0
        start_pos = 0
        while idx < len(s):
            if s[idx] not in cache:
                cache[s[idx]] = idx
                current_length += 1
            else:
                maxlength = max(current_length, maxlength)
                next_start = cache[s[idx]]+1
                for i in range(start_pos, cache[s[idx]]+1):
                    del cache[s[i]]
                    current_length -= 1
                start_pos = next_start
                cache[s[idx]] = idx
                current_length += 1
            idx += 1
        maxlength = max(current_length, maxlength)
        return maxlength

char, count = lcc("ABAACDDDBBA")
print("Char is {}, length is {}".format(char, count))

print("Max length of consecutive substring of string {} is {}".format("ABAACDDDBBA", length_of_longest_substring("ABAACDDDBBA")))
