# ECG-Wavelet-Analysis

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for Python package and environment management. `uv` is a fast, modern replacement for `pip` and `venv`.

### Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or with Homebrew:

```bash
brew install uv
```

### Install dependencies and run

```bash
# Create a virtual environment and install dependencies
uv sync

# Run the project
uv run main.py
```

`uv sync` reads `pyproject.toml` and installs all dependencies into an isolated `.venv`. You never need to manually activate the environment — `uv run` handles it.

### Managing packages

```bash
# Add a package
uv add numpy

# Add a dev-only package
uv add --dev pytest

# Remove a package
uv remove numpy
```

Running `uv add` or `uv remove` automatically updates `pyproject.toml` and `uv.lock`.

## Data

This project uses the [MIT-BIH Arrhythmia Database](https://physionet.org/content/mitdb/1.0.0/) from PhysioNet.

Download the dataset with:

```bash
wget -r -N -c -np https://physionet.org/files/mitdb/1.0.0/
```

This will create a `physionet.org/` directory containing the raw ECG recordings. The `-N` flag skips files that are already up to date, so re-running the command is safe.
