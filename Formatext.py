import streamlit as st
import re
import streamlit.components.v1 as components

st.set_page_config(page_title="List to Text Formatter", page_icon="📝", layout="centered")

st.title("📝 List to Text Formatter")
st.write("Paste your list below (one item per line). The app will merge them into a single line separated by ` | `.")

# Input area
user_input = st.text_area("Your list:", height=200, placeholder="1. First item\n2. Second item\n3. Third item")

if user_input.strip():
    # Clean numbering/bullets
    lines = [re.sub(r"^[\d\.\-\)\s\t]+", "", line).strip()
             for line in user_input.strip().split("\n")
             if line.strip()]

    # Join into a single line
    formatted_text = " | ".join(lines)

    st.subheader("Formatted Output")
    st.code(formatted_text, language="text")

    # HTML + JS button (runs inside iframe so it works reliably)
    components.html(
        f"""
        <button id="copyButton" style="
            background-color:#4CAF50;
            color:white;
            padding:8px 16px;
            font-size:16px;
            border:none;
            border-radius:5px;
            cursor:pointer;
        ">📋 Copy to Clipboard</button>

        <p id="status" style="color:green;font-weight:bold;"></p>

        <script>
        const btn = document.getElementById('copyButton');
        const status = document.getElementById('status');
        btn.addEventListener('click', () => {{
            navigator.clipboard.writeText(`{formatted_text}`).then(() => {{
                status.textContent = '✅ Copied!';
                setTimeout(() => status.textContent = '', 2000);
            }});
        }});
        </script>
        """,
        height=80,
    )
