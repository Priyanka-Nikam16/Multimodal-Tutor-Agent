from pdf2image import convert_from_path
import uuid

def pdf_to_images(pdf_path):
    pages=convert_from_path(pdf_path)
    image_paths=[]
    for page in pages:
        image_path=f"uploads/{uuid.uuid4()}.jpg"
        page.save(image_path,"JPEG")
        image_paths.append(image_path)
    return image_paths