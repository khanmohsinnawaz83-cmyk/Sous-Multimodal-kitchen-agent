import streamlit as st
from agents import analyze_kitchen

st.set_page_config(
    page_title="Sous Kitchen Agent",
    page_icon="🍳"
)

st.title("🍳 Sous — Multimodal Kitchen Agent")

st.write(
    "Give Sous your ingredients using text, audio or a fridge image."
)

text = st.text_area(
    "What would you like to cook?"
)

image = st.file_uploader(
    "📷 Upload fridge image",
    type=["jpg", "jpeg", "png"]
)

audio = st.file_uploader(
    "🎤 Upload voice instruction",
    type=["mp3", "wav", "m4a"]
)

if st.button("🚀 Ask Sous"):

    image_path = None
    audio_path = None

    if image:
        image_path = "uploaded_image.jpg"

        with open(image_path, "wb") as f:
            f.write(image.getbuffer())

    if audio:
        audio_path = "uploaded_audio.wav"

        with open(audio_path, "wb") as f:
            f.write(audio.getbuffer())

    with st.spinner("Sous is thinking..."):

        result = analyze_kitchen(
            text,
            image_path,
            audio_path
        )

    st.subheader("👨‍🍳 Sous's Recommendation")

    st.write(result)