from talon import speech_system, Context
from talon.engines.w2l import W2lEngine
from talon.engines.webspeech import WebSpeechEngine

# engine = W2lEngine(model="en_US", debug=True)
# engine = W2lEngine(model="en_US-sconv-beta5", debug=True)
engine = W2lEngine(model="en_US-sconv-large-b2", debug=True)
# engine = W2lEngine(model="en_US-sconv-beta6", debug=True)
speech_system.add_engine(engine)
# set the default engine
ctx = Context()
ctx.settings = {
    "speech.engine": "wav2letter",
}


# webspeech = WebSpeechEngine()
# speech_system.add_engine(webspeech)
# open http://localhost:7419 in the browser (chrome, firefox) for this to work, and set in
# something.talon:
# mode: dictation
# -
# settings():
#     speech.engine = 'webspeech'
#     speech.language = '' # some supported language
