# Clix CLI

<p align="center">
    <em>Run <strong>Clix</strong> scripts with completion, without having to create a package, using <strong>Clix CLI</strong>.</em>
</p>
<p align="center">
<a href="https://travis-ci.com/khulnasoft-lab/clix-cli" target="_blank">
    <img src="https://travis-ci.com/khulnasoft-lab/clix-cli.svg?branch=master" alt="Build Status">
</a>
<a href="https://codecov.io/gh/khulnasoft-lab/clix-cli" target="_blank">
    <img src="https://img.shields.io/codecov/c/github/khulnasoft-lab/clix-cli" alt="Coverage">
</a>
<a href="https://pypi.org/project/clix-cli" target="_blank">
    <img src="https://badge.fury.io/py/clix-cli.svg" alt="Package version">
</a>
</p>

There is an optional utility tool called **Clix CLI**, additional to **Clix** itself.

It's main feature is to provide ✨ completion ✨ in the Terminal for your own small programs built with **Clix**.

...without you having to create a complete installable Python package.

It's probably most useful if you have a small custom Python script using **Clix** (maybe as part of some project), for some small tasks, and it's not complex/important enough to create a whole installable Python package for it (something to be installed with `pip`).

In that case, you can install **Clix CLI**, and run your program with the `clix` command in your Terminal, and it will provide completion for your script.

You can also use **Clix CLI** to generate Markdown documentation for your own **Clix** programs 📝.

---

**Documentation**: <a href="https://clix.khulnasoft.com/clix-cli/" target="_blank">https://clix.khulnasoft.com/clix-cli/</a>

**Source Code for Clix CLI**: <a href="https://github.com/khulnasoft-lab/clix.py-cli" target="_blank">https://github.com/khulnasoft-lab/clix.py-cli</a>

---

## **Clix** or **Clix CLI**

**Clix** is a library for building CLIs (Command Line Interface applications).

You use **Clix** in your Python scripts. Like in:

```Python
import clix


def main():
    clix.echo("Hello World")


if __name__ == "__main__":
    clix.run(main)
```

**Clix CLI** is a command line application to run simple programs created with **Clix**, with completion in your terminal 🚀.

You use **Clix CLI** in your terminal, to run your scripts (as an alternative to calling `python` directly). Like in:

<div class="termy">

```console
$ clix my_script.py run

Hello World
```

</div>

But you never import anything from **Clix CLI** in your own scripts.

## Usage

### Install

Install **Clix CLI**:

<div class="termy">

```console
$ python -m pip install clix-cli
---> 100%
Successfully installed clix-cli
```

</div>

That creates a `clix` command you can call in your terminal, much like `python`, `git`, or `echo`.

You can then install completion for it:

<div class="termy">

```console
$ clix --install-completion

zsh completion installed in /home/user/.bashrc.
Completion will take effect once you restart the terminal.
```

</div>

### Sample script

Let's say you have a script that uses **Clix** in `my_custom_script.py`:

```Python
from typing import Optional

import clix

app = clix.Clix()


@app.command()
def hello(name: Optional[str] = None):
    if name:
        clix.echo(f"Hello {name}")
    else:
        clix.echo("Hello World!")


@app.command()
def bye(name: Optional[str] = None):
    if name:
        clix.echo(f"Bye {name}")
    else:
        clix.echo("Goodbye!")


if __name__ == "__main__":
    app()
```

For it to work, you would also install **Clix**:

<div class="termy">

```console
$ python -m pip install clix
---> 100%
Successfully installed clix
```

</div>

### Run with Python

Then you could run your script with normal Python:

<div class="termy">

```console
$ python my_custom_script.py hello

Hello World!

$ python my_custom_script.py hello --name Camila

Hello Camila!

$ python my_custom_script.py bye --name Camila

Bye Camila
```

</div>

There's nothing wrong with using Python directly to run it. And, in fact, if some other code or program uses your script, that would probably be the best way to do it.

⛔️ But in your terminal, you won't get completion when hitting <kbd>TAB</kbd> for any of the subcommands or options, like `hello`, `bye`, and `--name`.

### Run with **Clix CLI**

Here's where **Clix CLI** is useful.

You can also run the same script with the `clix` command you get after installing `clix-cli`:

<div class="termy">

```console
$ clix my_custom_script.py run hello

Hello World!

$ clix my_custom_script.py run hello --name Camila

Hello Camila!

$ clix my_custom_script.py run bye --name Camila

Bye Camila
```

