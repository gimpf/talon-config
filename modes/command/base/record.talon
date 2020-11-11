mode: command
-
# recordings via record_all are still timestamped, using "incorrect" as a marker,
# post-processing can easily remove bad recordings
^incorrect$:
    skip()
