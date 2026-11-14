import time
import httpx  # Импортируем HTTPX

# Шаг 1. Создание пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",  # Уникальный email с timestamp
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# Шаг 2. Открытие кредитного счета
open_credit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]
}
open_credit_card_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json=open_credit_card_account_payload
)
open_credit_card_account_response_data = open_credit_card_account_response.json()

# Выполнение операции покупки
make_purchase_operation_payload = {
    "status": "COMPLETED",
    "amount": 100,
    "cardId": open_credit_card_account_response_data["account"]["cards"][0]["id"],
    "accountId": open_credit_card_account_response_data["account"]["id"],
    "category": "test"
}
make_purchase_operation_response = httpx.post(
    "http://localhost:8003/api/v1/operations/make-purchase-operation",
    json=make_purchase_operation_payload
)
make_purchase_up_operation_response_data = make_purchase_operation_response.json()

# Вывод результатов в консоль
print("Make purchase operation response:", make_purchase_up_operation_response_data)
print("Make purchase operation status code:", make_purchase_operation_response.status_code)