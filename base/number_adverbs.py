from talon import Module, Context

# see https://english.stackexchange.com/questions/312527/what-is-the-name-for-the-group-of-words-that-includes-once-twice-and-thri

mod = Module()
mod.list("simple_numeral_adverb", desc="the list of plain numerical adverbs")

@mod.capture(rule="{self.simple_numeral_adverb} | <number> times")
def numeral_adverb(m) -> int:
    """Returns a single numeral adverb like once or four times as an integer"""
    if hasattr(m, "simple_numeral_adverb"):
        return int(m.simple_numeral_adverb)
    else:
        return int(m.number)


ctx = Context()
ctx.lists["self.simple_numeral_adverb"] = {
    "once": "1",
    "one time": "1",
    "twice": "2",
    "thrice": "3",
}
