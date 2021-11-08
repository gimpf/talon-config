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
# bat -> buy (bat seems to be like at: always chosen whether it was meant to or not)
# sit -> ivy (disambiguates w/zip, very microphone, bg-noise dependent, english z unnatural sound for me)
# jury -> joy (easier to pronounce, jury recognizes just as as anything but j for me)
# crunch -> kiss
# # odd -> oppo (odd is too similar to some noises between words, like 'control trap' is recognized as 'control odd trap')
# # b2-large doesn't like this quench -> quass (quass has a strong U and then long A vowel, very different from everything else)
# urge -> use (-"-)
# whale -> wave (bad to pronounce for me, is confused with bat (sic!) often, otherwise red, sun ...)
letters_alphabet = " ".join(
    [
        "air buy cap drum each fine gust",
        "harp ivy joy kiss look made near",
        "odd pit quench red sun trap use vest",
        "wave plex yank zip",
    ]
).split(" ")


letters_letters = "abcdefghijklmnopqrstuvwxyz"
letters_alphabet_to_letter = dict(zip(letters_alphabet, letters_letters))
symbols_alphabet_to_symbol = {
    "point": ".",
    # "dot": ".",
    "comma": ",",
    "colon": ":",
    "semicolon": ";",
    "question": "?",
    "inverted question": "¿",
    "exclamation": "!",
    "inverted exclamation": "¡",
    "interrobang": "‽",
    "single quote": "'",
    "double quote": '"',
    "back tick": "`",
    "grave": "`",
    "acute": "´",
    "left paren": "(",
    "right paren": ")",
    "left brace": "{",
    "right brace": "}",
    "left bracket": "[",
    "right bracket": "]",
    "left angle": "⟨",
    "right angle": "⟩",
    "less than": "<",
    "greater than": ">",
    "slash": "/",
    "backslash": "\\",
    "tilde": "~",
    "equals": "=",
    "plus": "+",
    "multiplication": "×",
    "division": "÷",
    "minus": "-",
    "dash": "-",
    "plus or minus": "±",
    "minus or plus": "∓",
    "logical not": "¬",
    "underscore": "_",
    "asterisk": "*",
    "hash": "#",
    "percent": "%",
    "per mille": "‰",
    "basis point": "‱",
    "caret": "^",
    "degree": "°",
    "commercial at": "@",
    "amper": "&",  # ampersand is often confused with percent
    "pipe": "|",
    "section": "§",
    "diameter": "⌀",
    "micro": "µ",
    "irony": "⸮",
    "pilcrow": "¶",
    "dagger": "†",
    "double dagger": "‡",
    "superscript one": "¹",
    "superscript two": "²",
    "superscript three": "³",
    "ellipsis": "…",
    "bullet point": "•",
    "white bullet point": "◦",
    "triangle bullet point": "‣",
    "trademark": "™",
    "registered trademark": "®",
    "copyright": "©",
    "left guillemets": "«",
    "right guillemets": "»",
    "prime": "′",
    "double prime": "″",
    "triple prime": "‴",
    "dollar": "$",
    "cent": "¢",
    "pound": "£",
    "yen": "¥",
    "euro": "€",
    "space": "space",  # also mapped in special char
}
specialchars_alphabet_to_char = {
    "tabby": "tab",
    "enter": "enter",
    "space": "space",  # also mapped in symbol
    "escape": "escape",
    "backspace": "backspace",
    "delete": "delete",
}
# todo digits should have a single definition shared across numbers/ordinals and here
fkey_num_to_word = "zero one two three four five six seven eight nine ten eleven twelve".split(
    " "
)
# use foil as function key prefix for better recognition in context ("eff four" performs poorly)
specialchars_alphabet_to_char.update(
    {f"foil {fkey_num_to_word[i]}": f"f{i}" for i in range(1, 13)}
)
navs_word_to_key = {
    "left": "left",
    "right": "right",
    "up": "up",
    "down": "down",
    "home": "home",
    "page up": "pageup",
    "page down": "pagedown",
    "end": "end",
}
modifiers_word_to_key = {
    "shift": "shift",
    # use 'counter' instead of 'control' because between 'control' and
    # the next letter, w2l often recognizes short letters like air or red
    # note: this might not be the case anymore w/new model, but also counter is
    # much easier to pronounce
    "counter": "ctrl",
    # "alt": "alt",
    # "option": "alt",
    # "alley": "alt",
    "fly": "alt",
    # "command": "cmd",
    # "R alt": "ralt",
    "super": "super",
    # "hyper": "hyper", # doesn's exist on windows?
}

