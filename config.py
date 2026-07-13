"""
Global configuration file for the Bosch CNC Edge Intelligence project.
"""

from pathlib import Path

# Root directory
PROJECT_ROOT = Path(__file__).resolve().parent

# Dataset directory
DATASET_DIR = PROJECT_ROOT / "datasets" / "bosch_cnc"

# Results directory
RESULTS_DIR = PROJECT_ROOT / "results"

# Models directory
MODELS_DIR = PROJECT_ROOT / "models"

# Figures directory
FIGURES_DIR = PROJECT_ROOT / "figures"

# Random seed
RANDOM_STATE = 42

# Test split
TEST_SIZE = 0.20
