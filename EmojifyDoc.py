# to be implemented.
import os
import pytesseract as pt
from pdf2image import convert_from_path
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from pilmoji import Pilmoji

# Need this to make Pytesseract run on my computer. Will differ for other users.
pt.pytesseract.tesseract_cmd = r'C:\Users\steve\AppData\Local\Tesseract-OCR\tesseract.exe'

################################## Helper Functions ##################################
def pdf_to_pil_images(pdf_pathname: str) -> list:
    ''' Takes an input PDF and returns a list of PIL images. '''

    # Make sure we get valid inputs
    assert os.path.exists(pdf_pathname), "File does not exist."
    PDF_HANDLE_INDEX = -3
    assert pdf_pathname[PDF_HANDLE_INDEX:].lower() == 'pdf', "File is not a PDF."

    individual_images = convert_from_path(pdf_pathname)
    im_paths = []
    for path in individual_images:
        im_paths.append(path)

    return im_paths

def get_words_and_bounding_boxes(pil_image) -> dict:
    ''' Takes a PIL image and returns a dict mapping each word to a list of tuples where that word appears. '''
    # width, height = pil_image.size
    # print(width, height)

    # Keys: 'level', 'page_num', 'block_num', 'par_num', 'line_num', 'word_num', 'left', 'top', 'width', 'height', 'conf', 'text'
    img_dict = pt.image_to_data(pil_image, output_type = pt.Output.DICT)
    formatted_words = {}
    for ix, word in enumerate(img_dict['text']):
        if word:
            x1 = img_dict['left'][ix]
            y1 = img_dict['top'][ix]
            x2 = img_dict['left'][ix] + img_dict['width'][ix]
            y2 = img_dict['top'][ix] + img_dict['height'][ix]
            if word in formatted_words:
                formatted_words[word].append((x1, y1, x2, y2))
            else:
                formatted_words[word] = [(x1, y1, x2, y2)]

    return formatted_words

if __name__ == "__main__":
    pass


'''
Input: PDF
pdf_to_pil_images -> list of PIL images

for img in PIL_images: 
    img's words and bounding boxes from get_words_and_bounding_boxes
    for word in that output:
        if word.has_emoji:
            for bounding box in output[word]:
                white out bounding box
                pilmoji insert emoji

# the pil images should be directly modified by now?

im_1.save(... from https://datatofish.com/images-to-pdf-python/) # save back to pdf

web app?

'''

# print(convert_and_save_as_image('test_file_storage'))
# print(convert_and_save_as_image('test_file_storage\page_0.jpg'))

# sample code for ending: convert all pil images back to pdf
images = pdf_to_pil_images('ps1.pdf')
print(images)

im1 = images[0]
image_list = images[1:]

print(im1)
print(image_list)

im1.save(os.path.join(os.getcwd(), "test_pdf.pdf"), save_all=True, append_images=image_list)

# for im in images:
#     print(get_words_and_bounding_boxes(im))
#     break