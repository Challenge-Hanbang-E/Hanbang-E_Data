import json

from faker import Faker

fake = Faker('ko-KR')

i = 1

all_email_data = []
sql_values = []
email_list = []

variation_value = 30  # 데이터를 더 생성하려면 여기를 변동해주셔야 합니다!

while i <= variation_value:
    while True:
        email_file_path = f'email_{i}.json'
        member_file_path = f'member_{i}.json'

        try:
            with open(email_file_path, "r") as email_file:
                data = json.load(email_file)
                email_data = data["email"]
                all_email_data.append(email_data)
                i += 1
        except:
            email_file_path = f'email_{i}.json'
            member_file_path = f'member_{i}.json'

            default_email_file = {"email": []}
            default_member_file = {"member": []}
            email_list = default_email_file["email"]
            sql_values = default_member_file["member"]
            break

    while len(email_list) < 25000:
        email_split = fake.email().split("@")
        email_change = email_split[0] = email_split[0] + f"{len(all_email_data)}" + f"{len(email_list)}@"
        fake_email = "".join(email_split)
        email_list.append(fake_email)
        value = f"('{fake_email}', '{fake.password()}', '{fake.address()}')"
        sql_values.append(value)

    with open(email_file_path, 'w') as email_outfile:
        json.dump(default_email_file, email_outfile, ensure_ascii=False)

    with open(member_file_path, 'w') as member_outfile:
        json.dump(default_member_file, member_outfile, indent=1, ensure_ascii=False)
