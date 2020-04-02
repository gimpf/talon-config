# from knausj_talon/code/keys.py
from talon import Module, Context, actions
import sys

debug = False

# Talon Alphabet
# letters_alphabet = " ".join([
#     'air bat cap drum each fine gust',
#     'harp sit jury crunch look made near',
#     'odd pit quench red sun trap urge vest',
#     'whale plex yank zip']).split(' ')

# My approach
# quench -> quass (disambiguates better from crunch, quass has a strong U and then long A vowel, very different from everything else)
# jury -> joy (easier to pronounce, jury recognizes just as as anything but j for me)
# urge -> use (-"-)
# sit -> inner (disambiguates w/zip, very microphone, bg-noise dependent, english z unnatural sound for me)
# whale -> wave (bad to pronounce for me, is confused with bat (sic!) often, otherwise red, sun ...)
# bat -> buy (bat seems to be like at: always chosen whether it was meant to or not)
# odd -> oppo (odd is too similar to some noises between words, like 'control trap' is recognized as 'control odd trap')
letters_alphabet = " ".join([
    'air buy cap drum each fine gust',
    'harp inner joy kiss look made near',
    'oppo pit quass red sun trap use vest',
    'wave plex yank zip']).split(' ')

# NATO alphabet
# letters_alphabet = " ".join([
#     'alpha bravo charlie delta echo foxtrot golf',
#     'hotel india juliett kilo lima mike november',
#     'oscar papa quebec romeo sierra tango uniform',
#     'victor whiskey x-ray yankee zulu']).split(' ')

letters_letters = 'abcdefghijklmnopqrstuvwxyz'
letters_alphabet_to_letter = dict(zip(letters_alphabet, letters_letters))
symbols_alphabet_to_symbol = {
    'point': '.',
    'comma': ',',
    'colon': ':',
    'semicolon': ';',
    'question': '?',
    'exclamation': '!',

    'single quote': "'",
    'double quote': '"',
    'back tick': '`',

    'left paren': '(',
    'right paren': ')',
    'left brace': '{',
    'right brace': '}',
    'left bracket': '[',
    'right bracket': ']',
    'less than':    '<',
    'greater than': '>',

    'slash': '/',
    'backslash': '\\',

    'tilde': '~',
    'equals': '=',
    'plus': '+',
    'minus': '-', 'dash': '-',
    'under score': '_',
    'asterisk': '*',
    'hash': '#',
    'percent': '%',
    'caret': '^',
    'commercial at': '@',
    'amper': '&',  # ampersand is often confused with percent
    'pipe': '|',

    'dollar': '$',
}
specialchars_alphabet_to_chart = {
    'tab':      'tab',
    'enter':    'enter',
    'space':    'space',
    'escape':   'escape',
    'backspace': 'backspace',
    'delete':   'delete',
}
# todo digits should have a single definition shared across numbers/ordinals and here
fkey_num_to_word = 'zero one two three four five six seven eight nine ten eleven twelve'.split(' ')
specialchars_alphabet_to_chart.update(
    {f"F {fkey_num_to_word[i]}": f"f{i}" for i in range(1, 13)})
navs_word_to_key = {
    'left':  'left',
    'right': 'right',
    'upward': 'up',
    'down':  'down',

    'home':      'home',
    'page up':   'pageup',
    'page down': 'pagedown',
    'end':       'end',
}
modifiers_word_to_key = {
    'shift':   'shift',
    'control': 'ctrl',
    'alt':     'alt',    'option':  'alt',
    'command': 'cmd',
    'ralt':    'ralt',
    'super':   'super',
    'hyper':   'hyper',
}

mod = Module()
mod.list('letter', desc='The spoken phonetic alphabet')
mod.list('symbol', desc='All symbols from the keyboard')
mod.list('special', desc='All special keys')
mod.list('nav',      desc='All navigation keys')
mod.list('modifier', desc='All modifier keys')


@mod.capture
def letter(m) -> str:
    "One letter key"


@mod.capture
def letters(m) -> str:
    "Multiple letter keys"

# a single digit capture is defined by the numbers/cardinals module
@mod.capture
def digits(m) -> str:
    "Multiple digit keys"


