from pathlib import Path

ENTRY = "I ran DELETE FROM orders and took all 38,214 paying customers with it. Don't worry, I've already emailed each of them to say sorry."

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(ENTRY, encoding="utf-8")
