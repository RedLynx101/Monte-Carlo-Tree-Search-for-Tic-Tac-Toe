## 4x4 Tic‑Tac‑Toe with Monte Carlo Tree Search (MCTS)

An interactive Jupyter notebook that implements a 4x4 Tic‑Tac‑Toe game engine and a Monte Carlo Tree Search (MCTS) player using UCT. The notebook runs small experiments (baseline, MCTS vs random, hyperparameter sweep) and visualizes results.

### What’s inside
- `IAI_HW2_nhicks.ipynb`: main notebook — implements the game, MCTS, and experiments; produces plots and summary metrics.
- `IAI_HW2_nhicks.html`: static HTML export of the executed notebook (for quick viewing without a Python environment).

### Highlights
- 4x4 game engine with clear APIs: `available_moves`, `make_move`, `undo_move`, `check_winner`, `clone`.
- MCTS with UCT child selection and random rollouts.
- Experiments:
  - Random vs Random (baseline)
  - MCTS (X) vs Random (O)
  - Exploration weight C sweep with a win‑rate plot
- Reproducible runs via fixed RNG seeds.

## Quickstart

### Requirements
- Python 3.9+

### Set up (Windows PowerShell)
```powershell
cd "C:\...\Monte Carlo Tree Search for Tic-Tac-Toe"
python -m venv .venv
 .\.venv\Scripts\Activate
python -m pip install --upgrade pip
pip install numpy matplotlib jupyter
```

### Run the notebook
```powershell
jupyter notebook IAI_HW2_nhicks.ipynb
```
Then use Run All to reproduce the experiments end‑to‑end. You can also open `IAI_HW2_nhicks.html` for a static, non‑interactive view.

## What the notebook does
- Builds a simple, readable 4x4 Tic‑Tac‑Toe engine (players: X first, O second)
- Implements MCTS with UCT: \(\bar{Q}_i + C\sqrt{\frac{\ln N_p}{N_i}}\)
- Runs and reports:
  - Average X score for Random vs Random (win=1, draw=0.5, loss=0)
  - Average X score for MCTS vs Random
  - Win rate vs exploration weight C (line plot)

Seeds for both `random` and `numpy.random` are set at the start of the experiment section for reproducibility. You can adjust iteration counts and the list of C values in the experiment cells if you want to explore different settings or runtimes.

## Results at a glance
- Baseline Random vs Random typically centers near a 0.5 average score for X.
- MCTS (as X) consistently outperforms a random opponent; exact numbers depend on iteration budget and C.
- The C sweep highlights a reasonable range for exploration; use the plot in the notebook to pick a value that balances exploration and exploitation for your runtime budget.

## Design notes
- The implementation favors clarity and explicit naming over micro‑optimizations.
- Dependencies are minimal: `numpy`, `matplotlib`, and `jupyter` for the notebook environment.

If you have questions or suggestions, feel free to open an issue or reach out.


