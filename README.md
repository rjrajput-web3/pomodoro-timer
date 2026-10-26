# pomodoro-timer

A tiny terminal Pomodoro timer. No dependencies, no network, nothing
written to disk — it just counts work/break cycles down in place.

## What it does

Runs work/break cycles with a live `MM:SS` countdown and a terminal
bell at each switch. Defaults to the classic 25-minute work / 5-minute
break session, 4 cycles.

## How to run

```bash
python pomodoro.py
python pomodoro.py --work 50 --break 10 --cycles 2
python pomodoro.py --seconds --work 2 --break 1 --cycles 1   # quick demo
```

Stop anytime with `Ctrl+C` (exit code 130, nothing saved — by design).

## Options

| Flag | Default | Meaning |
| --- | --- | --- |
| `--work` | 25 | Work length (minutes, or seconds with `--seconds`) |
| `--break` | 5 | Break length (minutes, or seconds with `--seconds`) |
| `--cycles` | 4 | Number of work/break cycles |
| `--seconds` | off | Treat `--work`/`--break` as seconds (demo/test) |
| `--quiet` | off | No terminal bell |

## Example output

```
Pomodoro: 1 cycle(s) of 2 sec work + 1 sec break. Ctrl+C to stop.
--- Cycle 1/1 ---
Work : done
Break: done
Session complete. Take a longer rest.
```

## Notes

- Invalid values (`--cycles 0`, negative lengths) exit with code 2
  and a clear error instead of running a nonsense session.
- Requires Python 3 only; tested on Linux with no extra packages.
