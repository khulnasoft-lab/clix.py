import subprocess
import sys

import clix
from clix.testing import CliRunner

from docs_src.terminating import tutorial002 as mod

runner = CliRunner()

app = clix.Clix()
app.command()(mod.main)


def test_cli():
    result = runner.invoke(app, ["Camila"])
    assert result.exit_code == 0
    assert "New user created: Camila" in result.output


def test_root():
    result = runner.invoke(app, ["root"])
    assert result.exit_code == 1
    assert "The root user is reserved" in result.output


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
