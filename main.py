import os
import mysql.connector
from mysql.connector import Error
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Database credentials from .env
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_DATABASE = os.getenv('DB_DATABASE', 'iposyandu')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')

def get_db_connection():
    """Establish and return a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            database=DB_DATABASE,
            user=DB_USER,
            password=DB_PASSWORD
        )
        if conn.is_connected():
            print('Connected to MySQL database')
        return conn
    except Error as er:
        print(f"Error connecting to database: {er}")
        return None

def process_and_pivot_age_data(conn):
    """Processes and pivots baby check-up age data."""
    print("\n--- Processing Age Data ---")
    query = """
        SELECT id, babies_id, checkup_date, c_age, o_age, m_age, o_pbu, o_bbu, o_bbpb, m_pbu, m_bbu, m_bbpb
        FROM babies_dob_checkup_bgo_bgm_age
        WHERE c_age BETWEEN 0 AND 60
    """
    my_data = pd.read_sql(query, conn)
    my_data = my_data.fillna(0)
    my_data['satu'] = my_data['id'] / my_data['id']
    my_data_pivot = pd.pivot_table(my_data, values='satu', index=['babies_id'], columns='c_age')
    my_data_pivot['isi'] = my_data_pivot.apply(lambda x: x.count(), axis='columns')
    my_data_pivot.to_csv('babies_age_pivot.csv')
    my_data_pivot.fillna(0).to_csv('babies_age_pivot_0.csv')

def process_and_pivot_pbu_data(conn):
    """Processes and pivots PBU data."""
    print("\n--- Processing PBU Data ---")
    query = """
        SELECT id, babies_id, name, checkup_date, c_age, o_pbu, m_pbu
        FROM babies_dob_checkup_bgo_bgm_age
        WHERE c_age BETWEEN 0 AND 60
    """
    my_data = pd.read_sql(query, conn)
    my_data['pbu'] = my_data[['o_pbu', 'm_pbu']].sum(axis=1)
    my_data_pivot = pd.pivot_table(my_data, values='pbu', index=['babies_id', 'name'], columns='c_age')
    my_data_pivot.to_csv('babies_history_pbu.csv')
    my_data_pivot['total'] = my_data_pivot.apply(lambda x: x.count(), axis='columns')
    my_data_pivot.to_csv('babies_history_pbu_total.csv')

def filter_data_by_total_checkups():
    """Filters data based on total check-ups."""
    print("\n--- Filtering by Check-ups ---")
    babies_history = pd.read_csv('babies_history_pbu_total.csv')
    
    babies_history[babies_history['total'] > 1].reset_index(drop=True).drop('total', axis=1).to_csv('babies_history_ge_2.csv', index=False)
    babies_history[babies_history['total'] > 2].reset_index(drop=True).drop('total', axis=1).to_csv('babies_history_ge_3.csv', index=False)
    babies_history[babies_history['total'] > 3].reset_index(drop=True).drop('total', axis=1).to_csv('babies_history_ge_4.csv', index=False)

def filter_data_by_specific_ages():
    """Filters data for specific ages (3, 6, 9, 12 months)."""
    print("\n--- Filtering by Ages 3, 6, 9, 12 ---")
    babies_history = pd.read_csv('babies_history_pbu_total.csv')
    babies_history_36912 = babies_history.loc[(babies_history['3'].notnull()) &
                                             (babies_history['6'].notnull()) &
                                             (babies_history['9'].notnull()) &
                                             (babies_history['12'].notnull())]
    babies_history_36912.to_csv('babies_history_36912.csv', index=False)

def main():
    """Main function to run the entire data processing workflow."""
    conn = get_db_connection()
    if conn:
        try:
            process_and_pivot_age_data(conn)
            process_and_pivot_pbu_data(conn)
            filter_data_by_total_checkups()
            filter_data_by_specific_ages()
            # Add other functions for height/weight and vitamin/immune data
        finally:
            conn.close()

if __name__ == "__main__":
    main()
