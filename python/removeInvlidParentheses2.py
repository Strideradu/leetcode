def removeInvalid(s):
    left = 0
    res = ''
    for char in s:
        if char == '(':
            left += 1
            res += char
        elif char == ')':
            if left > 0:
                left -= 1
                res += char

        else:
            res += char

    result = ''
    right = 0
    for char in res[::-1]:
        if char == ')':
            right += 1
            result = char + result

        elif char == '(':
            if right > 0:
                right -= 1
                result = char + result

        else:
            result = char + result

    return result
