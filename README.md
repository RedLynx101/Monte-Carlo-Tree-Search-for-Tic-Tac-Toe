# Monte Carlo Tree Search for 4x4 Tic-Tac-Toe

This is a Carnegie Mellon 95-891 Introduction to AI course artifact by Noah Hicks. The notebook
implements a 4x4 Tic-Tac-Toe engine and a Monte Carlo Tree Search player using Upper Confidence
Bounds for Trees (UCT), then compares seeded random play with MCTS-guided play.

The point of the project is the search and evaluation loop, not a polished game interface.

## What is here

- `IAI_HW2_nhicks.ipynb` contains the engine, MCTS implementation, experiments, explanations, and
  plots.
- `IAI_HW2_nhicks.html` is a static export for reading the executed notebook without Python.
- `scripts/verify_notebook.py` reruns the notebook from a clean kernel and records the outputs under
  `verification/latest/`.
- `requirements-verification.txt` pins the environment used for the latest verification run.

The implementation includes:

- a 4x4 board with move, undo, clone, terminal-state, and winner detection;
- MCTS expansion, random rollout, backpropagation, and UCT child selection;
- a random-versus-random baseline;
- MCTS as X against a random O player; and
- an exploration-weight sweep.

## Reproduced results

A clean Python 3.11.5 run on August 16, 2026 reproduced the checked-in results:

| Experiment | Configuration | Average X score |
|---|---|---:|
| Random vs. random | 50 games, seed 42 | 0.54 |
| MCTS vs. random | 50 games, 400 search iterations per MCTS move, C=1.4 | 1.0 |
| Best observed C in the sweep | 200 games per value, 300 iterations per move, C=0.5 | 0.9925 |

The score is 1 for an X win, 0.5 for a draw, and 0 for an X loss. These are small, seeded
experiments against a random opponent. They do not establish a general benchmark or optimal play.
The reported search is purpose-built for MCTS playing X; the final root-child selection is not a
generic two-sided agent interface.

The clean verification run took about 256 seconds on the verification machine. Runtime will vary.

## Reproduce the notebook

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-verification.txt
python scripts\verify_notebook.py
```

The verifier writes an executed notebook, a static HTML export, a machine-readable result summary,
and the reproduced plot to `verification/latest/`. That directory is intentionally ignored by Git.

You can also open the notebook in Jupyter and run all cells manually.

## Authorship and assistance

The notebook records Noah Hicks as the author. It also records use of GPT-5 inline autocomplete in
Cursor during development; Noah reviewed the work and takes responsibility for the implementation
and conclusions.

## Public access and reuse

The source is publicly viewable. This repository does not currently include a software license, so
public visibility should not be interpreted as permission to reuse or redistribute the code beyond
what applicable law permits.
