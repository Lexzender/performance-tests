import time

import httpx  # Импортируем библиотеку HTTPX

# Данные для создания пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Выполняем запрос на создание пользователя
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# Выводим полученные данные пользователя
print("Create user response:", create_user_response_data)
print("Status Code:", create_user_response.status_code)


# Выполняем запрос на открытие депозитного счета

create_deposit_payload = {
    "userId": f"{create_user_response_data['user']['id']}"
}

create_deposit_response = httpx.post("http://localhost:8003/api/v1/accounts/open-deposit-account", json=create_deposit_payload)
create_user_deposit_data = create_deposit_response.json()

# Выводим полученные данные открытого депозитного счета
print("Create deposit response:", create_user_deposit_data)
print("Status Code:", create_deposit_response.status_code)
