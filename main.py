import sys

def is_one_to_one(s1, s2):
    mapping = {} #maps one char in s1 to s2

    if len(s1) != len(s2): #one_to_one only if same length
        return False

    for i in range(len(s1)):
        if s1[i] in mapping and mapping[s1[i]] != s2[i]:
            return False #maps to different chars
        else:
            mapping[s1[i]] = s2[i]

    return True

def main():
    if len(sys.argv) != 3:
        print('false')
        return False

    if is_one_to_one(sys.argv[1], sys.argv[2]):
        print('true')
    else:
        print('false')


if __name__ ==  "__main__":
    main()
