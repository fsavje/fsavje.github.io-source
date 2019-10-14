#!/usr/bin/env python

import json
import jinja2

def lr_bracket(input):
    return '{' + input + '}'

def l_bracket(input):
    return '{' + input

def r_bracket(input):
    return input + '}'

def lr_space(input):
    return ' ' + input + ' '

def l_space(input):
    return ' ' + input

def r_space(input):
    return input + ' '

def escape_latex(input):
    return input.replace('&', '\\&')

def remove_first_word(input):
    first, _, rest = input.partition(" ")
    return rest or first

with open('../data/cv.json') as cv_file:
    cv_data = json.load(cv_file)

env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
env.filters.update({
    'lr_bracket' : lr_bracket,
    'l_bracket' : l_bracket,
    'r_bracket' : r_bracket,
    'lr_space' : lr_space,
    'l_space' : l_space,
    'r_space' : r_space,
    'remove_first_word' : remove_first_word,
    'escape_latex' : escape_latex
})
env.get_template('cv_template.tex').stream(cv_data).dump('fredrik-savje-cv.tex')
