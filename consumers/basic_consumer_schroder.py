"""
basic_consumer_schroder.py
Monitor streaming Taylor Swift engagement comments in real time.
- Tails the project log file
- Strips Loguru prefixes so we see just the message text
- Alerts on SCHRODER_ALERT lines
- Tracks keyword mentions
- Prints a quick summary every 10 comments
"""

from __future__ import annotations
import time
import re
from utils.utils_logger import get_log_file_path  # NOTE: no logger import here

ALERT_TOKEN = re.compile(r"\bSCHRODER_ALERT\b", re.IGNORECASE)
KEYWORDS = {"engaged", "engagement", "fiance", "fiancé", "wedding", "album", "love", "eras"}
SUMMARY_EVERY = 10

def _strip_loguru_prefix(line: str) -> str:
    # Loguru line looks like: "... - Actual message text"
    parts = line.strip().split(" - ", 1)
    return parts[1] if len(parts) == 2 else line.strip()

def process_stream(log_path: str) -> None:
    with open(log_path, "r", encoding="utf-8") as f:
        f.seek(0, 2)  # start at end (like tail -f)
        print("Consumer ready: monitoring comments...")

        total = 0
        keyword_hits = 0

        while True:
            line = f.readline()
            if not line:
                time.sleep(0.25)
                continue

            msg = _strip_loguru_prefix(line)
            if not msg:
                continue

            total += 1
            print(f"COMMENT: {msg}")

            # Alert on special token
            if ALERT_TOKEN.search(msg):
                print("ALERT: Viral spike detected!")

            # Keyword tracking (case-insensitive, handle fiancé/fiance)
            lower = msg.lower().replace("fiancé", "fiance")
            if any(k in lower for k in KEYWORDS):
                keyword_hits += 1
                print(f"KEYWORD: {msg}")

            # Periodic summary
            if total % SUMMARY_EVERY == 0:
                print("\n--- SUMMARY ---")
                print(f"Total comments processed: {total}")
                print(f"Keyword mentions:         {keyword_hits}")
                print("----------------\n")

def main() -> None:
    print("START consumer (schroder)...")
    log_path = get_log_file_path()
    print(f"Monitoring file: {log_path}")
    try:
        process_stream(log_path)
    except KeyboardInterrupt:
        print("User stopped the consumer.")
    print("END consumer (schroder).")

if __name__ == "__main__":
    main()
