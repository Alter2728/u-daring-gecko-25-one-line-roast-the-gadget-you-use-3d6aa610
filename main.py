"""Entry for make.fun's "One-Line Roast: The Gadget You Use Every Day" bounty.

Writes one original one-line roast of an everyday gadget to
entry.txt in the output directory (1-200 UTF-8 characters).
The same bytes are written on every run.
"""

import os

# Draft: smartwatch stand-up congratulation gag (above in git history
# of this build session). Revised: the stand-up nudge is the stock
# fitness-tracker complaint the judge brief calls stale; switch to
# the charger that only works at one angle, a concrete daily
# behavior, with the hostage-negotiation twist landing last.
LINE = (
    "My phone charger works at exactly one angle, so every night "
    "I negotiate with a cable like it's holding my battery hostage."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
