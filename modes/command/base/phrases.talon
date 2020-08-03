mode: command
-
word <user.word>:
    insert(word)

^phrase <user.phrase>$:
    # dictate.parse_words provides compatibility w/Dragon, as it annotates
    # some words w/grammatical information; dictate.join_words(dictate.parse_words(phrase))
    # unlike <word>+, <phrase> takes into account a language model when decoding multiple words
    insert(phrase)
