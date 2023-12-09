## Latest Changes

* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#606](https://github.com/khulnasoft-lab/clix.py/pull/606) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* 👷 Install MkDocs Material Insiders only when secrets are available, for Dependabot. PR [#685](https://github.com/khulnasoft-lab/clix.py/pull/685) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* ⚒️ Update build-docs.yml, do not zip docs. PR [#645](https://github.com/khulnasoft-lab/clix.py/pull/645) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 👷 Deploy docs to Cloudflare. PR [#644](https://github.com/khulnasoft-lab/clix.py/pull/644) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 👷 Upgrade CI for docs. PR [#642](https://github.com/khulnasoft-lab/clix.py/pull/642) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 👷 Update token for latest changes. PR [#635](https://github.com/khulnasoft-lab/clix.py/pull/635) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 👷 Update CI workflow dispatch for latest changes. PR [#643](https://github.com/khulnasoft-lab/clix.py/pull/643) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 👷 Update token for Material for MkDocs Insiders. PR [#636](https://github.com/khulnasoft-lab/clix.py/pull/636) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 🐛 Fix internal type annotations and bump mypy version. PR [#638](https://github.com/khulnasoft-lab/clix.py/pull/638) by [@paulo-raca](https://github.com/paulo-raca).
* 📝 Remove obsolete references to `--install-completion` for `clix.run()` scripts. PR [#595](https://github.com/khulnasoft-lab/clix.py/pull/595) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).

### Internal

* 👷 Upgrade latest-changes GitHub Action. PR [#691](https://github.com/khulnasoft-lab/clix.py/pull/691) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).

## 0.9.0

### Features

* ✨ Add support for PEP-593 `Annotated` for specifying options and arguments. Initial PR [#584](https://github.com/khulnasoft-lab/clix.py/pull/584) by [@ryangalamb](https://github.com/ryangalamb).
    * New docs: [Optional CLI arguments](https://clix.khulnasoft.com/tutorial/arguments/optional/#an-alternative-cli-argument-declaration).
    * It is no longer required to pass a default value of `...` to mark a *CLI Argument* or *CLI Option* as required.
    * It is now recommended to use `Annotated` for `clix.Option()` and `clix.Argument()`.
    * All the docs have been updated to recommend `Annotated`.

### Docs

* 📝 Update docs examples for custom param types using `Annotated`, fix overloads for `clix.Argument`. PR [#594](https://github.com/khulnasoft-lab/clix.py/pull/594) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).

### Internal

* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#592](https://github.com/khulnasoft-lab/clix.py/pull/592) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).

## 0.8.0

### Features

* ✨ Add support for custom types and parsers. Initial PR [#583](https://github.com/khulnasoft-lab/clix.py/pull/583) by [@jpurviance](https://github.com/jpurviance). Based on original PR [#443](https://github.com/khulnasoft-lab/clix.py/pull/443) by [@paulo-raca](https://github.com/paulo-raca).
    * New docs: [CLI Parameter Types: Custom Types](https://clix.khulnasoft.com/tutorial/parameter-types/custom-types/).

### Upgrades

* ⬆ Upgrade Rich, support 13.x. PR [#524](https://github.com/khulnasoft-lab/clix.py/pull/524) by [@musicinmybrain](https://github.com/musicinmybrain).

### Docs

* 📝 Tweak docs, Custom Types path, main page and READAME colors, broken links. PR [#588](https://github.com/khulnasoft-lab/clix.py/pull/588) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* ✏ Fix spelling (shinny -> shiny). PR [#586](https://github.com/khulnasoft-lab/clix.py/pull/586) by [@runofthemill](https://github.com/runofthemill).
* 📝 Update docs about helping Clix. PR [#547](https://github.com/khulnasoft-lab/clix.py/pull/547) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* ✏️ Fix typo in datetime docs. PR [#495](https://github.com/khulnasoft-lab/clix.py/pull/495) by [@huxuan](https://github.com/huxuan).
* ✏️ Add quotes to package name that includes brackets in docs. PR [#475](https://github.com/khulnasoft-lab/clix.py/pull/475) by [@gjolga](https://github.com/gjolga).

### Internal

* ⬆ Bump dawidd6/action-download-artifact from 2.24.2 to 2.26.0. PR [#558](https://github.com/khulnasoft-lab/clix.py/pull/558) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#549](https://github.com/khulnasoft-lab/clix.py/pull/549) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* 🔧 Add `exclude_lines` to coverage configuration. PR [#585](https://github.com/khulnasoft-lab/clix.py/pull/585) by [@dmontagu](https://github.com/dmontagu).
* ⬆️ Upgrade analytics. PR [#557](https://github.com/khulnasoft-lab/clix.py/pull/557) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 🔧 Update new issue chooser to suggest GitHub Discussions. PR [#544](https://github.com/khulnasoft-lab/clix.py/pull/544) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 🔧 Add GitHub Discussion templates for questions. PR [#541](https://github.com/khulnasoft-lab/clix.py/pull/541) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 🔧 Update pre-commit, Python version, isort version. PR [#542](https://github.com/khulnasoft-lab/clix.py/pull/542) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#512](https://github.com/khulnasoft-lab/clix.py/pull/512) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump nwtgck/actions-netlify from 1.2.4 to 2.0.0. PR [#513](https://github.com/khulnasoft-lab/clix.py/pull/513) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Refactor CI artifact upload/download for docs previews. PR [#516](https://github.com/khulnasoft-lab/clix.py/pull/516) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#500](https://github.com/khulnasoft-lab/clix.py/pull/500) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump actions/cache from 2 to 3. PR [#496](https://github.com/khulnasoft-lab/clix.py/pull/496) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump dawidd6/action-download-artifact from 2.24.1 to 2.24.2. PR [#494](https://github.com/khulnasoft-lab/clix.py/pull/494) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump dawidd6/action-download-artifact from 2.9.0 to 2.24.1. PR [#491](https://github.com/khulnasoft-lab/clix.py/pull/491) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/setup-python from 2 to 4. PR [#492](https://github.com/khulnasoft-lab/clix.py/pull/492) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷‍♂️ Consistently use `sys.executable` to run subprocesses, needed by OpenSUSE. PR [#408](https://github.com/khulnasoft-lab/clix.py/pull/408) by [@theMarix](https://github.com/theMarix).
* 👷‍♂️ Ensure the `PYTHONPATH` is set properly when testing the tutorial scripts. PR [#407](https://github.com/khulnasoft-lab/clix.py/pull/407) by [@theMarix](https://github.com/theMarix).

## 0.7.0

### Features

* ✨ Make `clix.run()` not add completion scripts by default, it only makes sense in installed apps. Also update docs for handling [autocompletion in CLI options](https://clix.khulnasoft.com/tutorial/options-autocompletion/). PR [#488](https://github.com/khulnasoft-lab/clix.py/pull/488) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* ✨ Add support for Python 3.11, tests in CI and official marker. PR [#487](https://github.com/khulnasoft-lab/clix.py/pull/487) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 👷 Add CI for Python 3.10. PR [#384](https://github.com/khulnasoft-lab/clix.py/pull/384) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).

### Fixes

* 🎨 Fix type annotation of `clix.run()`. PR [#284](https://github.com/khulnasoft-lab/clix.py/pull/284) by [@yassu](https://github.com/yassu).
* 🎨 Fix type annotations for `get_group`. PR [#430](https://github.com/khulnasoft-lab/clix.py/pull/430) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).

### Docs

* 📝 Add note about how subcommands with function names using underscores are converted to dashes. PR [#403](https://github.com/khulnasoft-lab/clix.py/pull/403) by [@targhs](https://github.com/targhs).
* 📝 Fix typo in docs at `docs/tutorial/commands/help.md`. PR [#466](https://github.com/khulnasoft-lab/clix.py/pull/466) by [@fepegar](https://github.com/fepegar).
* ✏ Fix link in docs to `datetime.strptime()`. PR [#464](https://github.com/khulnasoft-lab/clix.py/pull/464) by [@Kobu](https://github.com/Kobu).
* ✏ Update `first-steps.md`, clarify distinction between parameter and argument. PR [#176](https://github.com/khulnasoft-lab/clix.py/pull/176) by [@mccarthysean](https://github.com/mccarthysean).
* ✏ Fix broken plac link. PR [#275](https://github.com/khulnasoft-lab/clix.py/pull/275) by [@mgielda](https://github.com/mgielda).

### Internal

* ✅ Add extra tests just for coverage because monkeypatching with strange imports confuses coverage. PR [#490](https://github.com/khulnasoft-lab/clix.py/pull/490) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 🔧 Tweak pytest coverage. PR [#485](https://github.com/khulnasoft-lab/clix.py/pull/485) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* ➕ Bring back pytest-cov because coverage can't detect pytest-xdist. PR [#484](https://github.com/khulnasoft-lab/clix.py/pull/484) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* ⬆ Bump actions/upload-artifact from 2 to 3. PR [#477](https://github.com/khulnasoft-lab/clix.py/pull/477) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump actions/checkout from 2 to 3. PR [#478](https://github.com/khulnasoft-lab/clix.py/pull/478) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#411](https://github.com/khulnasoft-lab/clix.py/pull/411) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* ⬆ Bump nwtgck/actions-netlify from 1.1.5 to 1.2.4. PR [#479](https://github.com/khulnasoft-lab/clix.py/pull/479) by [@dependabot[bot]](https://github.com/apps/dependabot).
* ⬆ Bump khulnasoft-lab/issue-manager from 0.2.0 to 0.4.0. PR [#481](https://github.com/khulnasoft-lab/clix.py/pull/481) by [@dependabot[bot]](https://github.com/apps/dependabot).
* 👷 Move from pytest-cov to coverage and Codecov to Smokeshow. PR [#483](https://github.com/khulnasoft-lab/clix.py/pull/483) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* ➕ Add extra Material for MkDocs deps for docs. PR [#482](https://github.com/khulnasoft-lab/clix.py/pull/482) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 🔧 Update Dependabot config. PR [#476](https://github.com/khulnasoft-lab/clix.py/pull/476) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).

## 0.6.1

### Fixes

* 🐛 Fix setting `FORCE_TERMINAL` with colors 2. PR [#424](https://github.com/khulnasoft-lab/clix.py/pull/424) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 🐛 Fix setting `FORCE_TERMINAL` with colors. PR [#423](https://github.com/khulnasoft-lab/clix.py/pull/423) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).

## 0.6.0

This release adds deep integrations with [Rich](https://rich.readthedocs.io/en/stable/). ✨

`rich` is an optional dependency, you can install it directly or it will be included when you install with:

```console
$ pip install "clix[all]"
```

If Rich is available, it will be used to show the content from `--help` options, validation errors, and even errors in your app (exception tracebacks).

There are new options to group commands, *CLI arguments*, and *CLI options*, support for [Rich Console Markup](https://rich.readthedocs.io/en/stable/markup.html), and more! 🎉

### Features

* ✨ Richify, add integrations with Rich everywhere. PR [#419](https://github.com/khulnasoft-lab/clix.py/pull/419) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
    * Recommend Rich as the main information displaying tool, new docs: [Printing and Colors](https://clix.khulnasoft.com/tutorial/printing/).
    * For most use cases not using Rich, use plain `print()` instead of `clix.echo()` in the docs, to simplify the concepts and avoid confusions. New docs: [Printing and Colors - clix Echo](https://clix.khulnasoft.com/tutorial/printing/#clix-echo).
    * Define help panels for *CLI arguments*, new docs: [CLI Arguments with Help - CLI Argument help panels](https://clix.khulnasoft.com/tutorial/arguments/help/#cli-argument-help-panels).
    * Define help panels for *CLI options*, new docs: [CLI Options with Help - CLI Options help panels](https://clix.khulnasoft.com/tutorial/options/help/#cli-options-help-panels).
    * New docs for deprecating commands: [Commands - Command Help - Deprecate a Command](https://clix.khulnasoft.com/tutorial/commands/help/#deprecate-a-command).
    * Support for Rich Markdown in docstrings, *CLI parameters* `help`, and `epilog` with the new parameter `clix.Clix(rich_markup_mode="markdown")`, new docs: [Commands - Command Help - Rich Markdown and Markup](https://clix.khulnasoft.com/tutorial/commands/help/#rich-markdown-and-markup).
    * Support for Rich Markup (different from Markdown) in docstrings, *CLI parameters* `help`, and `epilog` with the new parameter `clix.Clix(rich_markup_mode="rich")`, new docs: [Commands - Command Help - Rich Markdown and Markup](https://clix.khulnasoft.com/tutorial/commands/help/#rich-markdown-and-markup).
    * Define help panels for *commands*, new docs: [Commands - Command Help - Help Panels](https://clix.khulnasoft.com/tutorial/commands/help/#help-panels).
    * New docs for setting an `epilog`, with support for Rich Markdown and Console Markup, new docs: [Commands - Command Help - Epilog](https://clix.khulnasoft.com/tutorial/commands/help/#epilog).
* ✨ Refactor and document handling pretty exceptions. PR [#422](https://github.com/khulnasoft-lab/clix.py/pull/422) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
    * Add support for customizing pretty short errors, new docs: [Exceptions and Errors](https://clix.khulnasoft.com/tutorial/exceptions/).
* ✨ Allow configuring pretty errors when creating the Clix instance. PR [#416](https://github.com/khulnasoft-lab/clix.py/pull/416) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).

### Docs

* 📝 Add docs for using Rich with Clix. PR [#421](https://github.com/khulnasoft-lab/clix.py/pull/421) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
    * Add new docs: [Ask with Prompt - Prompt with Rich](https://clix.khulnasoft.com/tutorial/prompt/#prompt-with-rich).
    * Add new docs to handle progress bars and spinners with Rich: [Progress Par](https://clix.khulnasoft.com/tutorial/progressbar/).

### Internal

* ⬆️ Upgrade codecov GitHub Action. PR [#420](https://github.com/khulnasoft-lab/clix.py/pull/420) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).

## 0.5.0

### Features

* ✨ Add pretty error tracebacks for user errors and support for Rich. PR [#412](https://github.com/khulnasoft-lab/clix.py/pull/412) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).

### Docs

* ✏ Fix typo, "ASCII codes" to "ANSI escape sequences". PR [#308](https://github.com/khulnasoft-lab/clix.py/pull/308) by [@septatrix](https://github.com/septatrix).

## 0.4.2

### Fixes

* 🐛 Fix type conversion for `List` and `Tuple` and their internal types. PR [#143](https://github.com/khulnasoft-lab/clix.py/pull/143) by [@hellowhistler](https://github.com/hellowhistler).
* 🐛 Fix `context_settings` for a Clix app with a single command. PR [#210](https://github.com/khulnasoft-lab/clix.py/pull/210) by [@daddycocoaman](https://github.com/daddycocoaman).

### Docs

* 📝 Clarify testing documentation about checking `stderr`. PR [#335](https://github.com/khulnasoft-lab/clix.py/pull/335) by [@cgabard](https://github.com/cgabard).
* ✏ Fix typo in docs for CLI Option autocompletion. PR [#288](https://github.com/khulnasoft-lab/clix.py/pull/288) by [@graue70](https://github.com/graue70).
* 🎨 Fix header format for "Standard Input" in `docs/tutorial/printing.md`. PR [#386](https://github.com/khulnasoft-lab/clix.py/pull/386) by [@briancohan](https://github.com/briancohan).
* ✏ Fix typo in `docs/tutorial/terminating.md`. PR [#382](https://github.com/khulnasoft-lab/clix.py/pull/382) by [@kianmeng](https://github.com/kianmeng).
* ✏ Fix syntax typo in `docs/tutorial/package.md`. PR [#333](https://github.com/khulnasoft-lab/clix.py/pull/333) by [@ryanstreur](https://github.com/ryanstreur).
* ✏ Fix typo, duplicated word in `docs/tutorial/options/required.md`.. PR [#316](https://github.com/khulnasoft-lab/clix.py/pull/316) by [@michaelriri](https://github.com/michaelriri).
* ✏ Fix minor typo in `index.md`. PR [#274](https://github.com/khulnasoft-lab/clix.py/pull/274) by [@RmStorm](https://github.com/RmStorm).
* ✏ Fix double "and" typo in first-steps tutorial. PR [#225](https://github.com/khulnasoft-lab/clix.py/pull/225) by [@softwarebloat](https://github.com/softwarebloat).
* 🎨 Fix format in docs explaining `datetime` parameter type. PR [#220](https://github.com/khulnasoft-lab/clix.py/pull/220) by [@DiegoPiloni](https://github.com/DiegoPiloni).

### Internal

* ⬆ [pre-commit.ci] pre-commit autoupdate. PR [#404](https://github.com/khulnasoft-lab/clix.py/pull/404) by [@pre-commit-ci[bot]](https://github.com/apps/pre-commit-ci).
* 👷 Fix Material for MkDocs install in CI. PR [#395](https://github.com/khulnasoft-lab/clix.py/pull/395) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 👷 Add pre-commit CI config. PR [#394](https://github.com/khulnasoft-lab/clix.py/pull/394) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 👷 Clear MkDocs Insiders cache. PR [#393](https://github.com/khulnasoft-lab/clix.py/pull/393) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 🔧 Add pre-commit config and formatting. PR [#392](https://github.com/khulnasoft-lab/clix.py/pull/392) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 👷 Disable installing MkDocs Insiders in forks. PR [#391](https://github.com/khulnasoft-lab/clix.py/pull/391) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* ⬆️ Upgrade Codecov GitHub Action. PR [#383](https://github.com/khulnasoft-lab/clix.py/pull/383) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).

## 0.4.1

### Fixes

* 🐛 Fix import of `get_terminal_size` for Click 8.1.0 support and upgrade Black to fix CI. PR [#380](https://github.com/khulnasoft-lab/clix.py/pull/380) by [@khulnasoft-lab](https://github.com/khulnasoft-lab) based on original PR [#375](https://github.com/khulnasoft-lab/clix.py/pull/375) by [@madkinsz](https://github.com/madkinsz).

### Internal

* 📝 Add Jina's QA Bot to the docs to help people that want to ask quick questions. PR [#368](https://github.com/khulnasoft-lab/clix.py/pull/368) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 💚 Only test on push when on master, avoid duplicate CI runs from PRs. PR [#358](https://github.com/khulnasoft-lab/clix.py/pull/358) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* ✨ Add support for previewing docs in PRs from forks and enable MkDocs Insiders. PR [#357](https://github.com/khulnasoft-lab/clix.py/pull/357) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* ⬆️ Upgrade MkDocs Material, MDX-Include, and MkDocs structure. PR [#356](https://github.com/khulnasoft-lab/clix.py/pull/356) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 👷 Update publish GitHub action. PR [#325](https://github.com/khulnasoft-lab/clix.py/pull/325) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).

## 0.4.0

### Features

* ✨ Add support for Click 8 while keeping compatibility with Click 7. PR [#317](https://github.com/khulnasoft-lab/clix.py/pull/317) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).

### Internal

* 📝 Add Security policy. PR [#324](https://github.com/khulnasoft-lab/clix.py/pull/324) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 🔧 Add updated issue templates. PR [#323](https://github.com/khulnasoft-lab/clix.py/pull/323) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 👷 Enable tests for Python 3.9. PR [#322](https://github.com/khulnasoft-lab/clix.py/pull/322) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 👷 Add GitHub Action Latest Changes. PR [#321](https://github.com/khulnasoft-lab/clix.py/pull/321) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 👷 Update docs CI name. PR [#320](https://github.com/khulnasoft-lab/clix.py/pull/320) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).
* 🔧 Add sponsors docs and badge. PR [#319](https://github.com/khulnasoft-lab/clix.py/pull/319) by [@khulnasoft-lab](https://github.com/khulnasoft-lab).

## 0.3.2

### Features

* Add support for `mypy --strict`. Original PR [#147](https://github.com/khulnasoft-lab/clix.py/pull/147) by [@victorphoenix3](https://github.com/victorphoenix3).

### Docs

* Update docs with new `--help` showing default values. PR [#135](https://github.com/khulnasoft-lab/clix.py/pull/135) by [@victorphoenix3](https://github.com/victorphoenix3).
* Add `Optional` to docs for *CLI Arguments and Options* with a default of `None`. PR [#131](https://github.com/khulnasoft-lab/clix.py/pull/131) by [@rkbeatss](https://github.com/rkbeatss).
* Add valid date formats to docs. PR [#122](https://github.com/khulnasoft-lab/clix.py/pull/122) by [@IamCathal](https://github.com/IamCathal).

### Internal

* Report coverage in XML to support GitHub Actions. PR [#146](https://github.com/khulnasoft-lab/clix.py/pull/146).
* Update badges and remove Travis, now that GitHub Actions is the main CI. PR [#145](https://github.com/khulnasoft-lab/clix.py/pull/145).

## 0.3.1

* Add GitHub Actions, move from Travis. PR [#144](https://github.com/khulnasoft-lab/clix.py/pull/144).
* Pin dependencies. PR [#138](https://github.com/khulnasoft-lab/clix.py/pull/138).
* Add Dependabot. PR [#136](https://github.com/khulnasoft-lab/clix.py/pull/136).
* Upgrade Isort to version 5.x.x. PR [#137](https://github.com/khulnasoft-lab/clix.py/pull/137).

## 0.3.0

* Add support for `help` parameter in *CLI arguments*:
    * As `help` in *CLI arguments* is not supported by Click, there are two new internal classes (Click sub-classes) to support it:
        * `clix.core.ClixArgument`
        * `clix.core.ClixCommand`
    * This includes a new auto-generated help text section `Arguments` for *CLI arguments*, showing defaults, required arguments, etc.
    * It's also possible to disable it and keep the previous behavior, not showing automatic help for *CLI arguments* (Click's default) using the `hidden` parameter.
    * Now `show_default` is `True` by default.
    * And now `show_envvar` is `True` by default.
    * So, default values and env vars are shown in the help text by default, without having to manually enable them, for both *CLI arguments* and *CLI options*.
    * New docs:
        * [CLI Arguments Intro](https://clix.khulnasoft.com/tutorial/arguments/).
        * [Optional CLI Arguments](https://clix.khulnasoft.com/tutorial/arguments/optional/).
        * [CLI Arguments with Default](https://clix.khulnasoft.com/tutorial/arguments/default/).
        * [CLI Arguments with Help](https://clix.khulnasoft.com/tutorial/arguments/help/).
        * [CLI Arguments with Environment Variables](https://clix.khulnasoft.com/tutorial/arguments/envvar/).
        * [CLI Arguments: Other uses](https://clix.khulnasoft.com/tutorial/arguments/other-uses/).
        * [CLI arguments with tuples](https://clix.khulnasoft.com/tutorial/multiple-values/arguments-with-multiple-values/#cli-arguments-with-tuples).
    * Lot's of tests for all the new examples in the new docs, keeping coverage at 100%.
    * PR [#123](https://github.com/khulnasoft-lab/clix.py/pull/123).
* Add docs for calling packages with `python -m some_package` using `__main__.py`: [Building a Package: Support `python -m`](https://clix.khulnasoft.com/tutorial/package/#support-python-m-optional). PR [#121](https://github.com/khulnasoft-lab/clix.py/pull/121).
* Add support for `*args` and `**kwargs` when calling the Clix app, just like in Click. PR [#120](https://github.com/khulnasoft-lab/clix.py/pull/120) by [@teymour-aldridge](https://github.com/teymour-aldridge).
* Fix typos in README and main docs [#103](https://github.com/khulnasoft-lab/clix.py/pull/103) by [@mrcartoonster](https://github.com/mrcartoonster).
* Fix typo in docs. PR [#98](https://github.com/khulnasoft-lab/clix.py/pull/98) by [@mrcartoonster](https://github.com/mrcartoonster).
* Fix typos and rewording in docs. PR [#97](https://github.com/khulnasoft-lab/clix.py/pull/97) by [@mrcartoonster](https://github.com/mrcartoonster).
* Update GitHub Action issue-manager. PR [#114](https://github.com/khulnasoft-lab/clix.py/pull/114).

## 0.2.1

* Add support for forward references (types declared inside of strings). PR [#93](https://github.com/khulnasoft-lab/clix.py/pull/93).

## 0.2.0

* Add support for completion for commands/programs not available on startup.
    * This allows installing a Clix program/script in a virtual environment and still have completion globally installed.
    * PR [#92](https://github.com/khulnasoft-lab/clix.py/pull/92).
* Add note about `clix.echo()` and `print()` for colors in Windows. PR [#89](https://github.com/khulnasoft-lab/clix.py/pull/89).
* Upgrade Mkdocs-Material version, update contributing guide style. PR [#90](https://github.com/khulnasoft-lab/clix.py/pull/90).

## 0.1.1

* Fix completion evaluation for Bash and Zsh when the program is not installed/found. PR [#83](https://github.com/khulnasoft-lab/clix.py/pull/83).
* Fix completion script for Fish. PR [#82](https://github.com/khulnasoft-lab/clix.py/pull/82).
* Fix shell installation for Bash to `~/.bashrc` and update Windows development docs. PR [#81](https://github.com/khulnasoft-lab/clix.py/pull/81).
* Update coverage badge. PR [#78](https://github.com/khulnasoft-lab/clix.py/pull/78).

## 0.1.0

* Fix coverage instructions. PR [#72](https://github.com/khulnasoft-lab/clix.py/pull/72).
* Add docs for [Building a Package](https://clix.khulnasoft.com/tutorial/package/). PR [#71](https://github.com/khulnasoft-lab/clix.py/pull/71).
* Add docs for [Using Click (with Clix)](https://clix.khulnasoft.com/tutorial/using-click/). PR [#70](https://github.com/khulnasoft-lab/clix.py/pull/70).
* Add support for type-based callbacks and autocompletion functions, extra tests and docs:
    * Extra tests, raising coverage to 100%.
    * New docs: [Printing and Colors: "Standard Output" and "Standard Error"](https://clix.khulnasoft.com/tutorial/printing/#standard-output-and-standard-error).
    * New docs: [Password CLI Option and Confirmation Prompt](https://clix.khulnasoft.com/tutorial/options/password/).
    * Support for callbacks based on type annotations. New docs: [CLI Option Callback and Context](https://clix.khulnasoft.com/tutorial/options/callback-and-context/).
    * New docs: [Version CLI Option, is_eager](https://clix.khulnasoft.com/tutorial/options/version/).
    * Support for autocompletion functions based on type annotations. New docs: [CLI Option autocompletion](https://clix.khulnasoft.com/tutorial/options/autocompletion/).
    * New docs: [Commands: Using the Context](https://clix.khulnasoft.com/tutorial/commands/context/).
    * New docs: [Testing](https://clix.khulnasoft.com/tutorial/testing/).
    * PR [#68](https://github.com/khulnasoft-lab/clix.py/pull/68).
* Fix Zsh completion install script. PR [#69](https://github.com/khulnasoft-lab/clix.py/pull/69).
* Fix typo in progressbar example. PR [#63](https://github.com/khulnasoft-lab/clix.py/pull/63) by [@ValentinCalomme](https://github.com/ValentinCalomme).

## 0.0.11

* Re-implement completion system:
    * Remove optional dependency `click-completion` (with its sub-dependencies, like Jinja).
    * Add optional dependency `shellingham` to auto detect shell to install (it was used by `click-completion`).
    * Completion now doesn't require a third party library.
        * If `shellingham` is not installed/added as a dependency, `--install-completion` and `--show-completion` take a value with the name of the shell.
    * Fix support for user provided completion in *CLI Parameters*.
    * Fix completion for files in Bash, Zsh, and Fish.
    * Add support for modern versions of PowerShell, 5, 6, and 7 (e.g. in Windows 10).
    * Add support for `pwsh` (PowerShell Core).
        * PowerShell support includes help strings for commands and *CLI Parameters*.
    * Several bug fixes.
    * Tests for the completion logic/code.
    * Tested in all the shells in Linux and Windows.
    * PR [#66](https://github.com/khulnasoft-lab/clix.py/pull/66).
* Fix format in docs with highlighted lines. PR [#65](https://github.com/khulnasoft-lab/clix.py/pull/65).
* Add docs about [Clix CLI - completion for small scripts](https://clix.khulnasoft.com/clix-cli/). PR [#64](https://github.com/khulnasoft-lab/clix.py/pull/64).
* Add docs about [Alternatives, Inspiration and Comparisons](https://clix.khulnasoft.com/alternatives/). PR [#62](https://github.com/khulnasoft-lab/clix.py/pull/62).
* Add [Development - Contributing Guide](https://clix.khulnasoft.com/contributing/). PR [#61](https://github.com/khulnasoft-lab/clix.py/pull/61).

## 0.0.10

* Add support for Click version 7.1.1. PR [#60](https://github.com/khulnasoft-lab/clix.py/pull/60).

## 0.0.9

* Add support for PEP 561, to allow `mypy` to type check applications built with **Clix**. PR [#58](https://github.com/khulnasoft-lab/clix.py/pull/58).
* Upgrade deploy docs to Netlify GitHub action. PR [#57](https://github.com/khulnasoft-lab/clix.py/pull/57).
* Add support for Mermaid JS for visualizations. PR [#56](https://github.com/khulnasoft-lab/clix.py/pull/56).
* Update CI to run docs deployment in GitHub actions. PR [#50](https://github.com/khulnasoft-lab/clix.py/pull/50).
* Update format for internal links. PR [#38](https://github.com/khulnasoft-lab/clix.py/pull/38).
* Tweak external links' format. PR [#36](https://github.com/khulnasoft-lab/clix.py/pull/36).

## 0.0.8

* Update docs and add latest changes to MkDocs/website. PR [#33](https://github.com/khulnasoft-lab/clix.py/pull/33).
* Add extra tests for edge cases that don't belong in docs' examples. PR [#32](https://github.com/khulnasoft-lab/clix.py/pull/32).
* Add docs for CLI Parameters with [Multiple Values](https://clix.khulnasoft.com/tutorial/multiple-values/). Includes tests for all the examples and bug fixes. PR [#31](https://github.com/khulnasoft-lab/clix.py/pull/31).
* Add docs for extra *CLI parameter* types: [CLI Parameter Types: Number](https://clix.khulnasoft.com/tutorial/parameter-types/number/) and [CLI Parameter Types: Boolean CLI Options](https://clix.khulnasoft.com/tutorial/parameter-types/bool/). PR [#30](https://github.com/khulnasoft-lab/clix.py/pull/30).
* Extend docs for Commands, add [Commands: Clix Callback](https://clix.khulnasoft.com/tutorial/commands/callback/) and [Commands: One or Multiple](https://clix.khulnasoft.com/tutorial/commands/one-or-multiple/). This includes tests for all the examples and bug fixes. PR [#29](https://github.com/khulnasoft-lab/clix.py/pull/29).
* Add docs for [SubCommands - Command Groups](https://clix.khulnasoft.com/tutorial/subcommands/). This includes tests for all the examples and bug fixes. PR [#28](https://github.com/khulnasoft-lab/clix.py/pull/28).
* Remove unneeded code for argument handling. PR [#26](https://github.com/khulnasoft-lab/clix.py/pull/26).
* Add docs for [Launching Applications](https://clix.khulnasoft.com/tutorial/launch/). PR [#25](https://github.com/khulnasoft-lab/clix.py/pull/25).
* Add docs for getting the [CLI Application Directory](https://clix.khulnasoft.com/tutorial/app-dir/). PR [#24](https://github.com/khulnasoft-lab/clix.py/pull/24).
* Add docs for [Progress Bars](https://clix.khulnasoft.com/tutorial/progressbar/). PR [#23](https://github.com/khulnasoft-lab/clix.py/pull/23).
* Add docs for [Asking with Interactive Prompts](). PR [#22](https://github.com/khulnasoft-lab/clix.py/pull/22).
* Update docs for path *CLI option*. PR [#21](https://github.com/khulnasoft-lab/clix.py/pull/21).
* Add colors module and docs for [Printing and Colors](https://clix.khulnasoft.com/tutorial/printing/) and for [Terminating](https://clix.khulnasoft.com/tutorial/terminating/), including tests. PR [#20](https://github.com/khulnasoft-lab/clix.py/pull/20).
* Refactor docs to make each individual page/section "bite-sized" / small. Add docs for [CLI option names](https://clix.khulnasoft.com/tutorial/options/name/). Update `clix.Argument()` to remove invalid positional `param_decls`. PR [#19](https://github.com/khulnasoft-lab/clix.py/pull/19).

## 0.0.7

* Add docs for [*CLI parameter* types](https://clix.khulnasoft.com/tutorial/parameter-types/). Includes tests and file classes refactor. PR [#17](https://github.com/khulnasoft-lab/clix.py/pull/17).
* Add tests for completion. PR [#15](https://github.com/khulnasoft-lab/clix.py/pull/15) and [#16](https://github.com/khulnasoft-lab/clix.py/pull/16).

## 0.0.6

* Add docs for [Commands](https://clix.khulnasoft.com/tutorial/commands/). Includes a bug fix for handling default values set in `clix.Clix()` parameters. PR [#14](https://github.com/khulnasoft-lab/clix.py/pull/14).
* Add docs for [CLI Arguments](https://clix.khulnasoft.com/tutorial/arguments/). PR [#13](https://github.com/khulnasoft-lab/clix.py/pull/13).
* Add docs for [CLI Options](https://clix.khulnasoft.com/tutorial/options/). PR [#12](https://github.com/khulnasoft-lab/clix.py/pull/12).

## 0.0.5

* Clean exports from Clix. Remove unneeded components from Click and add needed `Exit` exception. PR [#11](https://github.com/khulnasoft-lab/clix.py/pull/11).
* Fix and document extracting help from a function's docstring [First Steps: Document your CLI app](https://clix.khulnasoft.com/tutorial/first-steps/#document-your-cli-app). PR [#10](https://github.com/khulnasoft-lab/clix.py/pull/10).
* Update references to `--install-completion` and `--show-completion` in docs. PR [#9](https://github.com/khulnasoft-lab/clix.py/pull/9).
* Fix testing utilities, add tests for First Steps examples. PR [#8](https://github.com/khulnasoft-lab/clix.py/pull/8).
* Add auto completion options by default when [click-completion](https://github.com/click-contrib/click-completion) is installed: `--install-completion` and `--show-completion`. PR [#7](https://github.com/khulnasoft-lab/clix.py/pull/7).
* Update Termynal to have fixed sizes, add "fast" button, and use it in [First Steps](https://clix.khulnasoft.com/tutorial/first-steps/). PR [#6](https://github.com/khulnasoft-lab/clix.py/pull/6).
* Add custom automatic [Termynal](https://github.com/khulnasoft-lab/termynal) for docs. PR [#5](https://github.com/khulnasoft-lab/clix.py/pull/5).

## 0.0.4

* Update short descriptions and assets.
* Docs rewording and fix typos. PR [#1](https://github.com/khulnasoft-lab/clix.py/pull/1) by [@mariacamilagl](https://github.com/mariacamilagl).

## 0.0.3

* Fix group creation without name.

## 0.0.2

* Add initial version of code, docs, etc.

## 0.0.1

* First commit. Publish to PyPI to reserve package name.
