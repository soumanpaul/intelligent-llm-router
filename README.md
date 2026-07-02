# Intelligent LLM Router

Train a small, fast classifier that reads a user prompt and picks the best downstream LLM for the job.

Instead of sending every request to one large model, a router can send simple questions to a cheap model and hard tasks to a stronger one. This project builds that router as a **text classifier** using [ModernBERT](https://huggingface.co/answerdotai/ModernBERT-base) on Hugging Face.

---

## How it works

```
User prompt  →  Router model  →  Label (which LLM to use)  →  Selected LLM
```

1. A labeled dataset maps prompts to the model that should handle them.
2. ModernBERT is fine-tuned on those labels.
3. At inference time, the router classifies a new prompt and returns the best model choice.

---

## Project status

This repo is in **early development**. The folder structure, config, and data-loading helpers are in place. Training, evaluation, and inference pipelines are scaffolded but not implemented yet.

| Component              | Status        |
| ---------------------- | ------------- |
| Data exploration       | Notebook ready |
| Dataset loading        | Basic helper  |
| Model training         | Planned       |
| Evaluation             | Planned       |
| Inference / routing    | Planned       |

---

## Requirements

- Python **3.10+** (3.13 tested locally)
- A machine with enough RAM/GPU for BERT fine-tuning
- Optional: [Hugging Face token](https://huggingface.co/settings/tokens) for gated models or datasets

---

## Quick start

### 1. Clone and enter the repo

```bash
git clone https://github.com/soumanpaul/intelligent-llm-router.git
cd intelligent-llm-router
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
```

### 3. Install dependencies

Install the package in editable mode plus pinned requirements:

```bash
pip install -e .
pip install -r requirements.txt
```

> **Note:** `requirements.txt` installs `transformers` from a specific Git commit because ModernBERT support may not be in the latest PyPI release yet.

### 4. (Optional) Set environment variables

```bash
cp .env.example .env
```

Edit `.env` and add your Hugging Face token if needed:

```bash
HF_TOKEN=your_token_here
```

### 5. Explore the data

Open the starter notebook:

```bash
jupyter notebook notebooks/01_data_exploration.ipynb
```

It loads a sample dataset and inspects labels. By default the notebook uses `legacy-datasets/banking77` as a stand-in while you experiment. The real router dataset is configured in `configs/default.yaml`.

---

## Configuration

All defaults live in [`configs/default.yaml`](configs/default.yaml).

| Section    | What it controls                                      |
| ---------- | ----------------------------------------------------- |
| `data`     | Hugging Face dataset ID and local cache directory     |
| `model`    | Base model name, max sequence length, number of labels |
| `training` | Epochs, batch size, learning rate, checkpoint paths  |
| `inference`| Checkpoint to load and how many top labels to return  |

Key dataset settings:

```yaml
data:
  dataset_id: DevQuasar/llm_router_dataset-synth   # target router dataset
  placeholder_dataset_id: legacy-datasets/banking77 # used for early experiments
  cache_dir: data/cache
```

Change `dataset_id` when you are ready to train on the real router data.

---

## Project layout

```
intelligent-llm-router/
├── configs/                 # YAML configuration
│   └── default.yaml
├── data/                    # Local dataset cache (gitignored)
├── notebooks/               # Jupyter experiments
│   └── 01_data_exploration.ipynb
├── scripts/                 # Command-line entry points
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
├── src/llm_router/          # Core Python package
│   ├── data/                # Dataset loading
│   ├── models/              # Router model wrapper
│   ├── training/            # Fine-tuning logic
│   ├── evaluation/          # Metrics
│   └── inference/           # Runtime routing
├── tests/
├── outputs/                 # Checkpoints and logs (gitignored, created at runtime)
├── pyproject.toml
└── requirements.txt
```

---

## Using the Python package

Load a dataset from Python:

```python
from llm_router.data.loading import load_router_dataset

dataset = load_router_dataset("legacy-datasets/banking77")
print(len(dataset["train"]), len(dataset["test"]))
```

---

## CLI scripts

Scripts are wired up with argument parsing but raise `NotImplementedError` until the pipelines are built.

```bash
# Fine-tune the router (not yet implemented)
python scripts/train.py --config configs/default.yaml

# Evaluate a checkpoint (not yet implemented)
python scripts/evaluate.py --config configs/default.yaml --checkpoint outputs/checkpoints/best

# Route a single prompt (not yet implemented)
python scripts/predict.py "Explain quantum entanglement in simple terms."
```

---

## Development

Run tests (when added):

```bash
pip install -e ".[dev]"
pytest
```

---

## Roadmap

- [ ] Implement ModernBERT fine-tuning in `src/llm_router/training/`
- [ ] Add evaluation metrics (accuracy, F1, confusion matrix)
- [ ] Wire up `scripts/predict.py` for live routing
- [ ] Switch from placeholder dataset to `DevQuasar/llm_router_dataset-synth`
- [ ] Add tests for data loading and config parsing

---

## License

No license file has been added yet. Add one before open-sourcing or sharing publicly.
