import os

def generate_reports(df):

    output_path = '../output'
    os.makedirs(output_path, exist_ok=True)

    # 🔷 1. Category-wise spending
    category_spend = df.groupby('category')['withdrawal_amt'].sum().sort_values(ascending=False)
    category_spend.to_csv(f'{output_path}/category_spend.csv')

    # 🔷 2. Monthly spending trend
    if 'date' in df.columns:
        df['month'] = df['date'].dt.to_period('M')
        monthly_spend = df.groupby('month')['withdrawal_amt'].sum()
        monthly_spend.to_csv(f'{output_path}/monthly_spend.csv')

    # 🔷 3. Credit vs Debit summary
    txn_summary = df.groupby('transaction_type')[['withdrawal_amt','deposit_amt']].sum()
    txn_summary.to_csv(f'{output_path}/transaction_summary.csv')

    print("✅ Reports generated in output folder")