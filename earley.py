from classes import CFGrammar, Configuration
from typing import List, Set


def scan(conf_list: Set[Configuration], conf_list_next: Set[Configuration], word: str, j: int):
    if j == 0:
        return
    for conf in conf_list:
        if conf.finish[-1] != '.' and conf.finish[conf.finish.index('.') + 1].islower():
            dot_index = conf.finish.index('.')
            if conf.finish[dot_index + 1] == word[j - 1]:
                new_conf_finish = conf.finish[:dot_index] + conf.finish[dot_index + 1]\
                                  + '.' + conf.finish[dot_index + 2:]
                conf_list_next.add(Configuration(conf.start, new_conf_finish, conf.i))


def predict(conf_list: Set[Configuration], grammar: CFGrammar, j: int):
    new_conf = set()
    for conf in conf_list:
        if conf.finish[-1] != '.' and conf.finish[conf.finish.index('.') + 1].isupper():
            dot_index = conf.finish.index('.')
            for letter, finish_set in grammar.rules.items():
                if letter == conf.finish[dot_index + 1]:
                    for finish in finish_set:
                        new_conf.add(Configuration(letter, '.' + finish, j))
    for item in new_conf:
        conf_list.add(item)


def complete(conf_list: List[Set[Configuration]], j: int):
    new_conf = set()
    for conf_low in conf_list[j]:
        if conf_low.finish[-1] == '.':
            for conf_up in conf_list[conf_low.i]:
                if conf_up.finish[-1] != '.' and conf_up.finish[conf_up.finish.index('.') + 1].isupper():
                    dot_index = conf_up.finish.index('.')
                    if conf_low.start == conf_up.finish[dot_index + 1]:
                        new_conf_up_finish = conf_up.finish[:dot_index] + conf_up.finish[dot_index + 1] +\
                                             '.' + conf_up.finish[dot_index + 2:]
                        new_conf.add(Configuration(conf_up.start, new_conf_up_finish, conf_up.i))
    for item in new_conf:
        conf_list[j].add(item)


def earley(grammar: CFGrammar, word: str):
    conf_list_storage: List[Set[Configuration]]
    assert 'Z' not in grammar.rules.keys()
    grammar.add_rule('Z', grammar.start_letter)
    conf_list_storage = [set() for i in range(len(word) + 1)]

    conf_list_storage[0].add(Configuration('Z', '.{}'.format(grammar.start_letter), 0))

    for j in range(len(word) + 1):
        if j > 0:
            scan(conf_list_storage[j - 1], conf_list_storage[j], word, j)
        while True:
            old_size = len(conf_list_storage[j])
            complete(conf_list_storage, j)
            predict(conf_list_storage[j], grammar, j)
            if len(conf_list_storage[j]) == old_size:
                break

    return Configuration('Z', '{}.'.format(grammar.start_letter), 0) in conf_list_storage[len(word)]
