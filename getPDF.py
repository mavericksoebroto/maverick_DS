import pandas as pd
from fpdf import FPDF

# File path
file_path = "output.csv"
pdf_output_path = "combined_output.pdf"

# Load CSV and clean NaNs
df = pd.read_csv(file_path)
df = df.fillna("")

# Convert float 1.0 to int 1 (and leave other values untouched)
df = df.applymap(lambda x: int(x) if isinstance(x, float) and x.is_integer() else x)

# Shorten column names
column_name_map = {
    "Sentiment Positive": "情緒正面",
    "Sentiment Negative": "情緒負面",
    "Sentiment Neutral": "情緒中立",
    "Is Market Category": "市場類別",
    "Is Regulation Category": "監管類別",
    "High Views (Above 20000)": "高瀏覽量",
    "Source CoinDesk": "CoinDesk"
}
df_display = df.copy()
df_display.columns = [column_name_map.get(col, col) for col in df.columns]

# PDF setup
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

# Add a Chinese font like NotoSansCJK (ensure it's in your working directory)
pdf.add_font("NotoSansCJK", "", "NotoSansCJK-Regular.ttc", uni=True)
pdf.set_font("NotoSansCJK", "", 10)

def draw_table(pdf, df):
    max_width = pdf.w - 2 * pdf.l_margin
    columns = df.columns.tolist()
    avg_col_width = max_width / len(columns)
    col_widths = [avg_col_width] * len(columns)
    row_height = 8

    # Header
    pdf.set_fill_color(200, 200, 200)
    pdf.set_font("NotoSansCJK", "", 10)
    for i, col in enumerate(columns):
        pdf.cell(col_widths[i], row_height, str(col), border=1, align="C", fill=True)
    pdf.ln(row_height)

    # Rows
    fill = False
    for _, row in df.iterrows():
        if pdf.get_y() > pdf.h - 2 * row_height:
            pdf.add_page()
            pdf.set_fill_color(200, 200, 200)
            for i, col in enumerate(columns):
                pdf.cell(col_widths[i], row_height, str(col), border=1, align="C", fill=True)
            pdf.ln(row_height)

        fill_color = (230, 240, 255) if fill else (255, 255, 255)
        pdf.set_fill_color(*fill_color)
        for i, item in enumerate(row):
            text = str(item)
            max_chars = int(col_widths[i] / 2.5)
            if len(text) > max_chars:
                text = text[:max_chars - 3] + "..."
            pdf.cell(col_widths[i], row_height, text, border=1, align="C", fill=True)
        pdf.ln(row_height)
        fill = not fill

draw_table(pdf, df_display)
pdf.output(pdf_output_path)
print(f"✅ PDF successfully saved as: {pdf_output_path}")
