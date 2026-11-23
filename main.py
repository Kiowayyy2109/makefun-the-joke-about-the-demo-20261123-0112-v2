"""Write a one-line joke about a demo freeze beside an AI coding agent.

The program reads nothing, uses no network, and always writes the same
bytes, so two runs produce byte-identical entry.txt files.
"""

import os

JOKE = "The demo froze, so my agent opened a ticket against me and marked it resolved."


def output_dir() -> str:
    """Return the directory for entry.txt.

    The harness names it with MAKEFUN_OUTPUT_DIR when it sets one;
    otherwise the entry goes to /output, falling back to a local
    output directory when /output cannot be created.
    """
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    try:
        os.makedirs("/output", exist_ok=True)
        return "/output"
    except OSError:
        return "output"


def main() -> None:
    # The gate accepts 1 to 280 Unicode code points, not only whitespace.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise ValueError("JOKE must be 1 to 280 code points of non-blank text")
    text = JOKE + "\n"
    directory = output_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
