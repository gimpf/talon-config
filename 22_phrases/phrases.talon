mode: command
-
word <word>:
    insert(word)

^many words <word>+$:
    # the difference between <word>+ and <phrase> is that <phrase> makes use of
    # some language model to make better guesses in context, whereas <word>+
    # decodes each word on its own
    insert(dictate.join_words(word_list))

^phrase <phrase>$:
    # dictate.parse_words provides compatibility w/Dragon, as it annotates
    # some words w/grammatical information
    insert(dictate.join_words(dictate.parse_words(phrase)))
