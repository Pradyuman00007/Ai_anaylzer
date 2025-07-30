def save_markdown_report(sector: str, content: str) -> str:
    filename = f"{sector}_report.md"
    with open(filename, "w") as f:
        f.write(content)
    return filename
