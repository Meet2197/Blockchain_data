# Simple Blockchain with Flask API

This is a simple implementation of a blockchain in Python. The blockchain is backed by a Flask API, which provides a way to view and save the blockchain as a JSON file. The blockchain contains blocks, each with data, a hash, and the previous block’s hash.

## Features

- Create a blockchain with a Genesis block (the first block in the chain).
- Add new blocks to the blockchain.
- Expose the blockchain as a JSON object via a Flask API endpoint.
- Save the blockchain to a JSON file for persistence.

## Prerequisites

Make sure you have the following installed on your machine:

- Python 3.x
- `pip` (Python's package installer)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/simple-blockchain-flask.git
   cd simple-blockchain-flask

   Create a virtual environment (optional but recommended):

bash

python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install the required dependencies:

bash

pip install -r requirements.txt
If you don’t have a requirements.txt file, you can manually install Flask using:

bash

pip install flask
Usage
Run the server:

bash

python blockchain_server.py
Access the blockchain via your web browser or using curl:

To view the blockchain in JSON format:

bash

http://127.0.0.1:5000/blockchain
To save the blockchain to a blockchain.json file:

bash

http://127.0.0.1:5000/save
Example Output
/blockchain endpoint:
The /blockchain endpoint will return the entire blockchain in JSON format.

json

[
    {
        "index": 0,
        "timestamp": "2025-02-04 12:34:56.789101",
        "data": "Genesis Block",
        "previous_hash": "0",
        "hash": "a2f3d79c234..."
    },
    {
        "index": 1,
        "timestamp": "2025-02-04 12:35:56.789101",
        "data": "Block #1 data",
        "previous_hash": "a2f3d79c234...",
        "hash": "3e4f8e2348..."
    }
]
/save endpoint:
The /save endpoint saves the blockchain to a blockchain.json file. You should see the following message:

bash

Blockchain saved to blockchain.json!
Notes
The blockchain is a simple implementation for educational purposes.
Each block contains an index, timestamp, data, hash of the current block, and the hash of the previous block.
The blockchain is saved to a blockchain.json file using the /save endpoint.
The API is built using Flask and can be expanded to include other features like mining or validation.
License
This project is licensed under the MIT License - see the LICENSE file for details.

sql


### Steps to Use This `README.md`:

1. Copy the above content and save it in a `README.md` file in the root directory of your project.
2. Update the GitHub repository URL to your actual repository URL if needed.
3. Commit the file to your repository:

```bash
git add README.md
git commit -m "Add README file"
git push origin main
