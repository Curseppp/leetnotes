# Leetnotes
[![CI](https://github.com/Curseppp/leetnotes/actions/workflows/ci.yml/badge.svg)](https://github.com/Curseppp/leetnotes/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.13%2B-blue)
![Code style](https://img.shields.io/badge/code%20style-ruff-blue)
![uv](https://img.shields.io/badge/package%20manager-uv-blue)

CLI tool for tracking LeetCode problems.

## Installation
To install dependencies, use uv - An extremely fast Python package and project manager, written in Rust (by Astral).
```
uv sync
```
## Usage

Initialize the database:

```bash

leetnotes init

```
Add a problem:

```bash

leetnotes add 1 "Two Sum" easy

```

Show all problems:

```bash

leetnotes show

```

Filter problems:

```bash

leetnotes show --difficulty medium

leetnotes show --status solved

```

Update problem status:

```bash

leetnotes edit-status 1 solved

```

Show statistics:

```bash

leetnotes stats difficulty

leetnotes stats status

```

Open problem in browser:

```bash

leetnotes open 1

```

Delete problem:

```bash

leetnotes delete 1

```