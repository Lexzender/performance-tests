from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class BaseOperationRequestDict(TypedDict):
    """
    Общие поля запроса на создание операции.
    """
    status: str
    amount: float
    accountId: str
    cardId: str


class OperationDict(TypedDict):
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    accountId: str


class GetOperationResponseDict(TypedDict):
    operation: list[OperationDict]


class GetOperationsResponseDict(TypedDict):
    operations: list[OperationDict]


class OperationReceiptDict(TypedDict):
    url: str
    document: str


class GetOperationReceiptResponseDict(TypedDict):
    receipt: OperationReceiptDict


class OperationsSummaryDict(TypedDict):
    spentAmount: str
    receivedAmount: str
    cashbackAmount: str


class GetOperationsSummaryResponseDict(TypedDict):
    summary: OperationsSummaryDict


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """
    accountId: str


class MakeFeeOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных создания операции комиссии
    """


class MakeFeeOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeTopUpOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных создания операции пополнения
    """


class MakeTopUpOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeCashbackOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных создания операции кэшбэка
    """


class MakeCashbackOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeTransferOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных создания операции перевода
    """


class MakeTransferOperationResponseDict(TypedDict):
    operation: OperationDict


class MakePurchaseOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных создания операции покупки
    """
    category: str

class MakePurchaseOperationResponseDict(TypedDict):
    operation: OperationDict

class MakeBillPaymentOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных создания операции оплаты по счету
    """
class MakeBillPaymentOperationResponseDict(TypedDict):
    operation: OperationDict

class MakeCashWithdrawalOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных создания операции снятия наличных денег
    """
class MakeCashWithdrawalOperationResponseDict(TypedDict):
    operation: OperationDict

class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получение списка операций для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId ': '123'}.
        :return: Объект httpx.Response с данными об операциях.
        """
        return self.get("/api/v1/operations", params=query)

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Получение статистики по операциям для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId ': '123'}.
        :return: Объект httpx.Response со статистикой об операциях.
        """
        return self.get("/api/v1/operations/operations-summary", params=query)

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param request: Словарь с данными об операции.
        :return: Объект httpx.Response с результатом создания комиссии.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции пополнения.

        :param request: Словарь с данными об операции.
        :return: Объект httpx.Response с результатом операции пополнения.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции кэшбэка.

        :param request: Словарь с данными об операции.
        :return: Объект httpx.Response с результатом операции кэшбэка.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции перевода.

        :param request: Словарь с данными об операции.
        :return: Объект httpx.Response с результатом операции перевода.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param request: Словарь с данными об операции.
        :return: Объект httpx.Response с результатом операции покупки.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции оплаты по счету..

        :param request: Словарь с данными об операции.
        :return: Объект httpx.Response с результатом операции оплаты по счету..
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции снятия наличных денег.

        :param request: Словарь с данными об операции.
        :return: Объект httpx.Response с результатом операции снятия наличных денег.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id) -> GetOperationsSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(
            self,
            status: str,
            amount: float,
            account_id: str,
            card_id: str
    ) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status=status,
            amount=amount,
            accountId=account_id,
            cardId=card_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(
            self,
            status: str,
            amount: float,
            account_id: str,
            card_id: str
    ) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status=status,
            amount=amount,
            accountId=account_id,
            cardId=card_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(
            self,
            status: str,
            amount: float,
            account_id: str,
            card_id: str
    ) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status=status,
            amount=amount,
            accountId=account_id,
            cardId=card_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(
            self,
            status: str,
            amount: float,
            account_id: str,
            card_id: str
    ) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status=status,
            amount=amount,
            accountId=account_id,
            cardId=card_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(
            self,
            status: str,
            amount: float,
            account_id: str,
            card_id: str,
            category: str
    ) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status=status,
            amount=amount,
            accountId=account_id,
            cardId=card_id,
            category=category
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(
            self,
            status: str,
            amount: float,
            account_id: str,
            card_id: str
    ) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status=status,
            amount=amount,
            accountId=account_id,
            cardId=card_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(
            self,
            status: str,
            amount: float,
            account_id: str,
            card_id: str
    ) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status=status,
            amount=amount,
            accountId=account_id,
            cardId=card_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
