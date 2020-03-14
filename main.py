
def is_one_to_one(s1, s2):
    d = {}
    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        if s1[i] in d:
            if d[s1[i]] != s2[i]:
                return False
        else:
            d[s1[i]] = s2[i]
    return True

def test():
    print(is_one_to_one("abc", "bcd"))
    print(is_one_to_one("foo", "bar"))
    print(is_one_to_one("bar", "foo"))
    print(is_one_to_one("", ""))
    print(is_one_to_one("a", ""))
    print(is_one_to_one("door", "door"))
    print(is_one_to_one("doora", "baara"))


test()

