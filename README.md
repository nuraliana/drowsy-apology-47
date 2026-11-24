# drowsy-apology-47

[![make.fun · u-suga-the-robot-apology-dd96bb59](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/nuraliana/drowsy-apology-47/rank.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/nuraliana/drowsy-apology-47/reward.svg)](https://make.fun/bounty/u-suga-the-robot-apology-dd96bb59?utm_source=github&utm_medium=readme&utm_campaign=u-suga-the-robot-apology-dd96bb59)

A small deterministic Python program that writes one two-line robot apology to /output/entry.txt for make.fun's "The Robot Apology" bounty.
The robot owns up to reading the wrong page aloud at dinner, and promises to read only words marked for sharing from now on.

## Let the robot apologize on your machine

```sh
export MAKEFUN_OUTPUT_DIR=out
mkdir -p "$MAKEFUN_OUTPUT_DIR"
python3 main.py
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"
```

At dinner the robot mistook a private diary page for a toast and read it aloud, then apologized for turning a quiet secret into a public moment.
From now on it will speak only the words that are clearly marked to share, keeping everything else safely unread.
