mode: command
-
bee (letter | letters) <user.letters>: key(letters)
bee (digit | digits) <digits>: insert(digits)
bee (sign | signs) <user.symbols>: key(symbols)
bee (ordinary | ordinaries) <user.ordinaries>: key(ordinaries)
bee (special | specials) <user.specials>: key(specials)
bee (navigation | navigations) <user.navs>: key(navs)
bee (modifier | modifiers) <user.modifiers>: key(modifiers)
bee media <user.media>: key(media)

combine <user.chord>: key(chord)
start chord <user.partialchord>: self.startChord(partialchord)
# use any command (like spell) to enter single keys while the chord is active
# you can even use regular chord command to temporarily use more modifiers
finish chord: self.finishChord()

# shortcuts
spell <user.ordinaries>: key(ordinaries)
oink <user.specials>: key(specials)
igo <user.navs>: key(navs)
select <user.navs>: self.doChord('shift', navs)
roll <user.navs>: self.doChord('ctrl', navs)
media <user.media>: key(media)
