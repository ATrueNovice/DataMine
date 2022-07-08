import sqlite3


data_db = '/Users/shaughton-scott/Desktop/DataMine/DMP/db.db'


connect = sqlite3.connect(data_db)
cursor = connect.cursor()



cursor.execute("""
    CREATE TABLE IF NOT EXISTS node (
        id INTEGER PRIMARY KEY,
        computer_name,
        system,
        version,
        last_update,
        processor,
        machine,
        mac_address,
        ip_address
    )
               """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS computer_details (
        id INTEGER PRIMARY KEY,
        physical_cores,
        total_cores,
        max_frequency,
        min_frequency,
        processor,
        cpu_usage,
        storage,
        storage_used,
        storage_free,
        storage_size,
        storage_usage_percent,
        memory,
        available,
        used,
        percentage,
        last_update
        
        
    )
    
               """)