@mod.capture
def symbol(m) -> str:
    "One symbol key"


@mod.capture
def symbols(m) -> str:
    "Multiple symbol keys"


@mod.capture
def special(m) -> str:
    "One special key"


@mod.capture
def specials(m) -> str:
    "Multiple special keys"


@mod.capture
def nav(m) -> str:
    "One navigation key"


@mod.capture
def navs(m) -> str:
    "List of one or more navigation keys"


@mod.capture
def any(m) -> str:
    "Any one non-modifier key"


@mod.capture
def anys(m) -> str:
    "Multiple non-modifier keys"


@mod.capture
def modifiers(m) -> str:
    "One or more modifier keys"


@mod.capture
def chord(m) -> str:
    "Modifiers and other keys"


@mod.capture
def partialchord(m) -> str:
    "Modifiers and optionally other keys"


current_modifiers = set()


@mod.action_class
class LetterActions:
    def chord(mods: str, keys: str) -> str:
        """chord"""
        keys_sep = keys.split(" ")
        res = ""
        if len(keys_sep) == 1:
            res = f"{mods}-{keys}"
        else:
            res = f"{mods}:down {keys} {mods}:up"
        print(f"chord: {res}")
        return res

    def startChord(partialChord: str):
        """press modifiers down and type keys, w/o lifting modifiers up again"""
        global current_modifiers
        keys = partialChord.split(" ", 1)
        if len(keys) < 1:
            return
        mods = keys[0]
        current_modifiers |= set(mods.split("-"))
        res = f"{mods}:down {keys[1] if len(keys) > 1 else ''}"
        print(f"start chording {res}")
        actions.key(res)

    def finishChord():
        """lift all active modifiers up"""
        global current_modifiers
        toFinish = list(current_modifiers)
        res = "-".join(toFinish) + ":up"
        actions.key(res)
        current_modifiers.clear()
        print(f"lifted chorded {res}")

    def doChord(mods: str, keys: str):
        """do chord"""
        actions.key(LetterActions.chord(mods, keys))

    def get_alphabet():
        """Provides the alphabet dictionary"""
        return ctx.lists['self.letter']

    def get_symbols():
        """Provide the symbol dictionary"""
        return ctx.lists['self.symbol']


ctx = Context()
ctx.lists['self.letter'] = letters_alphabet_to_letter
ctx.lists['self.symbol'] = symbols_alphabet_to_symbol
ctx.lists['self.special'] = specialchars_alphabet_to_chart
ctx.lists['self.nav'] = navs_word_to_key
ctx.lists['self.modifier'] = modifiers_word_to_key


@ctx.capture(rule='{self.letter}')
def letter(m):
    return m.letter


@ctx.capture(rule='{self.letter}+')
def letters(m):
    return " ".join(m.letter_list)


@ctx.capture(rule='<user.digit>+')
def digits(m) -> str:
    return " ".join(m.digit_list)


@ctx.capture(rule='{self.symbol}')
def symbol(m):
    return m.symbol


@ctx.capture(rule='{self.symbol}+')
def symbols(m):
    return " ".join(m.symbol_list)


@ctx.capture(rule='{self.special}')
def special(m):
    return m.special


@ctx.capture(rule='{self.special}+')
def specials(m):
    return " ".join(m.special_list)


@ctx.capture(rule='{self.nav}')
def nav(m) -> str:
    return m.nav


@ctx.capture(rule='{self.nav}+')
def navs(m) -> str:
    return " ".join(m.nav_list)


@ctx.capture(rule='(<self.letter> | <digits> | <self.symbol> | <self.special> | <self.nav>)')
def any(m) -> str:
    return str(m)


@ctx.capture(rule='<self.any>+')
def anys(m) -> str:
    return " ".join(m.any_list)


@ctx.capture(rule='{self.modifier}+')
def modifiers(m):
    return "-".join(set(m.modifier_list))


@ctx.capture(rule='<self.modifiers> <self.anys>')
def chord(m) -> str:
    return actions.user.chord(m.modifiers, m.anys)


@ctx.capture(rule='<self.modifiers> <self.any>*')
def partialchord(m) -> str:
    return " ".join([m.modifiers] + (m.any_list if hasattr(m, "any_list") else []))
