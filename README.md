# EmojifyDoc

**EmojifyDoc** is The Chicken Coop's project for HackMIT 2022. 

Want to spice 🌶️ up your PDFs? EmojifyDoc is the perfect 💯 solution for you! 

Input Document: 

![Input Document](assets/sample_fable_image.jpg?raw=true "Title")

Output Document: 😎

![Output Document](assets/sample_fable_emojified_image.jpg?raw=true "Title")

Note that this sample output used GloVe, which means it contains more emojis (yay!) but also more mistakes (oh no).

___

Instructions:
python EmojifyDoc.py --path path_to_pdf (--glove True/False, optional and default False)
- will need to install the necessary packages (and change the pytesseract path in the code)


**Run create_glove_file.py first to download everything necessary to utilize GloVe. Otherwise, the default emoji suggestion is used. Note that using GloVe may drastically increase the runtime for less powerful computers.**

### How EmojifyDoc works: 

We use pdf2image to split the input PDF into individual JPG images. We then run Pytesseract (OCR) on each image to get words along with their bounding boxes. These words are then converted to emojis if an appropriate emoji can be found. In the process of finding a relevant emoji, we first try the emoji_translate package to see if it already has a matching emoji. Then, we check a dictionary of pre-determined pairings that we curated by hand. Finally, we use GloVe word embeddings to get similar words and try to use the emoji_translate package again on them. If there is a word on the image that can be expressed as an emoji, we white out that bounding box and place a relevant emoji there instead. 

Note that some emojis show up as boxes. That is funky. Also note that when a word can be represented through multiple emojis, EmojifyDoc will randomly select one. This is not perfect, nor did we intend it to be. In a way, it adds to the fun 😀.

Enjoy!!
