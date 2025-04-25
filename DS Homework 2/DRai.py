import os
import sys
import pandas as pd
import json

ITEMS = [
    "Sentiment Positive",
    "Sentiment Negative",
    "Sentiment Neutral",
    "Is Market Category",
    "Is Regulation Category",
    "High Views (Above 20000)",
    "Source CoinDesk"
]

def parse_row(row):
    result = {}

    result["Sentiment Positive"] = "1" if row["Sentiment"] == "Positive" else ""
    result["Sentiment Negative"] = "1" if row["Sentiment"] == "Negative" else ""
    result["Sentiment Neutral"] = "1" if row["Sentiment"] == "Neutral" else ""
    result["Is Market Category"] = "1" if row["Category"] == "Market" else ""
    result["Is Regulation Category"] = "1" if row["Category"] == "Regulation" else ""
    result["High Views (Above 20000)"] = "1" if row["Views"] > 20000 else ""
    result["Source CoinDesk"] = "1" if row["Source"] == "CoinDesk" else ""

    return result

def main():
    if len(sys.argv) < 2:
        print("Usage: python DRai.py <path_to_csv>")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_csv = "output.csv"

    if os.path.exists(output_csv):
        os.remove(output_csv)

    df = pd.read_csv(input_csv)
    results = [parse_row(row) for _, row in df.iterrows()]
    result_df = pd.DataFrame(results)
    final_df = pd.concat([df, result_df], axis=1)
    final_df.to_csv(output_csv, index=False, encoding="utf-8-sig")

    # NEW: print each row as a JSON object block
    for _, row in final_df.iterrows():
        print("-----")
        print("```json")
        print(json.dumps(row.to_dict(), ensure_ascii=False, indent=2))
        print("```")

if __name__ == "__main__":
    main()
    