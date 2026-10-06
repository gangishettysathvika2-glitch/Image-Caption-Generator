import streamlit as st 
import ollama 
import base64 
 
 
# ------------------------------- 
# PAGE SETTINGS 
# ------------------------------- 
 
st.set_page_config( 
    page_title="AI Image Caption Generator", 
    page_icon="🖼️", 
    layout="centered" 
) 
 
 
# ------------------------------- 
# TITLE 
# ------------------------------- 
 
st.title("🖼️ AI Image Caption Generator") 
 
st.write( 
    "Upload an image and Ollama AI will generate a description." 
) 
 
 
# ------------------------------- 
# IMAGE UPLOAD 
# ------------------------------- 
 
uploaded_file = st.file_uploader( 
    "Choose an image", 
    type=["jpg", "jpeg", "png"] 
) 
 
 
# ------------------------------- 
# GENERATE CAPTION 
# ------------------------------- 
 
if uploaded_file is not None: 
 
    # Display image 
    st.image( 
        uploaded_file, 
        caption="Uploaded Image", 
        use_container_width=True 
    ) 
 
    # Generate button 
    if st.button("✨ Generate Caption"): 
 
        with st.spinner("🤖 AI is analyzing the image..."): 
 
            try: 
 
                # Read image 
                image_bytes = uploaded_file.read() 
 
                # Convert image to base64 
                image_base64 = base64.b64encode( 
                    image_bytes 
                ).decode("utf-8") 
 
                # Send image to Ollama 
                response = ollama.chat( 
                    model="gemma3", 
                    messages=[ 
                        { 
                            "role": "user", 
                            "content": ( 
                                "Describe this image in one " 
                                "simple and clear sentence." 
                            ), 
                            "images": [image_base64] 
                        } 
                    ] 
                ) 
 
                # Get caption 
                caption = response["message"]["content"] 
 
                # Display result 
                st.success("Caption generated!") 
 
                st.subheader("🤖 Generated Caption") 
 
                st.info(caption) 
 
            except Exception as e: 
 
                st.error( 
                    "Something went wrong." 
                ) 
 
                st.write(e) 
 
 
# ------------------------------- 
# INFORMATION 
# ------------------------------- 
 
else: 
 
    st.info( 
        "👆 Upload an image to generate an AI caption." 
    ) 
 
 
# ------------------------------- 
# FOOTER 
# ------------------------------- 
 
st.markdown("---") 
 
st.caption( 
    "Built using Streamlit + Ollama" 
)