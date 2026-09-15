# Open Python for WRR Data Project - Starter Template

This repository is a starter for the student project. It gives you a clean, reproducible Python setup for water resources research (WRR) analyses with geodata and GDAL - the same structure professionals use, scaled down to project size.

## Quick start

1. Install [Miniforge](https://conda-forge.org/download/) (gives you `mamba`; if you already use `conda`, that works too - just replace `mamba` with `conda` below).
2. Clone this repository and **change into its folder** (the environment installs this project's own code, so the folder matters):
   ```bash
   mamba env create -f environment.yml
   mamba activate wrr-proj
   ```
3. Enable the automatic code checks (one time only):
   ```bash
   pre-commit install
   ```
4. Run the pipeline end-to-end to verify everything works:
   ```bash
   make all
   ```
   You should see a normal-depth result printed, a CSV in `results/`, and a figure in `figures/`.

On Windows without `make`: run the commands inside the `Makefile` directly, e.g. `python -m wrr.scripts.run_analysis`.

## Repo structure

```
.
├── environment.yml        # the reproducible environment (conda-forge)
├── Makefile               # one command per pipeline step
├── pyproject.toml         # makes src/wrr an installable package
├── ruff.toml              # code style rules (ruff lints AND formats)
├── .pre-commit-config.yaml
├── notebooks/             # your deliverables: project definition + results report
├── src/wrr/               # your reusable functions live HERE, not in notebooks
│   ├── standard_step.py   # 1D hydraulics (Manning, normal depth, GVF profile)
│   ├── gdal_utils.py      # raster/geodata helpers (you complete these)
│   └── scripts/           # pipeline entry points (prepare_data, run_analysis)
├── tests/                 # example unit tests - copy the pattern for your code
├── data/                  # not tracked; document sources in data/README.md
├── gdal/                  # log of the exact GDAL commands you used and why
├── prompts/               # your AI collaboration diary (mandatory)
├── results/               # generated outputs (wiped by make clean)
└── figures/               # generated figures (wiped by make clean)
```

The rule of thumb: **notebooks tell the story, `src/wrr/` does the work.** Write functions in `src/wrr/`, test them in `tests/`, and call them from notebooks and scripts. Because the environment installs the package in editable mode, `from wrr.standard_step import normal_depth_rectangular` works everywhere.

## Make targets

```bash
make data      # prepare/download input data (you implement this)
make build     # run the analysis; writes results/ and figures/
make test      # fast tests (no geodata needed)
make test-all  # all tests, including those needing GDAL/rasterio
make lint      # check code style without changing files
make fmt       # auto-format your code
make clean     # remove generated outputs
make all       # data + build + test
```

## What you must customize

1. Fill in `notebooks/project-definition-TEMPLATE.ipynb` with your site, flows, and parameters, and build your `notebooks/results-report.ipynb` on top of it.
2. Replace the placeholder steps in `src/wrr/gdal_utils.py` and `src/wrr/scripts/` with your AOI (area of interest) and CRS.
3. Fill `data/README.md` with your sources, licenses, CRS, and checksums.
4. Add at least one test per function you write (see `tests/` for the pattern).
5. Keep the AI diary in `prompts/AI_DIARY_TEMPLATE.md` up to date.

## Working with AI assistants ("vibe coding" done right)

You are encouraged to use LLM tools (Claude, ChatGPT, Copilot, ...) - that is how engineers work now. But **you remain the engineer**: the AI is a fast junior assistant, and you sign off on the result. Rules for this project:

1. **Never commit code you cannot explain.** If the AI wrote it, ask it to walk you through the code line by line until you could rewrite it yourself.
2. **Verify with hydraulics, not with vibes.** Check AI-generated formulas against a hand calculation, a textbook case, or a physical limit (e.g. Froude = 1 at critical depth) - then freeze that check as a unit test in `tests/`.
3. **Give the AI context.** Paste the relevant function and the error message, state units and CRS explicitly. Vague prompts produce plausible-looking, wrong hydraulics.
4. **Watch the units and the CRS.** These are the two classic failure modes of AI-generated geodata code - and exactly what you, not the AI, are trained to catch.
5. **Log it in the AI diary** (`prompts/AI_DIARY_TEMPLATE.md`): what you asked, what you accepted or rejected, and how you verified it. Honest entries are part of the grade; "I didn't use AI" with AI-style code is not a good look.
6. **Let the tools backstop you:** `make lint` and the pre-commit hooks catch many mechanical mistakes; `make test` catches the engineering ones - but only for things you wrote tests for.

## Notes

- Heavy geospatial libraries (GDAL, rasterio, geopandas; 1+ GB) are installed from conda-forge via `environment.yml` because pip installs of GDAL are unreliable. Always install/update them by editing `environment.yml` and running `mamba env update -f environment.yml`, not with ad-hoc `pip install`.
- Generated files (`results/`, `figures/`, raw data) stay out of git; a pre-commit hook blocks accidental commits of large files.
- Continuous integration (`.github/workflows/ci.yml`) runs the style checks and tests on every push - if it turns red, read the log; it tells you exactly what failed.
