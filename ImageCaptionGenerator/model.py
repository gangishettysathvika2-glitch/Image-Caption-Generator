import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration


# --------------------------------------------------
# MODEL CONFIGURATION
# --------------------------------------------------

MODEL_NAME = "Salesforce/blip-image-captioning-base"

# Use GPU if available, otherwise CPU
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


# --------------------------------------------------
# LOAD AI MODEL
# --------------------------------------------------

def load_model():
    """
    Loads the BLIP image captioning model
    and its processor.
    """

    print("Loading AI model...")

    processor = BlipProcessor.from_pretrained(
        MODEL_NAME
    )

    model = BlipForConditionalGeneration.from_pretrained(
        MODEL_NAME
    )

    # Move model to CPU or GPU
    model.to(DEVICE)

    print(f"Model loaded successfully on {DEVICE}")

    return processor, model


# --------------------------------------------------
# GENERATE IMAGE CAPTION
# --------------------------------------------------

def generate_caption(image, processor, model):
    """
    Takes an image and generates an AI caption.
    """

    # Make sure image is RGB
    image = image.convert("RGB")

    # Convert image into model input
    inputs = processor(
        images=image,
        return_tensors="pt"
    )

    # Move inputs to selected device
    inputs = {
        key: value.to(DEVICE)
        for key, value in inputs.items()
    }

    # Generate caption
    with torch.no_grad():

        output = model.generate(
            **inputs,
            max_new_tokens=30,
            num_beams=5
        )

    # Convert model output into readable text
    caption = processor.decode(
        output[0],
        skip_special_tokens=True
    )

    return caption


# --------------------------------------------------
# TEST THE MODEL
# --------------------------------------------------

if __name__ == "__main__":

    print("Image Caption Generator Model")
    print("--------------------------------")
    print(f"Using device: {DEVICE}")
    print(f"Model: {MODEL_NAME}")
    print("--------------------------------")

    # Load model
    processor, model = load_model()

    print("Ready to generate captions!")