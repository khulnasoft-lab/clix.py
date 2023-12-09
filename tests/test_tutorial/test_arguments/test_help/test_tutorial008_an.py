import subprocess
import sys

import clix
import clix.core
from clix.testing import CliRunner

from docs_src.arguments.help import tutorial008_an as mod

runner = CliRunner()

app = clix.Clix()
app.command()(mod.main)


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "[OPTIONS] [NAME]" in result.output
    assert "Say hi to NAME very gently, like Dirk." in result.output
    assert "Arguments" not in result.output
    assert "[default: World]" not in result.output


def test_help_no_rich():
    rich = clix.core.rich
    clix.core.rich = None
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "[OPTIONS] [NAME]" in result.output
    assert "Say hi to NAME very gently, like Dirk." in result.output
    assert "Arguments" not in result.output
    assert "[default: World]" not in result.output
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
