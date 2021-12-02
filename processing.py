from earley import CFGrammar, earley


def processing():
    g = CFGrammar()
    n = int(input())
    for i in range(0, n):
        rule = input().split()
        if len(rule) == 1:
            rule.append('')
        assert rule[0].isalpha() and rule[0].isupper()
        assert rule[1].isalpha() or rule[1] == '' or rule[1] == '1'
        g.add_rule(rule[0], rule[1])
    return g


if __name__ == '__main__':
    g = processing()
    w = input()
    print(earley(g, w))
