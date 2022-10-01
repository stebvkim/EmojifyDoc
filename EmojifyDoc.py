# to be implemented.
import os
from pdf2image import convert_from_path

def convert_and_save_as_image(pdf_pathname: str) -> list[str]:
    ''' Takes an input PDF and creates a new folder containing the individual pages as JPG files. '''

    assert os.path.exists(pdf_pathname), "File does not exist."
    PDF_HANDLE_INDEX = -3
    assert pdf_pathname[PDF_HANDLE_INDEX:].lower() == 'pdf', "File is not a PDF."

    individual_images = convert_from_path(pdf_pathname)

    path = os.path.join(os.getcwd(), 'test_file_storage')
    if not os.path.isdir(path):
        os.mkdir(path)

    im_paths = []

    for ix, im in enumerate(individual_images):
        im_path = os.path.join(path, f'page_{ix}.jpg')
        im.save(im_path)
        im_paths.append(im_path)

    return im_paths

def get_words_and_bounding_boxes(image_path: str):
    pass

# print(convert_and_save_as_image('test_file_storage'))
# print(convert_and_save_as_image('test_file_storage\page_0.jpg'))