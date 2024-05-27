# Deactivate current virtual environment
deactivate

# Update Python and create a new virtual environment
sudo apt-get update
sudo apt-get install python3.9 python3.9-venv

# Create a new virtual environment
python3.9 -m venv venv

# Activate the new virtual environment
source venv/bin/activate

# Install your project dependencies
pip install -r requirements.txt
