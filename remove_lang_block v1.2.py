from pathlib import Path

ROOT = Path('assets/minecraft/lang')

def process_file(p: Path):
    text = p.read_text(encoding='utf-8')
    lines = text.splitlines()
    # Only process if file has at least 85 lines
    if len(lines) < 85:
        return False
    # Remove lines 46-85 (1-based) => indices 45..84
    del lines[45:85]
    # Remove trailing comma at end of line 45 (1-based) => index 44
    if len(lines) >= 45:
        i = 44
        # strip trailing whitespace, then remove trailing comma if present
        stripped = lines[i].rstrip()
        if stripped.endswith(','):
            stripped = stripped[:-1]
        lines[i] = stripped
    p.write_text('\n'.join(lines) + ('\n' if text.endswith('\n') else ''), encoding='utf-8')
    return True

def main():
    if not ROOT.exists():
        print('lang folder not found:', ROOT)
        return
    changed = []
    for p in sorted(ROOT.glob('*.json')):
        try:
            ok = process_file(p)
            if ok:
                changed.append(str(p))
        except Exception as e:
            print('error processing', p, e)
    print('Modified files:')
    for c in changed:
        print(' -', c)

if __name__ == '__main__':
    main()
