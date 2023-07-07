# Edit-PDF-and-Merge-two-PDFs-Into-one

## Description: - 

***
* Three Approaches are mentioned to write string and image on PDFs:
	* Approach 1: Uses packages like reportlab, PyPDF4(or PyPDF2) and io to write and merge. Creates one pdf containing strings and images and merges with original pdf and stores it. And creates merger object and adds pdfs and save it at last.
	* Approach 2: Uses packages same as Approach 1. Only difference is that strings and images are written on a blank pdf and then it is merged.
	* Approach 3: Uses packages like fpdf, Pypdf4 and maps strings, images coordinate wise and merges with original pdf

* Two approaches to merge PDFs:
	* Approach 1: With Pypdf4
	* Approach 2: With pikepdf

* Whole thing is implemented on the class basis.
* If you are looking for the best way to write pdf forms and have so many pages then you should use Approach 3 creating pdf with sting, image etc with Approach 2 merging PDF as per my opinion, but you can always try others out

---
## Reference: -
1. https://stackoverflow.com/questions/62261355/how-to-add-watermark-in-all-pages-of-pdf-files-with-python
2. https://www.geeksforgeeks.org/add-watermark-to-pdf-using-pypdf4-in-python/