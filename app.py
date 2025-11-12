import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# Configure API Key
genai.configure(api_key="AIzaSyBTAV13Brz4kzh_uaEeL2mgAUeuQ2jqnZo")

# Use the latest Gemini model
vision_model = genai.GenerativeModel("gemini-2.0-flash")

# Disease Remedies Dictionary
disease_remedies = {
    "Powdery Mildew": "Use sulfur-based fungicides. Ensure good air circulation and avoid overhead watering.",
    "Rust": "Apply copper-based fungicides. Remove infected leaves and improve plant spacing.",
    "Leaf Blight": "Use fungicides containing chlorothalonil. Remove affected leaves and avoid water splashing.",
    "Bacterial Spot": "Use copper sprays and resistant plant varieties. Avoid wet foliage.",
    "Healthy Leaf": "No disease detected! Keep the plant well-watered and nourished."
}

# Streamlit UI
st.title("🌿 Leaf Disease Detection")

# File Upload
uploaded_file = st.file_uploader("Upload a leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Leaf", use_column_width=True)

    # Convert image to bytes
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_data = image_bytes.getvalue()

    # Prepare request
    image_dict = {"mime_type": "image/png", "data": image_data}

    # Send to Gemini model
    response = vision_model.generate_content([image_dict, "Identify the leaf disease and provide a short name."])

    # Get model output
    detected_disease = response.text.strip()

    # Display results
    st.subheader("🩺 Detected Disease:")
    st.write(detected_disease)

    # Provide Remedies
    remedy = disease_remedies.get(detected_disease, "Consult an agricultural expert for further advice.")
    st.subheader("💡 Suggested Remedy:")
    st.write(remedy)
