def lcs(string1: str, string2: str):
    l1: int
    l1, l2, ans = len(string1), len(string2), ''
    lcss, path = [[0]], [['NaN']]
    for i1 in range(l1):
        lcss[0].append(0)
        path[0].append('NaN')

    for i2 in range(1, l2+1):
        lcss.append([0])
        path.append(['NaN'])
        for i1 in range(1, l1+1):
            if lcss[i2][i1-1] < lcss[i2-1][i1]:
                lcss[i2].append(lcss[i2-1][i1])
                path[i2].append('s2')
            else:
                lcss[i2].append(lcss[i2][i1-1])
                path[i2].append('s1')
            if (string1[i1-1] == string2[i2-1]) and ((lcss[i2-1][i1-1] + 1) > lcss[i2][i1]):
                lcss[i2][i1], path[i2][i1] = lcss[i2-1][i1-1] + 1, 'both'

#    for i in range(len(lcss)):
#        print(lcss[i], path[i])

    while l1 and l2:
        if path[l2][l1] == 'both':
            ans += string1[l1-1]
            l1, l2 = l1-1, l2-1
        elif path[l2][l1] == 's1':
            l1 -= 1
        elif path[l2][l1] == 's2':
            l2 -= 1
        else:
            break

    return ans[::-1]


a = lcs(input('first string: '), input('second string: '))
print('Longest Common Subsequence is {0} with {1} characters'.format(a, len(a)))
