# -*- coding: utf-8 -*-
"""Generates cv.pdf for Yougesh Kumar's portfolio."""
from fpdf import FPDF

# Theme colours
BLUE = (74, 137, 220)
DARK = (44, 62, 80)
GREY = (110, 110, 110)
LIGHT_RULE = (210, 210, 210)

NAME = "Yougesh Kumar"
TITLE = "Web Developer & AI / ML Enthusiast"

CONTACT = [
    ("Email", "katariayougesh@gmail.com", "mailto:katariayougesh@gmail.com"),
    ("Phone", "0327 7037201", None),
    ("Location", "Sukkur, Sindh, Pakistan", None),
    ("GitHub", "github.com/Yougeshkumar7", "https://github.com/Yougeshkumar7"),
    ("LinkedIn", "linkedin.com/in/yougesh-kumar-06150b318",
     "https://www.linkedin.com/in/yougesh-kumar-06150b318"),
]

SUMMARY = (
    "Software Engineering undergraduate and web developer who builds clean, responsive "
    "web applications and is actively expanding into Artificial Intelligence and Machine "
    "Learning. Comfortable across the front-end stack (HTML, CSS, JavaScript, React) and "
    "with Python for data-driven projects such as classification and fraud-detection models. "
    "Passionate about combining thoughtful design with intelligent, practical solutions."
)

EDUCATION = {
    "degree": "BS Software Engineering",
    "school": "Sukkur IBA University",
    "loc": "Sukkur, Sindh, Pakistan",
    "dates": "2024 - 2028 (expected)",
    "gpa": "CGPA: 3.53 / 4.0",
}

SKILLS = {
    "Web Development": "HTML5, CSS3, JavaScript, React, Responsive Design",
    "Programming": "Python, Java, C++",
    "AI / ML": "Machine Learning, Pandas, scikit-learn, Prompt Engineering",
    "Tools & Data": "MySQL, Git & GitHub, Figma, Command Line",
}

PROJECTS = [
    ("Chronos - Watches Store",
     "A sleek, fully responsive online watches store with a modern product showcase.",
     "HTML, CSS, JavaScript",
     "https://yougeshkumar7.github.io/CHRONOS/"),
    ("Credit Card Fraud Detection",
     "Machine learning model that detects fraudulent transactions using classification techniques.",
     "Python, Machine Learning, Pandas, scikit-learn",
     "https://github.com/Yougeshkumar7/credit_card_fraud_detection_system"),
    ("Tickora - Habit Tracker",
     "Habit-tracking app to build routines, mark daily progress and stay consistent.",
     "HTML, CSS, JavaScript",
     "https://yougeshkumar7.github.io/Tickora/"),
    ("Python Quiz System",
     "Interactive quiz application that tracks scores and gives instant feedback.",
     "Python, HTML, JavaScript",
     "https://yougeshkumar7.github.io/quiz/"),
    ("GPA Calculator",
     "Tool to calculate grade point average from course grades and credit hours in real time.",
     "HTML, CSS, JavaScript",
     "https://yougeshkumar7.github.io/GPA_Calculator/"),
]

CERTS = [
    ("Google AI Essentials", "United Latino Students Association", "Dec 2025"),
    ("Google Prompting Essentials", "Coursera", "Jul 2025"),
    ("Claude Code in Action", "Anthropic", "Mar 2026"),
    ("Claude 101", "Anthropic", "Mar 2026"),
    ("Introduction to Figma", "Simplilearn", "Dec 2024"),
]

ACHIEVEMENTS = [
    "Participated in the Sibathon Hackathon, collaborating on a team project under time constraints.",
]

LANGUAGES = "English, Sindhi, Urdu, Hindi"


class CV(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-12)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*GREY)
        self.cell(0, 8, "Yougesh Kumar  -  Curriculum Vitae", align="C")

    def section_title(self, text):
        self.ln(3)
        self.set_font("Helvetica", "B", 12.5)
        self.set_text_color(*BLUE)
        self.cell(0, 8, text.upper(), new_x="LMARGIN", new_y="NEXT")
        y = self.get_y()
        self.set_draw_color(*BLUE)
        self.set_line_width(0.5)
        self.line(self.l_margin, y, self.w - self.r_margin, y)
        self.ln(2.5)


