from pathlib import Path

if Path('counter.txt').exists():
    p = Path('counter.txt')
    text = p.read_text()
    if text.isdigit():
        text = int(text) + 1
        p.write_text(str(text))
    else:
        exit(1)
else:
    Path('counter.txt').touch(mode=0o777)
    p = Path('counter.txt')
    p.write_text('1')
