from talon import Module, Context

mod = Module()
mod.list("vocabulary", "dictionary of words to replace w/other stuff")


@mod.capture(rule='{self.vocabulary}')
def mapped_word(m) -> str:
    """word returns a single mapped word from the vocabulary as string"""
    return m.vocabulary


@mod.capture(rule='(<user.mapped_word> | <phrase>)+')
def text(m) -> str:
    return str(m)


ctx = Context()
ctx.lists['self.vocabulary'] = {
    "coffee cup": "kafka"
}

# alternatively, w/o translation
# ctx.lists['self.vocabulary'] = [
#     "kafka",
#     "varkelshorp"
# ]
