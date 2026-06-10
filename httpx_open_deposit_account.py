from faker import Faker
import httpx

faker = Faker()

create_user_payload = {
    "email": faker.email(),
    "lastName": faker.last_name(),
    "firstName":faker.first_name(),
    "middleName": faker.first_name(),
    "phoneNumber": faker.phone_number()
}

create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
user_id = create_user_response_data['user']['id']

print("Create user response:", create_user_response_data)
print("User ID:", user_id)
print("Status Code:", create_user_response.status_code)

print("="*200)

open_deposit_payload = {
    "userId": user_id
}

open_dep_response = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account", json=open_deposit_payload)

print("Open deposit response data:", open_dep_response.json())
print("Status Code:", open_dep_response.status_code)