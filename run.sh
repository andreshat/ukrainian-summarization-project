#!/bin/bash

# Check if the virtual environment exists
if [ ! -d "venv" ]; then
  # Create the virtual environment
  echo "Creating virtual environment..."
  python3 -m venv venv
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Check if requirements are installed
if ! pip freeze | grep -q transformers; then
  # Install requirements
  echo "Installing requirements..."
  pip install -r requirements.txt
fi

# Load environment variables
echo "Loading environment variables..."
source env_vars/wandb_vars.sh

# Run training script
echo "Running training script..."
# Example: python code/train.py --model_config configs/model_bart_config.json --dataset_config configs/dataset_xlsum_v2_ukr_config.json
