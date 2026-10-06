import streamlit as st
import ollama
import base64
import json
from datetime import datetime


# ==========================================================
# PAGE SETTINGS
# ==========================================================

st.set_page_config(
    page_title="AI Image Caption Generator",
    page_icon="🖼️",
    layout="wide"
)


# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
}

.result-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #f3f6fa;
    margin-top: 10px;
    margin-bottom: 15px;
}

.feature-box {
    padding: 15px;
    border-radius: 12px;
    background-color: #eef5ff;
    margin-bottom: 10px;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)


# ==========================================================
# TITLE
# ==========================================================

st.markdown(
    '<div class="main-title">🖼️ AI Image Caption Generator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Transform images into meaningful AI-generated descriptions'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.header("⚙️ Project Settings")

    st.write("### 🤖 AI Model")

    model_name = st.text_input(
        "Ollama Model",
        value="gemma3"
    )

    st.markdown("---")

    st.header("📌 Project Features")

    st.write("✅ Image Caption")
    st.write("✅ Detailed Description")
    st.write("✅ Object Detection")
    st.write("✅ Keyword Extraction")
    st.write("✅ Mood Analysis")
    st.write("✅ Scene Detection")
    st.write("✅ Social Media Caption")
    st.write("✅ Download Report")
    st.write("✅ Caption History")

    st.markdown("---")

    st.info(
        "This project uses Ollama Vision AI "
        "to understand images and generate "
        "useful textual information."
    )


# ==========================================================
# SESSION STATE
# ==========================================================

if "history" not in st.session_state:
    st.session_state.history = []


# ==========================================================
# IMAGE UPLOAD
# ==========================================================

uploaded_file = st.file_uploader(
    "📤 Upload your image",
    type=["jpg", "jpeg", "png"],
    help="Upload JPG, JPEG or PNG images"
)


# ==========================================================
# FUNCTION: SEND IMAGE TO OLLAMA
# ==========================================================

def analyze_image(image_base64, prompt):

    response = ollama.chat(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt,
                "images": [image_base64]
            }
        ]
    )

    return response["message"]["content"].strip()


# ==========================================================
# IMAGE PROCESSING
# ==========================================================

