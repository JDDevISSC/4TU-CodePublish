#!/bin/sh

# Ensure the script exits on error
set -e

# Locate the latest wheel file in dist/
latest_wheel=$(ls dist/*.whl -t | head -n 1)

# Check if we found a wheel file
if [ -z "$latest_wheel" ]; then
    echo "No wheel file found in the dist/ directory. Exiting."
    exit 1
fi

echo "Found wheel file: $latest_wheel"

# Install the latest wheel file
echo "Installing the latest wheel file..."
pip install "$latest_wheel" --force-reinstall

echo "Installation complete."