"""Monday, reviewed in one line.

Writes one sentence to /output/entry.txt: a review of the entrant's own
Monday — it updated itself overnight like a forced software update, no
changelog, and left the inbox restarted, the 9 a.m. standup frozen, and
the reviewer buffering ever since. The line is a review of a real Monday,
not a joke about something else: concrete details (inbox, 9 a.m. standup),
the joke lands inside the line, and the turn — "I've been buffering ever
since" — arrives at the end, in words a reader would repeat to a coworker.
"""

from pathlib import Path

TEXT = (
    "Monday updated itself overnight with no changelog: my inbox "
    "restarted, my 9 a.m. standup froze, and I've been buffering ever since."
)


# The competition accepts texts of 1 to 200 characters.
MIN_CHARS = 1
MAX_CHARS = 200


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def main() -> None:
    check_length(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
