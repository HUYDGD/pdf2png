from pdf2image import convert_from_path
import os

def pdf_to_png(pdf_path):
    output_folder = os.path.dirname(pdf_path)
    os.makedirs(output_folder, exist_ok=True)

    images = convert_from_path(pdf_path)

    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i + 1}.png")
        image.save(image_path, "PNG")
        print(f"Page {i + 1} saved as {image_path}")

if __name__ == "__main__":
    # Prompt the user to enter the input PDF file path
    pdf_file = input("Enter the path of the PDF file: ")

    # Check if the provided file exists
    if not os.path.isfile(pdf_file):
        print("Error: The specified file does not exist.")
    else:
        pdf_to_png(pdf_file)
