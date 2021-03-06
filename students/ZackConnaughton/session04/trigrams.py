#!/usr/bin/env python

"""
trigrams!
"""
import random

def strip_punct(s):
    output = s
    if '--' in output:
        output = output.replace('--', ' ')
    if '"' in output:
        output = output.replace('"', '')
    return output


words = 'I wish I may I wish I might'

def make_trigrams(words):
    tris = {}
    just_words = strip_punct(words)
    words_list = just_words.split()
    for i in range(len(words_list) - 2):
        w1 = words_list[i].lower()
        w2 = words_list[i + 1].lower()
        w3 = words_list[i + 2].lower()
        pair = (w1, w2)
        if pair in tris:
            if not tris[pair] == list(w3):
                tris[pair].append(w3)
        else:
            tris[pair] = [w3]
    return tris

def long_file(file):
    f = open(file, 'r', encoding='utf8')
    output_tris = make_trigrams(f.read())
    f.close()
    return output_tris


tris = make_trigrams(words)
long_tris = long_file('sherlock_small.txt')


def output_next(dict_key, tris):
    output = random.choice(tris[dict_key])
    return output


def seed_tris(tris):
    print(type(tris.keys()))
    key = random.choice(list(tris.keys()))
    return str(key[0]) + " " + str(key[1]) + " "


def trigrams_text(file, length=30):
    tris = long_file(file)
    output_string = seed_tris(tris)

    while len(output_string.split()) < length:
        sentence = output_string.split()
        w1 = sentence[-2].lower()
        w2 = sentence[-1].lower()
        dict_key = (w1, w2)
        output_string += output_next(dict_key, tris) + " "
    return(output_string)

if __name__ == '__main__':
    make_trigrams(words)
    #print(long_file('sherlock_small.txt'))
    print(trigrams_text('sherlock_small.txt'))
    print(trigrams_text('source/RobinHood.txt', 500))
