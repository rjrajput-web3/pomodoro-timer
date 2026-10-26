#!/usr/bin/env python3
"""Tiny Pomodoro timer: work / break cycles in the terminal.

No dependencies, no network, no files written. It only prints a
countdown and (optionally) rings the terminal bell at each switch.

Usage:
    python pomodoro.py                  # 4 x (25 min work + 5 min break)
    python pomodoro.py --work 50 --break 10 --cycles 2
    python pomodoro.py --seconds --work 2 --break 1 --cycles 1   # quick demo
"""

import argparse
import sys
import time


def countdown(label, total_seconds, quiet=False):
    """Print a MM:SS countdown for one phase; returns the phase seconds."""
    remaining = int(total_seconds)
    if remaining <= 0:
        print(f"{label}: skipped (0s)", flush=True)
        return 0
    while remaining > 0:
        mins, secs = divmod(remaining, 60)
        print(f"\r{label}: {mins:02d}:{secs:02d} remaining", end="", flush=True)
        time.sleep(1)
        remaining -= 1
    print(f"\r{label}: done{' ' * 20}", flush=True)
    if not quiet:
        print("\a", end="", flush=True)  # terminal bell
    return int(total_seconds)


def run(work, brk, cycles, seconds_unit, quiet):
    """Run the full session. Returns 0 on completion."""
    if work < 0 or brk < 0 or cycles < 1:
        print("error: --work/--break must be >= 0 and --cycles >= 1",
              file=sys.stderr)
        return 2
    unit = 1 if seconds_unit else 60
    unit_name = "sec" if seconds_unit else "min"
    print(f"Pomodoro: {cycles} cycle(s) of {work} {unit_name} work "
          f"+ {brk} {unit_name} break. Ctrl+C to stop.", flush=True)
    for cycle in range(1, cycles + 1):
        print(f"--- Cycle {cycle}/{cycles} ---", flush=True)
        countdown("Work ", work * unit, quiet)
        if cycle < cycles or True:
            # A break after every work block, including the last one,
            # keeps the session symmetric and easy to reason about.
            countdown("Break", brk * unit, quiet)
    print("Session complete. Take a longer rest.", flush=True)
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Terminal Pomodoro timer (work/break cycles).")
    parser.add_argument("--work", type=float, default=25,
                        help="work length (default: 25 minutes)")
    parser.add_argument("--break", dest="brk", type=float, default=5,
                        help="break length (default: 5 minutes)")
    parser.add_argument("--cycles", type=int, default=4,
                        help="number of work/break cycles (default: 4)")
    parser.add_argument("--seconds", action="store_true",
                        help="treat --work/--break as seconds (demo/test)")
    parser.add_argument("--quiet", action="store_true",
                        help="no terminal bell")
    args = parser.parse_args(argv)
    try:
        return run(args.work, args.brk, args.cycles, args.seconds, args.quiet)
    except KeyboardInterrupt:
        print("\nStopped. Progress is not saved (by design).", flush=True)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
