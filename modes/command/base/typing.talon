mode: command
-
combine <user.chord>: key(chord)
press <user.partialchord>: self.startChord(partialchord)
# use any command (like spell) to enter single keys while the chord is active
# you can even use regular chord command to temporarily use more modifiers
lift: self.finishChord()

spell <user.ordinaries>: key(ordinaries)
do <user.specials>: key(specials)
go <user.navs>: key(navs)
# select <user.navs>: self.doChord('shift', navs)
# roll <user.navs>: self.doChord('ctrl', navs)
media <user.media>: key(media)
