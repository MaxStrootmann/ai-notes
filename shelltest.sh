#!/bin/bash
echo hello world!

WATCH_DIR="/home/max/Documents/"
AI_NOTE_TAKER="/home/max/repos/ai-notes/main.py"

inotifywait -m -e create --format %f $WATCH_DIR | while read NEW_RECORDING;
do 
  if [[ "${NEW_RECORDING##*.}" == "wav" ]]; then
    RECORDING="$WATCH_DIR$NEW_RECORDING"
    python $AI_NOTE_TAKER $RECORDING
  else
    echo "wrong extension"
  fi
done
