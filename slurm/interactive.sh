#!/bin/bash --login

# 1. Load system modules
module load apps/binapps/conda/miniforge3/25.9.1
module load apps/binapps/ollama/0.30.6
module load libs/nvidia-hpc-sdk/23.1

# 2. Activate Conda environment and install dependencies
conda activate env
pip install -r requirements.txt

# 3. Setup and start Ollama in the background
pkill ollama || true
sleep 1
unset ROCR_VISIBLE_DEVICES
export OLLAMA_HOST=0.0.0.0:11434
ollama serve > ollama.log 2>&1 &

echo "Waiting for Ollama server to spin up..."
sleep 10


echo "Ollama initialization complete!"