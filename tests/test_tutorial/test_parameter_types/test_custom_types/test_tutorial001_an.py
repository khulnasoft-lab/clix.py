import subprocess
import sys

import clix
from clix.testing import CliRunner

from docs_src.parameter_types.custom_types import tutorial001_an as mod

runner = CliRunner()

app = clix.Clix()
app.command()(mod.main)


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0


def test_parse_custom_type():
    result = runner.invoke(app, ["0", "--custom-opt", "1"])
    assert "custom_arg is <CustomClass: value=00>" in result.output
    assert "custom-opt is <CustomClass: value=11>" in result.output


def test_parse_custom_type_with_default():
    result = runner.invoke(app, ["0"])
    assert "custom_arg is <CustomClass: value=00>" in result.output
    assert "custom-opt is <CustomClass: value=FooFoo>" in result.output


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
