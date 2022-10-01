# EmojifyDoc

**EmojifyDoc** is The Chicken Coop's project for HackMIT 2022. 

Want to spice up your PDFs? EmojifyDoc is the perfect solution for you! 

Input Document: 
*insert image here*

Output Document:
*insert image here*


___


### How EmojifyDoc works: 

We use *pdf2image* to split the input PDF into individual JPG images. We then run Pytesseract (OCR) on each image to get words along with their bounding boxes. Using a dictionary mapping emojis to words (manually curated by a team member), if there is a word on the image that can be expressed as an emoji, we white out that bounding box and place a relevant emoji there instead. 


Enjoy!
