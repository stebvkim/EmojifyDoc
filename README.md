# EmojifyDoc

**EmojifyDoc** is The Chicken Coop's project for HackMIT 2022. 

Want to spice up your PDFs? EmojifyDoc is the perfect solution for you! 

Input Document: 
*insert image here*

Output Document:
*insert image here*


___


### How EmojifyDoc works: 

We use *pdf2image* to split the input PDF into individual JPG images. We then run Pytesseract (OCR) on each image to get words along with their bounding boxes. These words are then converted to emojis if an appropriate emoji can be found. When a relevant emoji is being found, we first try the emoji_translate package to see if it already has a matching emoji. Then, we check a dictionary of pre-determined pairings that were created by hand. Finally, we use GloVe word embeddings to get similar words and try to use the emoji_translate package again on them. If there is a word on the image that can be expressed as an emoji, we white out that bounding box and place a relevant emoji there instead. 


Enjoy!
