# EmojifyDoc

**EmojifyDoc** is The Chicken Coop's project for HackMIT 2022. 

Want to spice up your PDFs? EmojifyDoc is the perfect solution for you! 

Input Document: 
![Input Document](assets/sample_fable_image.jpg?raw=true "Title")

Output Document:
![Output Document](assets/sample_fable_emojified_image.jpg?raw=true "Title")


___

**Be sure to run run_glove_file.py first to utilize GloVe. Otherwise, the default emoji suggestion is used.**

### How EmojifyDoc works: 

We use *pdf2image* to split the input PDF into individual JPG images. We then run Pytesseract (OCR) on each image to get words along with their bounding boxes. These words are then converted to emojis if an appropriate emoji can be found. When a relevant emoji is being found, we first try the emoji_translate package to see if it already has a matching emoji. Then, we check a dictionary of pre-determined pairings that were created by hand. Finally, we use GloVe word embeddings to get similar words and try to use the emoji_translate package again on them. If there is a word on the image that can be expressed as an emoji, we white out that bounding box and place a relevant emoji there instead. 

Note that some emojis show up as boxes. This is likely due to something funky with Unicode. Also note that when a word can be represented through multiple emojis, EmojifyDoc will randomly select one.

Enjoy!
