from openai import OpenAI
from dotenv import load_dotenv
from langsmith import traceable
import os
import base64

load_dotenv()

client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

VISION_MODEL="gpt-4o"

def encode_image(image_path):
    with open(image_path,"rb" ) as image_file:
        encoded_string=base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

@traceable(name="Multimodal Tutor Agent")
def analyze_image(image_path):
    base64_image=encode_image(image_path) # Encode the image to base64 format

    response=client.chat.completions.create(
        model=VISION_MODEL,
        messages=[
            {
                "role":"user",
                "content":[
                    {
                        "type":"text",
                        "text":"""
                    Analyze the following content carefully and perform all the following tasks:
                    1. Explain in 1 liner simple sentence what is in the image
                    2. Generate summary notes
                    3. Genertae 2 questions that can be asked from the content in the image
                    4. Mention important concepts and explain  i simple terms
                    5. Generate a mid map of the content in the image

                    Format the response properly.
                    """

                    },
                    {
                        "type": "image_url",
                        "image_url":{
                            "url":f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }


        ],temperature=0.3,
        max_tokens=2000
    )
    return response.choices[0].message.content
