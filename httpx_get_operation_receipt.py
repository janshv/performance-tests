from faker import Faker
import httpx

faker = Faker()


# Создание нового пользователя
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

# Создание кредитного счёта
credit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]
}
open_credit_card_account_payload_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json=credit_card_account_payload
)
open_credit_card_account_response_data = open_credit_card_account_payload_response.json()

card_id = open_credit_card_account_response_data["account"]["cards"][0]["id"]
account_id = open_credit_card_account_response_data["account"]["id"]


# Выполнение операции покупки
purchase_operation_payload = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "cardId": card_id,
    "accountId": account_id,
    "category": "taxi"
}
purchase_operation_response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation", json=purchase_operation_payload)
purchase_operation_response_data = purchase_operation_response.json()
operation_id = purchase_operation_response_data["operation"]["id"]

# Получение чека по операции
operation_receipt_response = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/{operation_id}")
print("Operation receipt data:", operation_receipt_response.json())

