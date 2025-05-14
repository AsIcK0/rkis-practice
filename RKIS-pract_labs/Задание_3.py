import psutil
import sqlite3
from datetime import datetime
import time
def create_database():
    conn = sqlite3.connect('system_monitor.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS system_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            cpu_usage REAL,
            memory_usage REAL,
            disk_usage REAL)''')
    conn.commit()
    conn.close()
def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    return cpu_usage, memory_usage, disk_usage
def save_metrics(cpu_usage, memory_usage, disk_usage):
    conn = sqlite3.connect('system_monitor.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO system_metrics (timestamp, cpu_usage, memory_usage, disk_usage)
        VALUES (?, ?, ?, ?)
    ''', (datetime.now(), cpu_usage, memory_usage, disk_usage))
    conn.commit()
    conn.close()
def view_saved_metrics():
    conn = sqlite3.connect('system_monitor.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM system_metrics ORDER BY timestamp DESC LIMIT 10')
    metrics = cursor.fetchall()
    conn.close()
    return metrics
def main():
    create_database()
    while True:
        print("\n1. Мониторинг")
        print("2. Посмотреть сохраненные измерения")
        print("3. Выход")
        choice = input()
        if choice == '1':
                while True:
                    cpu_usage, memory_usage, disk_usage = get_system_metrics()
                    print(f"\nВремя: {datetime.now()}")
                    print(f"Использование ЦП: {cpu_usage}%")
                    print(f"Использование памяти: {memory_usage}%")
                    print(f"Использование диска: {disk_usage}%")
                    save_metrics(cpu_usage, memory_usage, disk_usage)
                    time.sleep(2)
        elif choice == '2':
            print("\nПоследние 10 измерений:")
            metrics = view_saved_metrics()
            for metric in metrics:
                print(f"Время: {metric[1]}, ЦП: {metric[2]}%, Память: {metric[3]}%, Диск: {metric[4]}%")
        elif choice == '3':
            break
if __name__ == "__main__":
    main()
