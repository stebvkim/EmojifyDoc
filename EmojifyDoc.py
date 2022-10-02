import argparse
import os
import pytesseract as pt
from pdf2image import convert_from_path
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from pilmoji import Pilmoji
from testing_dict import emojify

PDF_HANDLE_INDEX_BACK = -3
PDF_HANDLE_INDEX_FRONT = -4

parser = argparse.ArgumentParser(description='Run EmojifyDoc.')
parser.add_argument('--path', type=str, required=True)

# Need this to make Pytesseract run on my computer. Will differ for other users.
pt.pytesseract.tesseract_cmd = r'C:\Users\steve\AppData\Local\Tesseract-OCR\tesseract.exe'

################################## Helper Functions ##################################
def pdf_to_pil_images(pdf_pathname: str) -> list:
    ''' Takes an input PDF and returns a list of PIL images. '''

    # Make sure we get valid inputs
    assert os.path.exists(pdf_pathname), "File does not exist."
    assert pdf_pathname[PDF_HANDLE_INDEX_BACK:].lower() == 'pdf', "File is not a PDF."

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

def emojify_text(img, xy: tuple, unicode: str):
    '''
    Whites out relevant text and emojifies them - assumes 
    that there is a relevant word behind xy and unicode.

    img = PIL image file -> containing document page
    xy = 4-tuple containing (x0, y0, x1, y1)
    unicode = str containing unicode for emoji
    '''
    (x0, y0, x1, y1) = xy
    area = [(x0, y0), (x1, y1)]
    emoji_location = (int((x1 + x0)/2 - (y1 - y0)/2), int(y0))    # point to center emoji 

    boundary_box = Image.new("RGB", (x1 - x0, y1 - y0), (255, 255, 255))
    img.paste(boundary_box, (x0, y0))

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', (y1 - y0))

    with Pilmoji(img) as pilmoji:
        pilmoji.text(emoji_location, unicode, (0, 0, 0), font)

def check_emojify(words_dict, img):
    '''
    Checks words in document to see if an emoji version
    exists and calls replacement function.

    words_dict = dict containing words and list of 4-tuples
    '''
    for key, val in words_dict.items():
        emojified = emojify(key)
        if (emojified):
            for v in val:
                emojify_text(img, v, emojified)
    
    return img


if __name__ == "__main__":

    args = parser.parse_args()
    input_pdf_path = args.path

    pil_images = pdf_to_pil_images(input_pdf_path)
    final_pil_images = []

    for img in pil_images:
        # final_pil_images.append(img)
        page_info = get_words_and_bounding_boxes(img)
        final_pil_images.append(check_emojify(page_info, img))

    page_one = final_pil_images[0]
    file_name = os.path.basename(input_pdf_path)

    if len(final_pil_images) > 1:
        other_pages = final_pil_images[1:]
        page_one.save(os.path.join(os.path.join(os.getcwd(), 'emojified_pdfs'), f'{file_name[:PDF_HANDLE_INDEX_FRONT]}_emojified.pdf'), save_all=True, append_images=other_pages)

    else:
        page_one.save(os.path.join(os.path.join(os.getcwd(), 'emojified_pdfs'), f'{file_name[:PDF_HANDLE_INDEX_FRONT]}_emojified.pdf'))