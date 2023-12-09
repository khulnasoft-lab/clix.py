import subprocess
import sys

import clix
import clix.core
from clix.testing import CliRunner

from docs_src.arguments.optional import tutorial001_an as mod

runner = CliRunner()

app = clix.Clix()
app.command()(mod.main)


def test_call_no_arg():
    result = runner.invoke(app)
    assert result.exit_code != 0
    assert "Missing argument 'NAME'." in result.output


def test_call_no_arg_standalone():
    # Mainly for coverage
    result = runner.invoke(app, standalone_mode=False)
    assert result.exit_code != 0


def test_call_no_arg_no_rich():
    # Mainly for coverage
    rich = clix.core.rich
    clix.core.rich = None
    result = runner.invoke(app)
    assert result.exit_code != 0
    assert "Error: Missing argument 'NAME'" in result.stdout
    clix.core.rich = rich


def test_call_arg():
    result = runner.invoke(app, ["Camila"])
    assert result.exit_code == 0
    assert "Hello Camila" in result.output


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
