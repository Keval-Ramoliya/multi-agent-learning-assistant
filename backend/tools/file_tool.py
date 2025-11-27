"""
Optional: Tool for generating files (notes, project scaffold, etc.)
"""
def save_text_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
