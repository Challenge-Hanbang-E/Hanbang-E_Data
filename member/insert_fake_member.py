import json

from db_connect import cur, conn
from logger_config import logger

i = 1

hundred_thousand = []

while True:
    try:
        member_file_path = f'./data/members/member_{i}.json'

        with open(member_file_path, "r") as member_file:
            values_data = json.load(member_file)
            values_data = values_data['member']
            hundred_thousand.append(values_data)

            if i % 4 == 0:
                values = str(hundred_thousand).replace("[", "").replace("]", "").replace('"', "")

                sql = "INSERT IGNORE INTO member (EMAIL, PASSWORD, ADDRESS) VALUES" + values
                cur.execute(sql)
                conn.commit()

                hundred_thousand = []

        i += 1
    except:
        logger.info(f"member_{i}.json 도중 에러")
        break

conn.close()
