import mysql.connector
import datetime
from config import host, user, password, db_name

try:
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    print("Успешно подключено к базе данных...")
except mysql.connector.Error as error:
    print("Ошибка при подключении к базе данных:", error)
    exit()

cursor = conn.cursor()

with open(r'C:\Users\Андрей\Desktop\python\practice\access_logs.log', 'r') as file:
    access_logs = file.readlines()

for log_line in access_logs:
    log_data = log_line.split(' - - ')
    if len(log_data) < 2:
        continue

    ip_address = log_data[0]

    timestamp_str = log_data[1].split(' [')[1].split(']')[0] if ' [' in log_data[1] else ''
    timestamp = datetime.datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S %z") if timestamp_str else None
    

    request_data = log_data[1].split('"')
    if len(request_data) < 3:
        continue

    request_line = request_data[1].strip()
    request_parts = request_line.split()
    if len(request_parts) != 3:
        continue

    request_method, requested_page, http_version = request_parts

    response_parts = request_data[2].split()
    if len(response_parts) != 2:
        continue

    try:
        status_code = int(response_parts[0])
        response_size = int(response_parts[1])
    except ValueError:
        continue

    user_agent = request_data[3] if len(request_data) > 3 else ''

    query = "INSERT INTO access_logs (ip_address, timestamp, request_method, requested_page, http_version, status_code, response_size, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (ip_address, timestamp, request_method, requested_page, http_version, status_code, response_size, user_agent)
    cursor.execute(query, values)

conn.commit()
cursor.close()
conn.close()