def build():
    pdf = CV(format="A4")
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_margins(15, 14, 15)
    pdf.add_page()
    usable = pdf.w - pdf.l_margin - pdf.r_margin

    # ---- Header band ----
    pdf.set_fill_color(*DARK)
    pdf.rect(0, 0, pdf.w, 34, style="F")
    pdf.set_xy(15, 7)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 11, NAME, new_x="LMARGIN", new_y="NEXT")
    pdf.set_x(15)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(150, 195, 255)
    pdf.cell(0, 8, TITLE, new_x="LMARGIN", new_y="NEXT")

    # ---- Contact line (placed below the dark header band) ----
    pdf.set_y(40)
    pdf.set_text_color(*DARK)
    pdf.set_font("Helvetica", "", 9.5)
    line_parts = []
    for label, value, link in CONTACT:
        line_parts.append((value, link))
    # render contact as wrapping inline items separated by "  |  "
    pdf.set_x(15)
    x = pdf.get_x()
    for i, (value, link) in enumerate(line_parts):
        text = value + ("   |   " if i < len(line_parts) - 1 else "")
        w = pdf.get_string_width(text) + 0.5
        if pdf.get_x() + w > pdf.w - pdf.r_margin:
            pdf.ln(6)
            pdf.set_x(15)
        if link:
            pdf.set_text_color(*BLUE)
            pdf.cell(w, 6, text, link=link)
            pdf.set_text_color(*DARK)
        else:
            pdf.cell(w, 6, text)
    pdf.ln(9)

    # ---- Summary ----
    pdf.section_title("Profile")
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.multi_cell(usable, 5.2, SUMMARY)

    # ---- Education ----
    pdf.section_title("Education")
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(*DARK)
    pdf.cell(usable - 35, 6, EDUCATION["degree"])
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(*GREY)
    pdf.cell(35, 6, EDUCATION["dates"], align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(*BLUE)
    pdf.cell(0, 5.5, EDUCATION["school"] + " - " + EDUCATION["loc"],
             new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(60, 60, 60)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.cell(0, 5.5, EDUCATION["gpa"], new_x="LMARGIN", new_y="NEXT")

    # ---- Skills ----
    pdf.section_title("Technical Skills")
    for cat, items in SKILLS.items():
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(*DARK)
        pdf.cell(38, 5.8, cat + ":")
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(60, 60, 60)
        pdf.multi_cell(usable - 38, 5.8, items, new_x="LMARGIN", new_y="NEXT")

    # ---- Projects ----
    pdf.section_title("Projects")
    for name, desc, tech, link in PROJECTS:
        pdf.set_font("Helvetica", "B", 10.5)
        pdf.set_text_color(*DARK)
        pdf.cell(0, 5.8, name, new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 9.8)
        pdf.set_text_color(60, 60, 60)
        pdf.multi_cell(usable, 5, desc, new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "I", 9)
        pdf.set_text_color(*GREY)
        pdf.cell(pdf.get_string_width("Tech: " + tech) + 2, 5, "Tech: " + tech)
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(*BLUE)
        pdf.cell(0, 5, "   " + link, link=link, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(1.5)

    # ---- Certifications ----
    pdf.section_title("Licenses & Certifications")
    for name, issuer, date in CERTS:
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(*DARK)
        nm_w = pdf.get_string_width(name) + 2
        pdf.cell(nm_w, 5.8, name)
        pdf.set_font("Helvetica", "", 9.5)
        pdf.set_text_color(60, 60, 60)
        pdf.cell(usable - nm_w - 22, 5.8, " - " + issuer)
        pdf.set_text_color(*GREY)
        pdf.cell(22, 5.8, date, align="R", new_x="LMARGIN", new_y="NEXT")

    # ---- Achievements ----
    pdf.section_title("Achievements")
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    for a in ACHIEVEMENTS:
        pdf.cell(5, 5.2, "-")
        pdf.multi_cell(usable - 5, 5.2, a, new_x="LMARGIN", new_y="NEXT")

    # ---- Languages ----
    pdf.section_title("Languages")
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(60, 60, 60)
    pdf.cell(0, 5.5, LANGUAGES, new_x="LMARGIN", new_y="NEXT")

    pdf.output("cv.pdf")
    print("cv.pdf generated, pages:", pdf.page_no())


if __name__ == "__main__":
    build()
