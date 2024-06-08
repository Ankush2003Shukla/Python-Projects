import PyPDF2

a = ["sample.pdf","dummy.pdf","sample2.pdf"] #putting pdfs in a list

b = PyPDF2.PdfMerger() #creating a new merged pdf

for i in a:
    c = open(i,'rb') #opening the pdf
    d = PyPDF2.PdfReader(c) #reading the pdf
    b.append(d) #appending the pdf
c.close() #file closed
b.write("Result.pdf") #generating new merged pdf file with name Result.pdf