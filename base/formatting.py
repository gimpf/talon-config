from typing import List, Union
from enum import Enum
from collections import namedtuple

from talon import Module, Context, actions, ui

Join = Enum("Join", "WithSeparator Smashed")
Word = namedtuple("Word", "value")
Symbol = namedtuple("Symbol", "value")
Formatter = namedtuple("Formatter", "Join Fn")


words_to_keep_lowercase = "a,an,the,at,by,for,in,is,of,on,to,up,and,as,but,or,nor".split(
    ","
)


def surround_phrase(by):
    """Surround the whole phrase with prefix/suffix specified in by."""

    def func(words):
        return [Symbol(by)] + words + [Symbol(by)]

    return Formatter(Join.WithSeparator, func)


def join_words(joiner):
    """Pass through words unchanged, but add a separator between them."""

    def func(words):
        if joiner == "":
            return words
        res = []
        last = len(words) - 1
        for i, v in enumerate(words):
            print(f"word = {type(v)}")
            res.append(v)
            if i != last and isinstance(words[i + 1], Word):
                res.append(Symbol(joiner))
        return res

    return Formatter(Join.Smashed, func)


def first_vs_rest(first_func, rest_func=lambda w: w):
    """Supply one or two transformer functions for the first and rest of
    words respectively.

    Leave second argument out if you want all but the first word to be passed
    through unchanged.
    Set first argument to None if you want the first word to be passed
    through unchanged."""
    if first_func is None:
        first_func = lambda w: w

    def func(words):
        res = []
        first = True
        for val in words:
            if isinstance(val, Symbol):
                # never format previously added symbols
                res.append(val)
                continue
            if first:
                # not unusual to start the list of tokens with
                # an added symbol like __ or ", so we have to
                # scan for the first real word
                first = False
                res.append(Word(first_func(val.value)))
            else:
                res.append(Word(rest_func(val.value)))
        return res

    return Formatter(Join.WithSeparator, func)


def every_word(word_func):
    """Apply one function to every word."""

    def func(words):
        res = []
        for val in words:
            if isinstance(val, Symbol):
                # never format previously added symbols
                res.append(val)
                continue
            res.append(Word(word_func(val.value)))
        return res

    return Formatter(Join.WithSeparator, func)


abbreviations = {
    "command": ["cmd"],
}


def chain(formatters):
    sep = Join.WithSeparator
    for s, _ in formatters:
        if s is Join.Smashed:
            sep = Join.Smashed
            break

    def func(words):
        for _, formatter in formatters:
            words = formatter(words)
        return words

    return Formatter(sep, func)


formatters_dict = {
    "camel": chain(
        [join_words(""), first_vs_rest(lambda w: w, lambda w: w.capitalize())]
    ),
    "pascal": chain([join_words(""), every_word(lambda w: w.capitalize())]),
    "snake": join_words("_"),
    "kebab": join_words("-"),
    "pack": join_words("::"),
    "pointy": join_words("."),
    "slash": join_words("/"),
    "smash": join_words(""),
    "dunder": chain([join_words("_"), surround_phrase("__")]),
    "allcaps": every_word(lambda w: w.upper()),
    "alldown": every_word(lambda w: w.lower()),
    "single quoted": surround_phrase("'"),
    "double quoted": surround_phrase('"'),
    "backtick quoted": surround_phrase("`"),
    "padded": surround_phrase(" "),
    "sentence": first_vs_rest(lambda w: w.capitalize()),
    "title": first_vs_rest(
        lambda w: w.capitalize(),
        lambda w: w.capitalize() if w not in words_to_keep_lowercase else w,
    ),
    "truncate to three": every_word(lambda w: w[:3]),
    "truncate to four": every_word(lambda w: w[:4]),
    "truncate to five": every_word(lambda w: w[:5]),
    "acronym": chain([join_words(""), every_word(lambda w: w[:1])]),
}


def format_text_helper(words, formatterNames):
    if isinstance(formatterNames, str):
        formatterNames = [formatterNames]
    join, formatter = chain([formatters_dict[name] for name in formatterNames])
    words = formatter(words)
    res = ""
    last = len(words) - 1
    for i, v in enumerate(words):
        if join is Join.Smashed or i == last:
            res += v.value
        else:
            res += v.value
            # only add spaces between words, but not between symbols or symbols and words
            if isinstance(v, Word) and isinstance(words[i + 1], Word):
                res += " "
    return res


# parse dragon marks on words
# words = actions.dictate.parse_words(m)
# replace from setting dicate.word_map
# words = actions.dictate.replace_words(words)
# make a sentence
# word = actions.dictate.join_words


mod = Module()
mod.list("formatters", desc="list of formatters")


active_formatters = []


@mod.capture
def formatters(m) -> List[str]:
    "Captures a list of of formatters"


@mod.action
def formatters_format_text(
    text: Union[str, List[str]], fmtrs: Union[str, List[str]]
) -> str:
    """Formats a list of parsed words given a list of formatters"""
    res = ""
    if isinstance(text, list):
        res = format_text_helper([Word(t) for t in text], fmtrs)
    else:
        res = format_text_helper([Word(t) for t in text.split(" ")], fmtrs)
    return res


@mod.action
def formatters_set(fmtrs: Union[str, List[str]]) -> str:
    """Saves a list of formatters for later use"""
    global active_formatters
    active_formatters = fmtrs


@mod.action
def formatters_formatted(text: Union[str, List[str]]) -> str:
    """Formats a text using the saved formatter"""
    return actions.user.formatters_format_text(text, active_formatters)


ctx = Context()
ctx.lists["self.formatters"] = formatters_dict.keys()


@ctx.capture(rule="{self.formatters}+")
def formatters(m):
    return m.formatters_list
