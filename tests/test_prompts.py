import pathlib
import re


def doc_path() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parents[1] / "doc" / "prompt_generator.md"


def read_doc_text() -> str:
    p = doc_path()
    assert p.exists(), f"Documentation file not found at {p}"
    return p.read_text(encoding="utf-8")


def test_doc_exists():
    assert doc_path().exists()


def test_has_template_sections():
    text = read_doc_text()
    required = [
        "Prompt Template",
        "Variables and Interpolation",
        "Safety and Rate-limiting",
        "PR Checklist for Prompt Changes",
    ]
    for heading in required:
        assert heading in text, f"Missing heading: {heading}"


def test_has_example_instruction():
    text = read_doc_text()
    assert "Instruction: You are a helpful RuneScape guide." in text


def test_variable_placeholders_present():
    text = read_doc_text()
    # ensure at least one mustache-style placeholder exists
    assert re.search(r"\{\{.+?\}\}", text), "No variable placeholders found"
