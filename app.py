import os

import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load API key dari file .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY tidak ditemukan.")

client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """
Anda adalah AI Akuntansi.
Tugas:
1) Jelaskan konsep akuntansi
2) Beri contoh numerik
3) Jelaskan langkah perhitungan
"""

def ask_ai(question):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]
    chat = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.2,
    )
    return chat.choices[0].message.content

def main():
    st.title("AI Akuntansi")
    st.write("Tanyakan apapun tentang akuntansi.")
    question = st.text_area("Masukkan pertanyaan Anda:")
    if st.button("Kirim"):
        answer = ask_ai(question)
        st.write(answer)

if __name__ == "__main__":
    main()
