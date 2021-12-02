from earley import *


def test_add_rule():
    grammar = CFGrammar()
    grammar.add_rule('S', 'aSbS')
    grammar.add_rule('S', 'bSaS')
    grammar.add_rule('S', '1')
    assert grammar.rules == {'S': ['aSbS', 'bSaS', '1']}


def test_earley():
    grammar = CFGrammar()
    grammar.add_rule('S', 'aSbS')
    grammar.add_rule('S', 'bSaS')
    grammar.add_rule('S', '1')
    word = 'abb'
    assert not earley(grammar, word)


def test_scan():
    word = 'abc'
    conf_list_storage = [set(), set()]
    conf_list_storage[0].add(Configuration('S', '.abc', 0))
    scan(conf_list_storage[0], conf_list_storage[1], word, 1)

    assert conf_list_storage[1] == {Configuration('S', 'a.bc', 0)}


def test_predict():
    grammar = CFGrammar()
    grammar.add_rule('U', 'xyz')
    conf_list_storage = [set()]
    conf_list_storage[0].add(Configuration('S', '.Ubc', 0))

    predict(conf_list_storage[0], grammar, 0)

    assert conf_list_storage[0] == {Configuration('S', '.Ubc', 0), Configuration('U', '.xyz', 0)}


def test_complete():
    conf_list_storage = [
        {Configuration('A', 'ab.Bcd', 2)},
        {Configuration('B', 'abT.', 0)}
    ]

    complete(conf_list_storage, 1)

    assert conf_list_storage[1] == {Configuration('B', 'abT.', 0), Configuration('A', 'abB.cd', 2)}


def test_whole_true():
    grammar = CFGrammar()
    grammar.add_rule('S', 'aTb')
    grammar.add_rule('T', 'bba')

    assert earley(grammar, 'abbab')


def test_whole_false():
    grammar = CFGrammar()
    grammar.add_rule('S', 'aTb')
    grammar.add_rule('T', 'bba')

    assert not earley(grammar, 'abab')


test_add_rule()
test_earley()
test_scan()
test_predict()
test_complete()
test_whole_true()
test_whole_false()
