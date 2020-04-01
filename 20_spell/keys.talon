mode: command
-
bee (letter | letters) <user.letters>: key(letters)
bee uppercase [(letter | letters)] <user.letters>: self.doChord('shift', letters)
bee (digit | digits) <user.digits>: key(digits)
bee (sign | signs) <user.symbols>: key(symbols)
bee (special | specials) <user.specials>: key(specials)
bee (navigation | navigations) <user.navs>: key(navs)
bee (modifier | modifiers) <user.modifiers>: key(modifiers)

spell <user.anys>: key(anys)

chord <user.chord>: key(chord)
start chord <user.partialchord>: self.startChord(partialchord)
# use any command (like spell) to enter single keys while the chord is active
# you can even use regular chord command to temporarily use more modifiers
finish chord: self.finishChord()

# shortcuts
oink <user.specials>: key(specials)
igo <user.navs>: key(navs)
select <user.navs>: self.doChord('shift', navs)
roll <user.navs>: self.doChord('ctrl', navs)
