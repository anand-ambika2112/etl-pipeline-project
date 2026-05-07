import sqlite3

def load_data(df):
    conn = sqlite3.connect('bank.db')
    df.to_sql('transactions', conn, if_exists='replace', index=False)
    conn.close()