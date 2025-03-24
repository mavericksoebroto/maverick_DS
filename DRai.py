import os
import sys
import pandas as pd

# Define evaluation criteria
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
    """
    Evaluate each row based on criteria and return a dictionary with '1' or ''.
    """
    result = {}

    # Sentiment evaluation
    result["Sentiment Positive"] = "1" if row["Sentiment"] == "Positive" else ""
    result["Sentiment Negative"] = "1" if row["Sentiment"] == "Negative" else ""
    result["Sentiment Neutral"] = "1" if row["Sentiment"] == "Neutral" else ""

    # Category evaluation
    result["Is Market Category"] = "1" if row["Category"] == "Market" else ""
    result["Is Regulation Category"] = "1" if row["Category"] == "Regulation" else ""

    # Views evaluation
    result["High Views (Above 20000)"] = "1" if row["Views"] > 20000 else ""

    # Source evaluation
    result["Source CoinDesk"] = "1" if row["Source"] == "CoinDesk" else ""

    return result

def main():
    if len(sys.argv) < 2:
        print("Usage: python DRai.py <path_to_csv>")
        sys.exit(1)
    
    input_csv = sys.argv[1]
    output_csv = "output.csv"  # Changed output filename

    if os.path.exists(output_csv):
        os.remove(output_csv)
    
    # Read the input CSV
    df = pd.read_csv(input_csv)

    # Evaluate each row and store results
    results = [parse_row(row) for _, row in df.iterrows()]

    # Convert evaluation results into DataFrame and merge with the original
    result_df = pd.DataFrame(results)
    final_df = pd.concat([df, result_df], axis=1)

    # Save the evaluated data to output.csv
    final_df.to_csv(output_csv, index=False, encoding="utf-8-sig")
    
    print(f"Evaluation completed. Results saved to: {output_csv}")

if __name__ == "__main__":
    main()
