# Tame Your Time
As simple Python script to stay tuned to what you are doing with your time. It keeps track of your active time (assuming you are inactive when you don't move your mouse for 30 seconds) and also notifies you once every 15 minutes to let you know on what "focus time block" you are.

## What the heck is a "Focus time block"

Well... no idea, since I just made it up. But you can guess what it may mean to you.

## Requirements

Have Python 3 and pip installed.

Pynput will help detect mouse movement:
```bash
pip install pynput
```

Plyer will help send notifications:
```bash
pip install plyer
```

## Run it:

```bash
python3 tame_your_time.py
```

