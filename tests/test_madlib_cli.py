
from madlib_cli.madlib_cli import parse,fun_input,read_template,fun_input_test

def test_one():
    expected="""
Make Me A Video Game!

I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister 
and plan to steal her {Adjective} {Plural Noun}!
What are a {Large Animal} and backpacking {Small Animal} to do? 
Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} 
and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair.
 There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game,
 along with hundreds of other goodies for you to find.
"""
    actual=read_template(open('assets/text.txt'))
    assert expected.strip() == actual


def test_two():
    expected=('{Adjective}{Adjective}{Noun}',['{Adjective}', '{Adjective}','{Noun}'])
    actual=parse(open('assets/text_test.txt').read())
    assert expected==actual

def test_three():
    a=('beutiful','greated','trip')
    b="It was a beutiful and greated trip."
    expected=b
    actual=fun_input_test(open('assets/text_test.txt').read(),a)
    assert expected==actual

def test_four():
    a=('beutiful','greated','trip')
    b="It was a beutiful and greated trip."
    expected=b
    actual=fun_input_test(open('assets/text_test.txt').read(),a)
    assert expected==actual

