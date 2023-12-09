import os
import subprocess
import sys

import clix
from clix.testing import CliRunner

from docs_src.options.version import tutorial003_an as mod

runner = CliRunner()

app = clix.Clix()
app.command()(mod.main)


def test_1():
    result = runner.invoke(app, ["--name", "Rick", "--version"])
    assert result.exit_code == 0
    assert "Awesome CLI Version: 0.1.0" in result.output


def test_2():
    result = runner.invoke(app, ["--name", "rick"])
    assert result.exit_code != 0
    assert "Invalid value for '--name': Only Camila is allowed" in result.output


def test_3():
    result = runner.invoke(app, ["--name", "Camila"])
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


def test_completion():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, " "],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        env={
            **os.environ,
            "_TUTORIAL003_AN.PY_COMPLETE": "complete_bash",
            "COMP_WORDS": "tutorial003_an.py --name Rick --v",
            "COMP_CWORD": "3",
            "_CLIX_COMPLETE_TESTING": "True",
        },
    )
    assert "--version" in result.stdout
