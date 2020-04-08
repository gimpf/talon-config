from talon import Module, Context

mod = Module()
mod.list("vocabulary", "dictionary of words to replace w/other stuff")

@mod.capture(rule='({self.vocabulary}| <word>)')
def word(m) -> str:
    """word returns a single word as string"""
    if hasattr(m, 'word'):
        return m.word
    return m.vocabulary

ctx = Context()
ctx.lists['self.vocabulary'] = {
    "coffee cup": "kafka"
}
