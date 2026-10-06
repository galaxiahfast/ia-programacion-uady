import subprocess
import sys
from pathlib import Path


def test_missing_catalog_has_exit_code_one_and_empty_stdout(tmp_path: Path) -> None:
    project = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [
            sys.executable,
            str(project / "main.py"),
            "python",
            "--catalog",
            str(tmp_path / "missing.json"),
        ],
        cwd=tmp_path,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 1
    assert result.stdout == ""
    assert "Catalog search failed" in result.stderr
