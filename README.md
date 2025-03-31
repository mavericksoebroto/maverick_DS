# Data Structure

# 113-2 師大資料結構
- 授課教師：蔡芸琤老師
- 姓名：陳生好
- 系級：科技系116

## 作業繳交區
### HW1 Gemini Python API 實作
(1) 作業程式原始碼 GitHub 連結
https://github.com/mavericksoebroto/maverick_DS_Homework_1.git

### HW2 DRai
All files related to this homework are located inside the **`DS Homework 2`** folder:

(1) `DRai.py`: A Python script that reads `bitcoin_news.csv`, evaluates each row based on criteria, and outputs the results.

(2) `bitcoin_news.csv`: 120 rows of fake Bitcoin news data that gets processed by `DRai.py`.

(3) `output.csv`: The final processed CSV file after running the Python script equipped with evaluation results.
  
### HW3 利用 Playwright 控制瀏覽器
Homework Objective:

This project uses **Playwright** to automate a browser session on Moodle, logging in and extracting assignment deadlines from the assignments page.

****

All files related to this homework are located inside the **`DS Homework 3`** folder:

(1) `moodle_deadlines.py`: 

  The main script that:
- Logs into Moodle using Playwright.
- Navigates to the assignments page.
- Extracts assignment deadlines and saves them in `moodle_deadlines.csv`.
- Takes screenshots for verification.

(2) `debug_deadlines.png`: A screenshot of the Moodle assignments page after the script navigates to it.

(3) `code_output.png`: A screenshot of the terminal output showing the script’s execution logs.

****

Expected Output:
- If **there ARE assignments**, the script generates `moodle_deadlines.csv`, listing each assignment's title and deadline.
- If **there are NO assignments**, the script prints:

  ```
  🔗 Logging into Moodle...

  ✅ Login successful!

  📌 Fetching assignment deadlines...

  ⚠️ No assignments found!

  📌 Process complete!
  ```
  and does **NOT** create `moodle_deadlines.csv`.

****

| 注意： At the time of testing, there were NO assignments available. Hence, the expected output file `moodle_deadlines.csv` was NOT generated because no data was available to save. |
|:--:|

### HW4

### HW5

## 期末專題繳交區
