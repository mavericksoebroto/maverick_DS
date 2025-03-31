from playwright.sync_api import sync_playwright
import os
import pandas as pd
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
MOODLE_USERNAME = os.getenv("MOODLE_USERNAME")
MOODLE_PASSWORD = os.getenv("MOODLE_PASSWORD")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Change to True for silent execution
    page = browser.new_page()

    print("🔗 Logging into Moodle...")
    page.goto("https://moodle3.ntnu.edu.tw/login/index.php")
    page.wait_for_timeout(3000)

    # Fill in credentials
    page.fill("#username", MOODLE_USERNAME)
    page.fill("#password", MOODLE_PASSWORD)
    page.click("#loginbtn")

    # Wait for login
    page.wait_for_timeout(5000)
    print("✅ Login successful!")

    # Navigate to the assignments page
    assignments_url = "https://moodle3.ntnu.edu.tw/mod/assign/index.php?id=your_course_id"
    page.goto(assignments_url)
    page.wait_for_timeout(3000)

    print("📌 Fetching assignment deadlines...")

    # Extract assignment data
    assignments = page.evaluate("""
        () => {
            let results = [];
            document.querySelectorAll("tr.assignment").forEach(row => {
                let title = row.querySelector("a")?.innerText.trim();
                let deadline = row.querySelector(".submissiondate")?.innerText.trim();
                let link = row.querySelector("a")?.href;
                if (title && deadline && link) {
                    results.push({ "作業名稱": title, "截止日期": deadline, "連結": link });
                }
            });
            return results;
        }
    """)

    # Save to CSV
    if assignments:
        df = pd.DataFrame(assignments)
        df.to_csv("moodle_deadlines.csv", index=False, encoding="utf-8-sig")
        print("✅ Deadlines saved to `moodle_deadlines.csv`")
    else:
        print("⚠️ No assignments found!")

    # Screenshot for verification
    page.screenshot(path="debug_deadlines.png")
    
    # Close browser
    browser.close()
    print("📌 Process complete!")
