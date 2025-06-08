# scripts/apply_schema.py
import os, argparse, mysql.connector
from mysql.connector import Error

parser = argparse.ArgumentParser()
parser.add_argument('--host',     default=os.getenv('DB_HOST', '127.0.0.1'))
parser.add_argument('--user',     default=os.getenv('DB_ADMIN_USER', 'root'))
parser.add_argument('--password', default=os.getenv('DB_PASSWORD', ''))
parser.add_argument('--database', default=os.getenv('DB_NAME', 'mysql'))
parser.add_argument('--script',   default='schema_changes.sql')
args = parser.parse_args()

def main():
    config = {
      'host':     args.host,
      'user':     args.user,
      'password': args.password,
      'database': args.database
    }
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        with open(args.script) as f:
            for stmt in f.read().split(';'):
                if stmt.strip():
                    cursor.execute(stmt)
                    print("✔", stmt.splitlines()[0])
        conn.commit()
    except Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    main()
