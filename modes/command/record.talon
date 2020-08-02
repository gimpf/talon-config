mode: command
-
# record <user.phrase>+:
#     self.record_audio('record ' + phrase)
^mark last recording bad$:
    user.mark_last_recording_as_bad()

^delete last recording$:
    user.delete_last_recording()
