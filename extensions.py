def main():
   x = input("File name: ")
   if x_gif(x):
    print("image/gif")
   elif x_jpg(x):
       print("image/jpg")
   elif x_jpeg(x):
       print("image/jpeg")
   elif x_png(x):
       print("image/png")
   elif x_pdf(x):
       print("application/pdf")
   elif x_PDF(x):
       print("application/pdf")
       
   elif x_txt(x):
       print("text/plain")
   elif x_zip(x):
       print("application/zip")
   else:
       print("application/octet-stream")


def x_gif(n):
    n =  n.endswith(".gif")
    return n
def x_jpg(n):
    n =  n.endswith(".jpg")
    return n

def x_jpeg(n):
    n =  n.endswith(".jpeg")
    return n
def x_png(n):
    n =  n.endswith(".png")
    return n
def x_pdf(n):
    n =  n.endswith(".pdf")
    return n
def x_PDF(n):
    n =  n.endswith(".PDF")
    return n
def x_txt(n):
    n =  n.endswith(".txt")
    return n
def x_zip(n):
    n =  n.endswith(".zip")
    return n




main()