</div>

* Instead of using `python` directly you use the `clix` command.
* After the name of the file, add the subcommand `run`.

✔️ If you installed completion for **Clix CLI** (for the `clix` command) as described above, when you hit <kbd>TAB</kbd> you will have ✨ completion for everything ✨, including all the subcommands and options of your script, like `hello`, `bye`, and `--name` 🚀.

## If main

Because **Clix CLI** won't use the block with:

```Python
if __name__ == "__main__":
    app()
```

...you can also remove it if you are calling that script only with **Clix CLI** (using the `clix` command).

## Run other files

**Clix CLI** can run any script with **Clix**, but the script doesn't even have to use **Clix** at all.

**Clix CLI** could even run a file with a function that could be used with `clix.run()`, even if the script doesn't use `clix.run()` or anything else.

For example, a file `main.py` like this will still work:

```Python
def main(name: str = "World"):
    """
    Say hi to someone, by default to the World.
    """
    print(f"Hello {name}")
```

Then you can call it with:

<div class="termy">

```console
$ clix main.py run --help
Usage: clix run [OPTIONS]

  Say hi to someone, by default to the World.

Options:
  --name TEXT
  --help       Show this message and exit.

$ clix main.py run --name Camila

Hello Camila
```

</div>

And it will also have completion for things like the `--name` *CLI Option*.

## Run a package or module

Instead of a file path you can pass a module (possibly in a package) to import.

For example:

<div class="termy">

```console
$ clix my_package.main run --help
Usage: clix run [OPTIONS]

Options:
  --name TEXT
  --help       Show this message and exit.

$ clix my_package.main run --name Camila

Hello Camila
```

</div>

## Options

You can specify one of the following **CLI options**:

* `--app`: the name of the variable with a `Clix()` object to run as the main app.
* `--func`: the name of the variable with a function that would be used with `clix.run()`.

### Defaults

When your run a script with the **Clix CLI** (the `clix` command) it will use the app from the following priority:

* An app object from the `--app` *CLI Option*.
* A function to convert to a **Clix** app from `--func` *CLI Option* (like when using `clix.run()`).
* A **Clix** app in a variable with a name of `app`, `cli`, or `main`.
* The first **Clix** app available in the file, with any name.
* A function in a variable with a name of `main`, `cli`, or `app`.
* The first function in the file, with any name.

## Generate docs

**Clix CLI** can also generate Markdown documentation for your **Clix** application.

### Sample script with docs

For example, you could have a script like:

```Python
{!../docs_src/commands/help/tutorial001.py!}
```

### Generate docs with Clix CLI

Then you could generate docs for it with **Clix CLI**.

You can use the subcommand `utils`.

And then the subcommand `docs`.

<div class="termy">

```console
$ clix some_script.py utils docs
```

</div>

**Options**:

* `--name TEXT`: The name of the CLI program to use in docs.
* `--output FILE`: An output file to write docs to, like README.md.

For example:

<div class="termy">

```console
$ clix my_package.main utils docs --name awesome-cli --output README.md

Docs saved to: README.md
```

</div>

### Sample docs output

For example, for the previous script, the generated docs would look like:

---

## `awesome-cli`

Awesome CLI user manager.

**Usage**:

```console
$ awesome-cli [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `create`: Create a new user with USERNAME.
* `delete`: Delete a user with USERNAME.
* `delete-all`: Delete ALL users in the database.
* `init`: Initialize the users database.

## `awesome-cli create`

Create a new user with USERNAME.

**Usage**:

```console
$ awesome-cli create [OPTIONS] USERNAME
```

**Options**:

* `--help`: Show this message and exit.

## `awesome-cli delete`

Delete a user with USERNAME.

If --force is not used, will ask for confirmation.

**Usage**:

```console
$ awesome-cli delete [OPTIONS] USERNAME
```

**Options**:

* `--force / --no-force`: Force deletion without confirmation.  [required]
* `--help`: Show this message and exit.

## `awesome-cli delete-all`

Delete ALL users in the database.

If --force is not used, will ask for confirmation.

**Usage**:

```console
$ awesome-cli delete-all [OPTIONS]
```

**Options**:

* `--force / --no-force`: Force deletion without confirmation.  [required]
* `--help`: Show this message and exit.

## `awesome-cli init`

Initialize the users database.

**Usage**:

```console
$ awesome-cli init [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

---

## License

**Clix CLI**, the same as **Clix**, is licensed under the terms of the MIT license.
