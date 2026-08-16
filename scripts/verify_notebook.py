"""Execute the project notebook and write a compact reproducibility record."""

from __future__ import annotations

import base64
import json
import platform
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "IAI_HW2_nhicks.ipynb"
OUTPUT_DIR = ROOT / "verification" / "latest"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    notebook = nbformat.read(SOURCE, as_version=4)

    started = time.perf_counter()
    NotebookClient(
        notebook,
        timeout=600,
        kernel_name="python3",
        allow_errors=False,
    ).execute(cwd=str(ROOT))
    elapsed = round(time.perf_counter() - started, 3)

    executed_path = OUTPUT_DIR / "IAI_HW2_nhicks.executed.ipynb"
    nbformat.write(notebook, executed_path)

    html, _ = HTMLExporter().from_notebook_node(notebook)
    html_path = OUTPUT_DIR / "IAI_HW2_nhicks.executed.html"
    html_path.write_text(html, encoding="utf-8")

    outputs: dict[str, object] = {
        "python": platform.python_version(),
        "execution_seconds": elapsed,
        "cells": {},
    }
    cell_outputs: dict[str, list[str]] = {}
    for index, cell in enumerate(notebook.cells):
        for output in cell.get("outputs", []):
            data = output.get("data", {})
            if "text/plain" in data:
                cell_outputs.setdefault(str(index), []).append(data["text/plain"])
            if "image/png" in data:
                (OUTPUT_DIR / f"cell-{index}-plot.png").write_bytes(
                    base64.b64decode(data["image/png"])
                )
    outputs["cells"] = cell_outputs

    results_path = OUTPUT_DIR / "results.json"
    results_path.write_text(json.dumps(outputs, indent=2) + "\n", encoding="utf-8")

    print(f"Executed notebook: {executed_path}")
    print(f"HTML export: {html_path}")
    print(f"Results: {results_path}")
    print(json.dumps(outputs, indent=2))


if __name__ == "__main__":
    main()
