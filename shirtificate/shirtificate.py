from fpdf import FPDF


def main():
    # Get user input
    name = input("Name: ")
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    pdf.add_page()
    pdf.set_font("Arial", "B", size=24)

    pdf.cell(0, 20, "CS50 Shirtificate", align="C")
    pdf.image("shirtificate.png", x=10, y=50, w=190)

    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Arial", "B", 20)
    pdf.set_xy(0, 120)
    pdf.cell(0, 10, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
