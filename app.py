import os
import time
import datetime
import json
import streamlit as st
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import login

st.set_page_config(page_title="DeepSeek LLM Chat Pro", page_icon="🤖", layout="wide")
st.title("DeepSeek LLM Chat Pro 🚀")
st.markdown("Interact with advanced DeepSeek models and customize your chat experience!")

st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .st-title, .st-markdown h1 { color: #007bff; }
    .st-sidebar { background-color: #e9ecef; border-right: 1px solid #ced4da; }
    .st-button { background-color: #28a745 !important; color: white !important; border: none !important; padding: 10px 20px !important; border-radius: 5px !important; }
    .st-button:hover { background-color: #218838 !important; }
    .st-text-area { border: 1px solid #ced4da; border-radius: 5px; }
    .st-slider { color: #17a2b8; }
    .st-success { color: #28a745; }
    .st-error { color: #dc3545; }
    .st-info { color: #17a2b8; }
    .chat-bubble {
        background-color: #f0f8ff;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 12px;
        word-wrap: break-word;
        color: #333;
        border: 1px solid #e0e0e0;
    }
    .user-bubble {
        background-color: #e6f7ff;
        border-radius: 8px;
        padding: 12px;
        margin-bottom: 12px;
        word-wrap: break-word;
        color: #0056b3;
        text-align: right;
        border: 1px solid #cceeff;
    }
    .st-chat-input { border-top: 1px solid #dee2e6; padding-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

@st.cache_resource(show_spinner=True)
def load_model(model_name, hf_api_key=None):
    try:
        if hf_api_key:
            login(token=hf_api_key)
        tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)
        gen_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)
        return gen_pipeline, tokenizer
    except Exception as e:
        st.error(f"Model loading failed: {e}")
        return None, None

with st.sidebar:
    st.header("⚙️ Settings")
    st.markdown("---")

    hf_api_key_source = st.radio("🔑 Hugging Face API Key", ["Not Required (Public Model)", "Enter Manually"], index=0)
    hf_api_key = None
    if hf_api_key_source == "Enter Manually":
        hf_api_key = st.text_input("Enter Your API Key", type="password")
        if hf_api_key:
            st.success("🔑 API Key Entered.")
        else:
            st.warning("🔑 API Key not provided. Using public access.")

    st.markdown("---")
    st.subheader("🤖 Model Selection")
    model_options = {
        "DeepSeek-R1": "deepseek-ai/DeepSeek-R1",
        "Mistral 7B": "mistralai/Mistral-7B-v0.1",
        "OpenChat": "openchat/openchat-3.5-0106"
    }
    selected_model_name = st.selectbox("Choose a Model", list(model_options.keys()))
    selected_model = model_options[selected_model_name]

    st.markdown("---")
    st.subheader("⚙️ Generation Parameters")
    max_length = st.slider("Max Length", 32, 2048, 512, 32)
    temperature = st.slider("Temperature", 0.01, 1.0, 0.7, 0.01)
    top_p = st.slider("Top P", 0.01, 1.0, 0.95, 0.01)
    repetition_penalty = st.slider("Repetition Penalty", 1.0, 2.0, 1.0, 0.05)

    st.markdown("---")
    st.subheader("💡 Prompt Templates")
    prompt_templates = {
        "Default": "",
        "Summarize Text": "Please summarize the following text:\n\n{text}",
        "Answer Question": "Answer the following question based on the context:\n\nQuestion: {question}\nContext: {context}",
        "Write a Story": "Write a short story about {topic}",
    }
    selected_template = st.selectbox("Select a Template", list(prompt_templates.keys()))
    if selected_template != "Default":
        st.info(f"Selected Template: {selected_template}")

pipe, tokenizer = load_model(selected_model, hf_api_key)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello! Ask me anything."}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        bubble_class = 'user-bubble' if msg["role"] == "user" else 'chat-bubble'
        st.markdown(f"<div class='{bubble_class}'>{msg['content']}</div>", unsafe_allow_html=True)

if prompt := st.chat_input("Ask a question or enter a prompt"):
    if not pipe:
        st.error("Model failed to load. Check your API key and connection.")
    else:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(f"<div class='user-bubble'>{prompt}</div>", unsafe_allow_html=True)
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            try:
                start_time = time.time()
                generation_kwargs = {
                    "max_length": max_length,
                    "num_return_sequences": 1,
                    "temperature": temperature,
                    "top_p": top_p,
                    "repetition_penalty": repetition_penalty,
                    "pad_token_id": tokenizer.eos_token_id
                }
                output = pipe(prompt, **generation_kwargs)
                generation_time = time.time() - start_time
                full_response = output[0]['generated_text']
                message_placeholder.markdown(f"<div class='chat-bubble'>{full_response}</div>", unsafe_allow_html=True)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                st.info(f"Generated in {generation_time:.2f} seconds.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

if selected_template != "Default" and prompt:
    template_text = prompt_templates[selected_template]
    if "{text}" in template_text:
        formatted_text = template_text.replace("{text}", prompt)
        st.session_state.messages[-1]["content"] = formatted_text
        st.experimental_rerun()
    elif "{question}" in template_text and "{context}" in template_text:
        st.warning("Please provide both a question and context for this template.")
    elif "{topic}" in template_text:
        formatted_text = template_text.replace("{topic}", prompt)
        st.session_state.messages[-1]["content"] = formatted_text
        st.experimental_rerun()
    else:
        st.warning("The selected template does not match your input.")

col1_clear, col2_save = st.columns([1, 1])
if col1_clear.button("🗑️ Clear Chat"):
    st.session_state.messages = [{"role": "assistant", "content": "Chat cleared. Start a new conversation!"}]
    st.experimental_rerun()

def save_chat(messages):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"deepseek_chat_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(messages, f, indent=4)
    st.success(f"Conversation saved as: {filename}")

if col2_save.button("💾 Save Chat"):
    if st.session_state.messages:
        save_chat(st.session_state.messages)
    else:
        st.warning("No conversation to save.")

st.markdown("---")
st.markdown("Developed with ❤️ using [Streamlit](https://streamlit.io/) and [Hugging Face Transformers](https://huggingface.co/docs/transformers/index).")
current_time_pk = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5)))
st.markdown(f"Current Location: Karachi, Sindh, Pakistan. (Time: {current_time_pk.strftime('%Y-%m-%d %H:%M:%S')} PKT)")

