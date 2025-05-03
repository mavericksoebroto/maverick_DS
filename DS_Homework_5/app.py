import gradio as gr
from report_generator import csv_to_pdf, csv_to_chart

def process_csv(file):
    pdf_path = csv_to_pdf(file.name)
    chart_path = csv_to_chart(file.name)
    return chart_path, pdf_path

with gr.Blocks() as demo:
    gr.Markdown("## 📊 Crypto CSV Analyzer: PDF + Chart Generator")

    file_input = gr.File(label="上傳你的 Crypto CSV", file_types=[".csv"])
    image_output = gr.Image(label="📈 價格趨勢圖")
    pdf_output = gr.File(label="📄 下載 PDF 報告")

    generate_button = gr.Button("生成報告")
    generate_button.click(fn=process_csv, inputs=file_input, outputs=[image_output, pdf_output])

demo.launch()
