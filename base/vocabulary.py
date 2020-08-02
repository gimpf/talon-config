from talon import Module, Context

mod = Module()
mod.list("vocabulary", "dictionary of words to replace w/other stuff")


@mod.capture(rule="{user.vocabulary}")
def vocabulary(m) -> str:
    """returns a single mapped word from the vocabulary as string"""
    return m.vocabulary


@mod.capture(rule="(<word> | <user.vocabulary>)")
def word(m) -> str:
    return str(m)


@mod.capture(rule="(<phrase> | <user.vocabulary>)+")
def phrase(m) -> str:
    return str(m)


simple_words = [
    "admin",
]

complex_words = {
    # 'coffee cup': 'Kafka',
}

vocabulary = {k: k for k in simple_words}
vocabulary.update(complex_words)

ctx = Context()
ctx.settings["dictate.word_map"] = vocabulary
ctx.lists["user.vocabulary"] = vocabulary
