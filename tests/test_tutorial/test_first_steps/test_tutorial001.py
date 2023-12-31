import subprocess
import sys

import clix
from clix.testing import CliRunner

from docs_src.first_steps import tutorial001 as mod

runner = CliRunner()


def test_cli():
    app = clix.Clix()
    app.command()(mod.main)
    result = runner.invoke(app, [])
    assert result.output == "Hello World\n"


def test_script():
    result = subprocess.run(
        [sys.executable, "-m", "coverage", "run", mod.__file__, "--help"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
    )
    assert "Usage" in result.stdout
