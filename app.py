import streamlit as st
from transformers import pipeline
from PIL import Image
from gtts import gTTS
import tempfile
import os

# --- Page Configuration ---
st.set_page_config(page_title="Kids Story Generator", page_icon="🧸", layout="centered")


# --- Model Loading Functions ---
# We use @st.cache_resource so the models only load once, saving memory and time.
@st.cache_resource
def load_caption_model():
    """Loads the Hugging Face image captioning pipeline."""
    return pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")


@st.cache_resource
def load_story_model():
    """Loads the Hugging Face text generation pipeline."""
    # Using flan-t5-base as it is excellent at following instructions for specific audiences (like kids).
    return pipeline("image-text-to-text", model="Salesforce/blip-image-captioning-base")


# --- Application Logic Functions ---
def generate_image_caption(image, caption_pipeline):
    """Generates a caption from the uploaded image."""
    result = caption_pipeline(image)
    return result[0]['generated_text']


def generate_kids_story(caption, story_pipeline):
    """Expands the caption into a 50-100 word story for 3-10 year olds."""
    prompt = f"Write a fun, imaginative story for a 5-year-old child about this: {caption}. Keep it between 50 and 100 words."

    # max_new_tokens is constrained to ensure the story length fits the 50-100 word requirement
    result = story_pipeline(prompt, max_new_tokens=150, do_sample=True, temperature=0.7)
    return result[0]['generated_text']


def text_to_audio(story_text):
    """Converts the generated story text into an audio file using gTTS."""
    tts = gTTS(text=story_text, lang='en', slow=False)

    # Save to a temporary file so Streamlit can read and play it
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    return temp_file.name


# --- Main Streamlit UI ---
def main():
    st.title("🧸 Magic Storybook Generator")
    st.write("Upload a picture, and I will write a magical story about it!")

    # Display loading spinners while models initialize
    with st.spinner("Loading AI Models... Please wait."):
        caption_model = load_caption_model()
        story_model = load_story_model()

    # File uploader for the user to provide an image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # 1. Display the uploaded image
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption="Your Uploaded Image", use_column_width=True)

        if st.button("✨ Generate My Story!"):
            # 2. Image Processing & Captioning
            with st.spinner("Looking at the picture..."):
                caption = generate_image_caption(image, caption_model)
                st.info(f"**What I see:** {caption.capitalize()}")

            # 3. Story Generation
            with st.spinner("Writing a magical story..."):
                story = generate_kids_story(caption, story_model)
                st.success("**Your Story:**")
                st.write(story)

            # 4. Text-to-Speech Conversion
            with st.spinner("Recording the story..."):
                audio_file_path = text_to_audio(story)
                st.audio(audio_file_path, format="audio/mp3")

                # Clean up the temporary audio file after loading it into the UI
                os.remove(audio_file_path)


if __name__ == "__main__":
    main()
