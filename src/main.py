from extract import extract_data
from transform import transform_data
from load import load_data
from report import generate_reports
import os

def run_pipeline():
    df = extract_data('../data/raw_data.csv')
    df_clean = transform_data(df)
    generate_reports(df_clean)
    
    load_data(df_clean)

    # 🔷 Create output folder if not exists
    output_path = '../output'
    os.makedirs(output_path, exist_ok=True)

    # 🔷 Save JSON output
    json_file = os.path.join(output_path, 'result_processed.json')
    df_clean.to_json(json_file, orient='records', indent=4)
    df_clean.to_csv('../output/result_processed.csv', index=False)

    print(f"\n✅ JSON output saved at: {json_file}")
    

    # 🔷 Print sample output
    print("\nSample Data After Transformation:\n")
    print(df_clean.head())

    print("\nData Info:\n")
    print(df_clean.info())


if __name__ == "__main__":
    run_pipeline()