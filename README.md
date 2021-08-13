### Instructions for use (OSX/MacIntosh)

# A. Setting up Python

1. Ensure that homebrew is installed on your computer.

Navigate to `https://brew.sh/` and follow the instructions for installing homebrew.

2. Ensure Python 3 is installed on your computer.

On OSX, type in `brew install python3` in the terminal.
Type in `python3 --version` and hit enter in the terminal.
You should see something like `Python 3.8.10` on the next line in the terminal.

3. Create a virtual environment by typing the following into terminal and hitting enter:

`python3 -m venv ~/dev/environments/world_modellers`

4. Activate the virtual environment:

`source ~/dev/environments/world_modellers/bin/activate`

5. Install the requirements for running the parquet_to_csv file

`python3 -m pip install -r requirements.txt`

# B. Running the script

1. Copy your parquet file on your computer and paste it into the `parquet_to_csv` folder.

2. Run the script:

Suppose your filename is `input.parquet.gzip`.
In terminal, type `python3 parquet_to_csv.py input.parquet.gzip output.csv`.
At this point you should see an `output.csv` file in the `parquet_to_csv` folder.