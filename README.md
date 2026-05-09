# 🧸 Magic Storybook Generator (ISOM5240 Individual Assignment)

**Author:** [Your Name]  
**Student ID:** [Your Student ID]  
**Course:** ISOM5240  

## 📖 Project Overview
The **Magic Storybook Generator** is a Python-based web application designed for children aged 3 to 10. Users can upload an image, and the application will use artificial intelligence to look at the picture, write a magical 50-100 word story about it, and read the story out loud. 

This project demonstrates the practical application of Hugging Face Transformers pipelines and interactive UI design using Streamlit, fulfilling the requirements for the ISOM5240 Individual Assignment.

## ✨ Features
* **Image Processing & Captioning:** Utilizes a pre-trained Vision-Encoder-Decoder model (`Salesforce/blip-image-captioning-base`) to extract descriptive details from uploaded images.
* **Story Generation:** Leverages a text-generation model (`google/flan-t5-base`) to creatively expand the image caption into an engaging, age-appropriate narrative.
* **Text-to-Speech (TTS):** Converts the generated text into an audio file using the `gTTS` library for an interactive, accessible user experience.
* **Cloud Deployment:** Fully containerized and deployed on Streamlit Cloud for seamless online access.

## 🛠️ Technology Stack
* **Language:** Python 3.x
* **Framework:** Streamlit
* **Machine Learning:** Hugging Face `transformers`, `torch`
* **Audio Processing:** `gTTS` (Google Text-to-Speech)
* **Image Processing:** `Pillow` (PIL)

## 🚀 How to Run Locally
If you want to run this application on your local machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/kids-story-generator.git](https://github.com/YourUsername/kids-story-generator.git)
   cd kids-story-generator
