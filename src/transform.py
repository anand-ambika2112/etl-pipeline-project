import pandas as pd

def transform_data(df):
    
    # 1. Drop useless column
    df = df.drop(columns=['.'], errors='ignore')

    # 2. Clean column names properly (IMPORTANT FIX 🔥)
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r'\s+', '_', regex=True)   # replace spaces/tabs with _
        .str.replace(r'[^\w_]', '', regex=True) # remove special chars like ., ()
    )

    print("Columns after cleaning:", df.columns)

    # 3. Handle date columns
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce', dayfirst=True)

    elif 'txn_date' in df.columns:
        df['date'] = pd.to_datetime(df['txn_date'], errors='coerce', dayfirst=True)

    elif 'transaction_date' in df.columns:
        df['date'] = pd.to_datetime(df['transaction_date'], errors='coerce', dayfirst=True)

    else:
        print("⚠️ No 'date' column found")

    if 'value_date' in df.columns:
        df['value_date'] = pd.to_datetime(df['value_date'], errors='coerce',dayfirst=True)

    # 4. Clean & convert numeric columns (IMPORTANT FIX 🔥)
    for col in ['withdrawal_amt', 'deposit_amt', 'balance_amt']:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(',', '')   # remove commas
                .str.strip()
            )
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # 5. Create transaction type
    if 'withdrawal_amt' in df.columns:
        df['transaction_type'] = df['withdrawal_amt'].apply(
            lambda x: 'debit' if x > 0 else 'credit'
        )

    # 6. Create category
    if 'transaction_details' in df.columns:
        df['category'] = df['transaction_details'].astype(str).str.lower().apply(categorize)

    return df


def categorize(text):
    if 'transfer' in text:
        return 'transfer'
    elif 'cash' in text:
        return 'cash'
    elif 'salary' in text:
        return 'salary'
    elif 'upi' in text:
        return 'upi'
    else:
        return 'others'