if uploaded_file is not None:

    # Read image
    image_bytes = uploaded_file.getvalue()

    # Convert to base64
    image_base64 = base64.b64encode(
        image_bytes
    ).decode("utf-8")


    # ======================================================
    # IMAGE INFORMATION
    # ======================================================

    st.subheader("📷 Uploaded Image")

    col1, col2 = st.columns([2, 1])

    with col1:

        st.image(
            image_bytes,
            caption="Uploaded Image",
            use_container_width=True
        )

    with col2:

        st.markdown("### 📊 Image Information")

        st.write(
            "**File name:**",
            uploaded_file.name
        )

        st.write(
            "**File type:**",
            uploaded_file.type
        )

        st.write(
            "**File size:**",
            f"{len(image_bytes) / 1024:.2f} KB"
        )

        st.write(
            "**Upload time:**",
            datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        )


    st.markdown("---")


    # ======================================================
    # ANALYSIS BUTTON
    # ======================================================

    if st.button(
        "✨ Analyze Image with AI",
        use_container_width=True
    ):

        try:

            # ==================================================
            # AI CAPTION
            # ==================================================

            with st.spinner(
                "🤖 Generating image caption..."
            ):

                caption = analyze_image(
                    image_base64,
                    """
                    Generate one accurate and natural
                    caption for this image.

                    The caption should:
                    - Be grammatically correct
                    - Clearly describe the main subject
                    - Be between 10 and 25 words
                    - Avoid unnecessary information

                    Return only the caption.
                    """
                )


            # ==================================================
            # DETAILED DESCRIPTION
            # ==================================================

            with st.spinner(
                "🔍 Creating detailed description..."
            ):

                description = analyze_image(
                    image_base64,
                    """
                    Analyze this image carefully and provide
                    a detailed description.

                    Include:
                    1. Main subjects
                    2. Background
                    3. Important objects
                    4. Activities
                    5. Environment
                    6. Overall visual context

                    Use simple and clear English.
                    """
                )


            # ==================================================
            # OBJECTS
            # ==================================================

            with st.spinner(
                "🎯 Detecting objects..."
            ):

                objects = analyze_image(
                    image_base64,
                    """
                    Identify the important objects or subjects
                    visible in this image.

                    Return them as a simple comma-separated list.

                    Example:
                    person, dog, tree, car, building
                    """
                )


            # ==================================================
            # KEYWORDS
            # ==================================================

            with st.spinner(
                "🏷️ Extracting keywords..."
            ):

                keywords = analyze_image(
                    image_base64,
                    """
                    Extract 8 important keywords that describe
                    this image.

                    Return only comma-separated keywords.
                    """
                )


            # ==================================================
            # MOOD
            # ==================================================

            with st.spinner(
                "😊 Analyzing mood..."
            ):

                mood = analyze_image(
                    image_base64,
                    """
                    Identify the overall mood or feeling
                    represented by this image.

                    Give:
                    1. Mood
                    2. Short reason

                    Keep the answer concise.
                    """
                )


            # ==================================================
            # SCENE
            # ==================================================

            with st.spinner(
                "🌍 Identifying scene..."
            ):

                scene = analyze_image(
                    image_base64,
                    """
                    Identify the type of scene or environment
                    shown in this image.

                    Examples:
                    beach, classroom, city, forest,
                    restaurant, home, sports ground.

                    Give the most suitable scene.
                    """
                )


            # ==================================================
            # SOCIAL MEDIA CAPTION
            # ==================================================

            with st.spinner(
                "📱 Creating social media caption..."
            ):

                social_caption = analyze_image(
                    image_base64,
                    """
                    Create a creative social-media caption
                    for this image.

                    Make it short, attractive and natural.
                    Add 3 suitable hashtags.

                    Example:
                    Enjoying a beautiful day in nature! 🌿
                    #Nature #Beautiful #Travel
                    """
                )


            # ==================================================
            # DISPLAY RESULTS
            # ==================================================

            st.success(
                "🎉 Image analysis completed successfully!"
            )


            # ==================================================
            # CAPTION
            # ==================================================

            st.subheader("🤖 AI Generated Caption")

            st.markdown(
                f"""
                <div class="result-box">
                <h3>📝 Caption</h3>
                <p>{caption}</p>
                </div>
                """,
                unsafe_allow_html=True
            )


            # ==================================================
            # DETAILED DESCRIPTION
            # ==================================================

            st.subheader("🔍 Detailed Image Description")

            st.write(description)


            # ==================================================
            # TWO COLUMN RESULTS
            # ==================================================

            col1, col2 = st.columns(2)


            with col1:

                st.markdown(
                    '<div class="feature-box">',
                    unsafe_allow_html=True
                )

                st.subheader("🎯 Detected Objects")

                st.write(objects)

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )


            with col2:

                st.markdown(
                    '<div class="feature-box">',
                    unsafe_allow_html=True
                )

                st.subheader("🏷️ Keywords")

                st.write(keywords)

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )


            # ==================================================
            # MOOD AND SCENE
            # ==================================================

            col1, col2 = st.columns(2)


            with col1:

                st.subheader("😊 Image Mood")

                st.info(mood)


            with col2:

                st.subheader("🌍 Scene / Environment")

                st.info(scene)


            # ==================================================
            # SOCIAL MEDIA CAPTION
            # ==================================================

            st.subheader(
                "📱 Suggested Social Media Caption"
            )

            st.success(social_caption)


            # ==================================================
            # CREATE REPORT
            # ==================================================

            report = f"""
AI IMAGE CAPTION GENERATOR
===========================

File Name:
{uploaded_file.name}

Generated Date:
{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

AI Model:
{model_name}

-----------------------------------

AI GENERATED CAPTION:

{caption}

-----------------------------------

DETAILED DESCRIPTION:

{description}

-----------------------------------

DETECTED OBJECTS:

{objects}

-----------------------------------

KEYWORDS:

{keywords}

-----------------------------------

MOOD:

{mood}

-----------------------------------

SCENE:

{scene}

-----------------------------------

SOCIAL MEDIA CAPTION:

{social_caption}

-----------------------------------

Generated using Streamlit + Ollama
"""


            # ==================================================
            # DOWNLOAD REPORT
            # ==================================================

            st.subheader("📥 Download Analysis")

            st.download_button(
                label="📄 Download AI Report",
                data=report,
                file_name="image_analysis_report.txt",
                mime="text/plain",
                use_container_width=True
            )


            # ==================================================
            # SAVE HISTORY
            # ==================================================

            st.session_state.history.append(
                {
                    "time": datetime.now().strftime(
                        "%H:%M:%S"
                    ),
                    "image": uploaded_file.name,
                    "caption": caption
                }
            )


        except Exception as e:

            st.error(
                "❌ Unable to analyze the image."
            )

            st.warning(
                "Please make sure Ollama is running "
                "and the selected model supports images."
            )

            st.code(str(e))


# ==========================================================
# CAPTION HISTORY
# ==========================================================

if len(st.session_state.history) > 0:

    st.markdown("---")

    st.subheader("🕘 Caption History")

    for item in reversed(
        st.session_state.history
    ):

        with st.expander(
            f"🖼️ {item['image']} — {item['time']}"
        ):

            st.write(
                item["caption"]
            )


# ==========================================================
# HOW THE PROJECT WORKS
# ==========================================================

st.markdown("---")

st.subheader("🧠 How This AI Project Works")

st.write(
    """
    1. The user uploads an image.
    
    2. Streamlit receives the image.
    
    3. The image is converted into a format that
       Ollama can process.
    
    4. The Ollama vision model analyzes the image.
    
    5. AI generates a caption and additional information.
    
    6. The results are displayed through the Streamlit interface.
    
    7. The user can download the complete AI analysis report.
    """
)


# ==========================================================
# FOOTER
# ==========================================================

st.markdown(
    """
    <div class="footer">
    <hr>
    🖼️ AI Image Caption Generator<br>
    Built using Streamlit + Ollama<br>
    AI-Powered Image Understanding System
    </div>
    """,
    unsafe_allow_html=True
)