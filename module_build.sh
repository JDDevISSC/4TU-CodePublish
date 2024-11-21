#!/bin/bash

# Ensure the script exits on error
set -e

# Build the package (this creates the dist/ directory with .tar.gz and .whl files)
echo "Building the package..."
python -m build