import streamlit as st

st.set_page_config(page_title="Strealmlit Demo")
st.title("Streamlit Demo")

color_text = st.text_input("あなたの好きな色は何ですか？")
go_button = st.button("Go", type="primary")

if go_button:
    st.write(f"私の好きな色も{color_text}です！")