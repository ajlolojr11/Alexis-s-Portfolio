# Problem Set 8
# Program: CS50 Shirtificate
# Alexis Varas Ortiz
# Description: Create a custom shirtificate with the user's name

from fpdf import FPDF, Align

class PDF(FPDF):
    #Initiates instance of class
    def __init__(self, name):
        super().__init__(orientation="P", format="A4") #sets pdf format
        self._name = name


    def header(self):
        self.set_font("Helvetica", "B", 36) #Sets font style for header
        self.set_xy(0,20)
        self.cell(60, None, "CS50 Shirtificate", align = Align.C, center=True) #Adds text to header

    #Separate shirt from header
    def shirt(self):
        self.add_page()
        self.set_font("Helvetica", "", 24) #Sets font style for text inside the shirt
        self.set_text_color(255, 255, 255) #set text color to white
        self.image("shirtificate.png", x=Align.C, y=50, w=200 , keep_aspect_ratio=True) #adds image
        self.set_xy(0,110) #Adjust to middle of the shirt
        self.cell(60, None, f"{self._name} took CS50", align = Align.C, center=True) #Adds text to shirt

    @property
    def name(self):
        return self._name


def main():
    pdf = PDF(input("Name: "))
    pdf.shirt()
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
