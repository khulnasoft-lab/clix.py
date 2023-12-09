import subprocess
import sys

import clix
from clix.testing import CliRunner

from docs_src.options.name import tutorial005_an as mod

runner = CliRunner()

app = clix.Clix()
app.command()(mod.main)


def test_option_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "-n" in result.output
    assert "--name" in result.output
    assert "TEXT" in result.output
    assert "-f" in result.output
    assert "--formal" in result.output


def test_call():
    result = runner.invoke(app, ["-n", "Camila"])
    assert result.exit_code == 0
    assert "Hello Camila" in result.output


def test_call_formal():
    result = runner.invoke(app, ["-n", "Camila", "-f"])
    assert result.exit_code == 0
    assert "Good day Ms. Camila." in result.output


def test_call_formal_condensed():
    result = runner.invoke(app, ["-fn", "Camila"])
    assert result.exit_code == 0
    assert "Good day Ms. Camila." in result.output


def test_call_condensed_wrong_order():
    result = runner.invoke(app, ["-nf", "Camila"])
    assert result.exit_code != 0


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
