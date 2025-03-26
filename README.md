---

# DeepSeek LLM Chat Pro 🤖

DeepSeek LLM Chat Pro is an advanced, interactive AI chatbot application that leverages state-of-the-art language models from Hugging Face. Built using [Streamlit](https://streamlit.io/) and [Hugging Face Transformers](https://huggingface.co/docs/transformers/index), this app offers a sleek, customizable chat interface for seamless user interaction with deep learning models.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

---

## Overview

DeepSeek LLM Chat Pro empowers users to interact with advanced language models in a user-friendly web environment. The application provides real-time text generation, complete with adjustable generation parameters such as temperature, max length, top-p, and repetition penalty. Additionally, users can choose from various prompt templates to streamline their queries and receive tailored responses.

---

## Features

- **Interactive Chat Interface:** A responsive UI built with Streamlit that supports conversation-based interactions.
- **Model Caching:** Efficient model loading and caching using Streamlit’s caching mechanisms for improved performance.
- **Customizable Generation Parameters:** Fine-tune the response output with settings like max length, temperature, top-p, and repetition penalty.
- **Prompt Templates:** Predefined templates help guide the model in generating summaries, answers, stories, and more.
- **API Key Integration:** Seamlessly integrate your Hugging Face API key for accessing protected models.
- **Custom CSS Styling:** Modern design with a clean, professional look that enhances the user experience.
- **Session Management:** Maintain conversation history across interactions with options to clear or save chats.
- **Export Conversations:** Save entire conversation sessions as JSON files for future reference or analysis.

---

## Technologies

This project is built using:
- **[Streamlit](https://streamlit.io/):** For building and deploying interactive web applications.
- **[Transformers](https://huggingface.co/docs/transformers):** For accessing and utilizing state-of-the-art language models.
- **[Hugging Face Hub](https://huggingface.co/docs/huggingface_hub):** For model hosting and API integration.
- **[PyTorch](https://pytorch.org/):** As the underlying deep learning framework powering the language models.

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/usama7871/AI-CHATBOT-
   cd AI-CHATBOT-
   ```

2. **Create and Activate a Virtual Environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   Ensure you have [pip](https://pip.pypa.io/en/stable/) installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` includes:

   ```
   streamlit
   transformers==4.30.0
   huggingface_hub
   torch==1.13.1
   ```

---

## Usage

1. **Start the Application:**

   In your terminal, run:

   ```bash
   streamlit run app.py
   ```

2. **Interact with the Chatbot:**

   - Open the provided local URL in your web browser.
   - Use the chat interface to ask questions or input prompts.
   - Adjust settings and select the desired model via the sidebar.
   - Save or clear chat sessions as needed.

3. **API Key (Optional):**

   If your selected model requires authentication, you can enter your Hugging Face API key directly through the sidebar.

---

## Configuration

The application is highly configurable:

- **Model Selection:** Choose between various models (e.g., DeepSeek-R1) directly from the sidebar. Additional models can be added by updating the model options.
- **Generation Parameters:** Adjust the text generation parameters:
  - **Max Length:** Control the length of the generated response.
  - **Temperature:** Modify the randomness in the output.
  - **Top P:** Adjust the nucleus sampling threshold.
  - **Repetition Penalty:** Prevent repetitive text generation.
- **Prompt Templates:** Use preset templates to tailor the conversation context. These include options for summarizing text, answering questions based on context, or even generating creative stories.

---

## Customization

Developers and users can easily extend the functionality:

- **Custom CSS Styling:** Modify the custom CSS in the app to better suit your brand or personal preferences.
- **Additional Prompt Templates:** Enhance the prompt templates dictionary to include more specialized templates.
- **Model Integration:** Integrate new models by updating the model options dictionary and ensuring compatibility with the Hugging Face API.
- **Session Management:** Customize how conversations are stored or exported by modifying the session state management and file saving functionality.

---

## Contributing

Contributions are welcome! If you have suggestions, feature requests, or bug fixes, please feel free to:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Submit a pull request detailing your changes.
4. Open issues for any bugs or enhancements.

Before contributing, please review the [contributing guidelines](CONTRIBUTING.md) (if available).

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute this software as per the license terms.

---

## Acknowledgements

- Special thanks to the [Streamlit Community](https://discuss.streamlit.io/) for their support and continuous improvements.
- Gratitude to [Hugging Face](https://huggingface.co/) for providing the powerful transformer models and easy-to-use APIs.
- Appreciation to all contributors and open-source developers who make projects like this possible.

---

## Contact

For any questions, feedback, or inquiries, please contact:

- **Usama**  
  GitHub: [usama7871](https://github.com/usama7871)  
  Email: *kusamakhan1234@gmail.com* 

---

DeepSeek LLM Chat Pro is continuously evolving. We welcome contributions that further enhance its capabilities and usability. Happy chatting!

---