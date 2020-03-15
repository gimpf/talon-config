# from knausj_talon/code/formatting.py
from talon import Module, Context, actions, ui
from typing import List, Union

words_to_keep_lowercase = "a,an,the,at,by,for,in,is,of,on,to,up,and,as,but,or,nor".split(
    ",")
NOSEP = True
SEP = False


def surround(by):
    """Surround the whole phrase with prefix/suffix specified in by."""
    def func(i, word, last):
        if i == 0:
            word = by + word
        if last:
            word += by
        return word
    return func


def join_words(joiner):
    """Pass through words unchanged, but add a separator between them."""
    def formatter_function(i, word, _):
        return word if i == 0 else joiner + word
    return (NOSEP, formatter_function)


def first_vs_rest(first_func, rest_func=lambda w: w):
    """Supply one or two transformer functions for the first and rest of
    words respectively.

    Leave second argument out if you want all but the first word to be passed
    through unchanged.
    Set first argument to None if you want the first word to be passed
    through unchanged."""
    if first_func is None:
        def first_func(w): return w

    def formatter_function(i, word, _):
        return first_func(word) if i == 0 else rest_func(word)
    return formatter_function


def every_word(word_func):
    """Apply one function to every word."""
    def formatter_function(i, word, _):
        return word_func(word)
    return formatter_function


def format_text_helper(words, fmtrs):
    tmp = []
    spaces = True
    for i, w in enumerate(words):
        for name in reversed(fmtrs):
            smash, func = formatters_dict[name]
            w = func(i, w, i == len(words) - 1)
            spaces = spaces and not smash
        tmp.append(w)
    words = tmp

    sep = " " if spaces else ""
    return sep.join(words)

# parse dragon marks on words
# words = actions.dictate.parse_words(m)
# replace from setting dicate.word_map
# words = actions.dictate.replace_words(words)
# make a sentente
# word = actions.dicate.join_words


formatters_dict = {
    "dunder": (NOSEP, first_vs_rest(lambda w: "__%s__" % w)),
    "camel": (NOSEP, first_vs_rest(lambda w: w, lambda w: w.capitalize())),
    "pascal": (NOSEP, every_word(lambda w: w.capitalize())),  # "hammer"
    "snake": (NOSEP, first_vs_rest(lambda w: w.lower(), lambda w: "_" + w.lower())),
    "smash": (NOSEP, every_word(lambda w: w)),
    "kebab": join_words("-"),
    "packed": join_words("::"),
    "dotted": join_words("."),
    "slasher": (NOSEP, every_word(lambda w: "/" + w)),

    "allcaps": (SEP, every_word(lambda w: w.upper())),
    "alldown": (SEP, every_word(lambda w: w.lower())),

    "single quoted": (SEP, surround('"')),
    "double quoted": (SEP, surround("'")),
    "backtick quoted": (SEP, surround("`")),
    "padded": (SEP, surround(" ")),

    "sentence": (SEP, first_vs_rest(lambda w: w.capitalize())),
    "title": (SEP, lambda i, word, _:  word.capitalize() if i == 0 or word not in words_to_keep_lowercase else word)
}

mod = Module()
mod.list('formatters', desc='list of formatters')


@mod.capture
def formatters(m) -> List[str]:
    "Captures a list of of formatters"


@mod.action_class
class Actions:
    def formatters_format_text(text: Union[str, List[str]], fmtrs: List[str]) -> str:
        """Formats a list of parsed words given a list of formatters"""
        res = ""
        if isinstance(text, list):
            res = format_text_helper(text, fmtrs)
        else:
            res = format_text_helper(text.split(" "), fmtrs)
        return res


ctx = Context()
ctx.lists['self.formatters'] = formatters_dict.keys()


@ctx.capture(rule='{self.formatters}+')
def formatters(m):
    return m.formatters_list