mod = Module()
mod.list("letter", desc="The spoken phonetic alphabet")
mod.list("symbol", desc="All symbols from the keyboard")
mod.list("special", desc="All special keys")
mod.list("nav", desc="All navigation keys")
mod.list("modifier", desc="All modifier keys")
mod.list("media", desc="All media keys")



@mod.capture(rule="[(uppercase | large)] {user.letter}")
def letter(m) -> str:
    "One letter key, optionally uppercase"
    letter = m[0]
    if m[0] == "uppercase" or m[0] == "large":
        letter = m[1]
    # letter = letters_alphabet_to_letter[letter]
    if m[0] == "uppercase" or m[0] == "large":
        return letter.upper()
    return letter


@mod.capture(rule="<user.letter>+")
def letters(m) -> str:
    "Multiple letter keys"
    return " ".join(m.letter_list)


# a single digit capture is defined by the numbers/cardinals module
@mod.capture(rule="<user.digit>+")
def digits(m) -> str:
    "Multiple digit keys"
    return " ".join(m.digit_list)


@mod.capture(rule="{self.symbol}")
def symbol(m) -> str:
    "One symbol key"
    return m.symbol


@mod.capture(rule="{self.symbol}+")
def symbols(m) -> str:
    "Multiple symbol keys"
    return " ".join(m.symbol_list)


@mod.capture(rule="(<self.letter> | <user.digit> | <self.symbol>)")
def ordinary(m) -> str:
    "One character of either letter, digit or symbol"
    return str(m)


@mod.capture(rule="<self.ordinary>+")
def ordinaries(m) -> str:
    "Multiple ordinary characters"
    return " ".join(m.ordinary_list)

@mod.capture(rule="{self.special}")
def special(m) -> str:
    "One special key"
    return m.special


@mod.capture(rule="{self.special}+")
def specials(m) -> str:
    "Multiple special keys"
    return " ".join(m.special_list)


@mod.capture(rule="{self.nav}")
def nav(m) -> str:
    "One navigation key"
    return m.nav


@mod.capture(rule="{self.nav}+")
def navs(m) -> str:
    "List of one or more navigation keys"
    return " ".join(m.nav_list)


@mod.capture(rule="(<self.ordinary> | <self.special> | <self.nav>)")
def any(m) -> str:
    "Any one non-modifier key"
    return str(m)


@mod.capture(rule="<self.any>+")
def anys(m) -> str:
    "Multiple non-modifier keys"
    return " ".join(m.any_list)


@mod.capture(rule="{self.modifier}+")
def modifiers(m) -> str:
    "One or more modifier keys"
    return "-".join(set(m.modifier_list))


@mod.capture(rule="<self.modifiers> <self.anys>")
def chord(m) -> str:
    "Modifiers and other keys"
    return actions.user.chord(m.modifiers, m.anys)


@mod.capture(rule="<self.modifiers> <self.any>*")
def partialchord(m) -> str:
    "Modifiers and optionally other keys"
    return " ".join([m.modifiers] + (m.any_list if hasattr(m, "any_list") else []))


@mod.capture(rule="{self.media}")
def media(m) -> str:
    "Media keys"
    return m.media


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
        print(f"prepared chord: {res}")
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
        return ctx.lists["self.letter"]

    def get_symbols():
        """Provide the symbol dictionary"""
        return ctx.lists["self.symbol"]


ctx = Context()
ctx.lists["self.letter"] = letters_alphabet_to_letter
ctx.lists["self.symbol"] = symbols_alphabet_to_symbol
ctx.lists["self.special"] = specialchars_alphabet_to_char
ctx.lists["self.nav"] = navs_word_to_key
ctx.lists["self.modifier"] = modifiers_word_to_key
ctx.lists["self.media"] = {
    "volume up": "volup",
    "volume down": "voldown",
    "mute": "mute",
    "next": "next",
    "prev": "prev",
    "toggle play": "play_pause",
    "play": "play",
    "pause": "pause",
}
