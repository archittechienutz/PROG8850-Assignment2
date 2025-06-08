#!/usr/bin/env python3
import os, argparse, mysql.connector
from mysql.connector import Error

# CLI args with env-var defaults
parser = argparse.ArgumentParser()
parser.add_argument('--host',     default=os.getenv('AZURE_MYSQL_HOST'))
parser.add_argument('--user',     default=os.getenv('AZURE_MYSQL_USER'))
parser.add_argument('--password', default=os.getenv('AZURE_MYSQL_PASSWORD'))
parser.add_argument('--database', default=os.getenv('AZURE_MYSQL_DATABASE'))
parser.add_argument('--script',   default='')
args = parser.parse_args()

def run_script(path):
    try:
        conn = mysql.connector.connect(
            host=args.host,
            user=args.user,
            password=args.password,
            database=args.database
        )
        cursor = conn.cursor()
        with open(path, 'r') as f:
            commands = f.read().split(';')
        for cmd in filter(str.strip, commands):
            cursor.execute(cmd)
            print("✔", cmd.splitlines()[0])
        conn.commit()
    except Error as e:
        print("✖ Error:", e)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    if not args.script:
        print("Usage: apply_schema.py --script <path/to/sql>")
    else:
        run_script(args.script)
