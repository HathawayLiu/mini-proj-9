import streamlit as st
import transformers
import tensorflow as tf
from transformers import pipeline, set_seed
set_seed(42)
generator = pipeline('text-generation', model='gpt2-medium')
@st.cache_data
def main():
    st.set_page_config(page_title="Q&A with Me!", page_icon=":question:", layout="wide")

    # HTML and CSS Styling
    st.markdown("""
    <style>
        .container {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .textbox {
            width: 80%;
            margin: 20px;
            padding: 15px;
            border: none;
            border-radius: 10px;
            box-shadow: 0 0 10px 0 rgba(0,0,0,0.1);
            resize: none;
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
            outline: none;
            color: #fff;
            background-color: #2a9d8f;
            border: none;
            border-radius: 15px;
            box-shadow: 0 9px #999;
        }
        .button:hover {background-color: #3e8e41}
        .button:active {
            background-color: #3e8e41;
            box-shadow: 0 5px #666;
            transform: translateY(4px);
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='container'><h1>Type in Random words!</h1></div>", unsafe_allow_html=True)
    text_input = st.text_area("", key="question_box", placeholder="Type your question here...", height=150, max_chars=500)

    if st.button("Generate Answer", key="generate_button"):
        if text_input:
            # Generate text with the language model
            res = generator(text_input, max_length=70, num_return_sequences=5)

            # Initialize an HTML string for display
            html_content = "<div class='results'>"

            # Iterate over each result and add to the HTML string
            for i, item in enumerate(res):
                generated_text = item['generated_text'].replace('\n', '<br>')  # Replace newlines with HTML line breaks
                html_content += f"<div class='result-item'><b>Result {i+1}:</b> {generated_text}</div>"

            html_content += "</div>"

            # Styling for the results
            st.markdown("""
            <style>
                .results {
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                }
                .result-item {
                    background-color: #f0f2f6;
                    border-radius: 10px;
                    padding: 10px;
                    border: 1px solid #ccc;
                }
            </style>
            """, unsafe_allow_html=True)

            st.markdown(html_content, unsafe_allow_html=True)
        else:
            st.warning("Please enter some text first.")

if __name__ == "__main__":
    main()
