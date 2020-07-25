# from knausj_talon/code/formatting.py
from talon import Module, Context, actions, ui
from typing import List, Union

words_to_keep_lowercase = "a,an,the,at,by,for,in,is,of,on,to,up,and,as,but,or,nor".split(
    ",")
NOSEP = True
SEP = False


def surround_phrase(by):
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


abbreviations = {
    "command": ["cmd"],
}


def chain_formatters(formatters):
    smash = SEP
    for s, _ in formatters:
        if s == NOSEP:
            smash = NOSEP
            break

    def formatter_function(i, word, isLast):
        for _, func in reversed(formatters):
            print(f"1. {word}")
            word = func(i, word, isLast)
            print(f"2. {word} - {type(word)} - after {func}")
        return word
    return (smash, formatter_function)


formatters_dict = {
    "camel": (NOSEP, first_vs_rest(lambda w: w, lambda w: w.capitalize())),
    "pascal": (NOSEP, every_word(lambda w: w.capitalize())),
    "snake": join_words("_"),
    "kebab": join_words("-"),
    "pack": join_words("::"),
    "dotted": join_words("."),
    "slash": join_words("/"),
    "dunder": (NOSEP, surround_phrase("__")),
    "smash": join_words(""),

    "allcaps": (SEP, every_word(lambda w: w.upper())),
    "alldown": (SEP, every_word(lambda w: w.lower())),

    "single quoted": (SEP, surround_phrase("'")),
    "double quoted": (SEP, surround_phrase('"')),
    "backtick quoted": (SEP, surround_phrase("`")),
    "padded": (SEP, surround_phrase(" ")),

    "sentence": (SEP, first_vs_rest(lambda w: w.capitalize())),
    "title": (SEP, lambda i, word, _: word.capitalize() if i == 0 or word not in words_to_keep_lowercase else word),

    "truncate to three": (SEP, every_word(lambda w: w[:3])),
    "truncate to four": (SEP, every_word(lambda w: w[:4])),
    "truncate to five": (SEP, every_word(lambda w: w[:5])),

    "acronym": (NOSEP, every_word(lambda w: w[:1]))
}


def format_text_helper(words, formatterNames):
    if isinstance(formatterNames, str):
        formatterNames = [formatterNames]
    formatters = [formatters_dict[name] for name in formatterNames]
    smash, formatter = chain_formatters(formatters)
    tmp = []
    for i, w in enumerate(words):
        w = str(w)
        w = formatter(i, w, i == len(words) - 1)
        tmp.append(w)
    words = tmp

    sep = " " if smash == SEP else ""
    return sep.join(words)

# parse dragon marks on words
# words = actions.dictate.parse_words(m)
# replace from setting dicate.word_map
# words = actions.dictate.replace_words(words)
# make a sentence
# word = actions.dictate.join_words


mod = Module()
mod.list('formatters', desc='list of formatters')


@mod.capture
def formatters(m) -> List[str]:
    "Captures a list of of formatters"


@mod.action_class
class Actions:
    def formatters_format_text(text: Union[str, List[str]], fmtrs: Union[str,List[str]]) -> str:
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
