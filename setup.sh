#!/bin/bash

echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Setting up environment variables..."
touch .env
echo "HUGGINGFACE_API_KEY=your_huggingface_api_key_here" >> .env

echo "Setup completed! Run 'streamlit run app.py' to start the chatbot."
