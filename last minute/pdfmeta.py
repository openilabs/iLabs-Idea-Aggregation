from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdftypes import resolve1
from xmp import xmp_to_dict
def do(filename=''):
	fp = open(filename, 'rb')
	parser = PDFParser(fp)
	doc = PDFDocument(parser)
	parser.set_document(doc)
#	doc.set_parser(parser)
#	doc.initialize()

	print doc.info        # The "Info" metadata

	if 'Metadata' in doc.catalog:
	    metadata = resolve1(doc.catalog['Metadata']).get_data()
	    print metadata  # The raw XMP metadata
	    print xmp_to_dict(metadata)
	return doc,doc.info[0]