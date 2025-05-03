import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
import os

def csv_to_pdf(csv_file_path):
    df = pd.read_csv(csv_file_path)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    col_width = pdf.w / (len(df.columns) + 1)

    for col in df.columns:
        pdf.cell(col_width, 10, col, border=1)
    pdf.ln()

    for _, row in df.iterrows():
        for item in row:
            pdf.cell(col_width, 10, str(item), border=1)
        pdf.ln()

    pdf_path = "report.pdf"
    pdf.output(pdf_path)
    return pdf_path

def csv_to_chart(csv_path):
    df = pd.read_csv(csv_path)

    # Try to guess time and price columns
    time_col = next((col for col in df.columns if 'time' in col.lower() or 'date' in col.lower()), None)
    price_col = next((col for col in df.columns if 'price' in col.lower() or 'close' in col.lower()), None)

    if not time_col or not price_col:
        raise ValueError("CSV must contain a time/date column and a price/close column.")

    df[time_col] = pd.to_datetime(df[time_col], errors='coerce')
    df = df.dropna(subset=[time_col, price_col])

    plt.figure(figsize=(10, 4))
    plt.plot(df[time_col], df[price_col], color='blue')
    plt.title("Crypto Price Over Time")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.grid(True)

    chart_path = "chart.png"
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    return chart_path
