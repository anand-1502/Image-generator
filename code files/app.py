from openai import OpenAI
import streamlit as st
from apikey import apikey

# Image generation client
client = OpenAI(api_key=apikey)

def generate_images(image_description, num_images):
    # To give out multiple images to the user
    image_urls = []
    for i in range(num_images):
        img_response = client.images.generate(
            model="dall-e-3",
            prompt=image_description,
            size="1024x1024", 
            quality="standard",
            n=1
        )
        image_url = img_response.data[0].url
        image_urls.append(image_url) 
    return image_urls

# Start Streamlit application
st.set_page_config(page_title="Image Generation", page_icon=":camera:", layout="wide")

# Title
st.title("Image Generation Tool")

# Subheader
st.subheader("Create images with just their descriptions")

# Input boxes
img_description = st.text_input("Type in the description of the image you want to explore")
num_of_images = st.number_input("Select number of images you want to generate", min_value=1, max_value=10, value=1)

# Submit button
if st.button("Generate Images"):
    if img_description.strip() == "":
        st.error("Please enter a description for the image.")
    else:
        with st.spinner("Generating images..."):
            generated_images = generate_images(img_description, num_of_images)
        if generated_images:
            st.success(f"Generated {len(generated_images)} images!")
            for idx, img_url in enumerate(generated_images):
                # Display description above the image
                st.subheader(f"{img_description} (Image {idx + 1})")
                # Display the image
                st.image(img_url, use_container_width=True)
        else:
            st.error("No images were generated. Please try again.")



