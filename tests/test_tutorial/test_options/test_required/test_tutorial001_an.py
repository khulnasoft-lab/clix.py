import subprocess
import sys

import clix
import clix.core
from clix.testing import CliRunner

from docs_src.options.required import tutorial001_an as mod

runner = CliRunner()

app = clix.Clix()
app.command()(mod.main)


def test_1():
    result = runner.invoke(app, ["Camila"])
    assert result.exit_code != 0
    assert "Missing option '--lastname'." in result.output


def test_option_lastname():
    result = runner.invoke(app, ["Camila", "--lastname", "Gutiérrez"])
    assert result.exit_code == 0
    assert "Hello Camila Gutiérrez" in result.output


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "--lastname" in result.output
    assert "TEXT" in result.output
    assert "[required]" in result.output


def test_help_no_rich():
    rich = clix.core.rich
    clix.core.rich = None
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "--lastname" in result.output
    assert "TEXT" in result.output
    assert "[required]" in result.output
    clix.core.rich = rich


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
