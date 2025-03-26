import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

DEFAULT_MODEL = "deepseek-ai/deepseek-llm"
DEFAULT_MAX_LENGTH = 1024
DEFAULT_TEMPERATURE = 0.7
