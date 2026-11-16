from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient

class BaseOperationRequestDict(TypedDict):
    """
    Общие поля запроса на создание операции.
    """
    status: str
    amount: float
    accountId: str
    cardId: str

class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций для определенного счета.
    """
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """
    accountId: str


class MakeFeeOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных создания операции комиссии
    """

class MakeTopUpOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных создания операции пополнения
    """

class MakeCashbackOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных создания операции кэшбэка
    """

class MakeTransferOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных создания операции перевода
    """

class MakePurchaseOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных создания операции покупки
    """
    category: str

class MakeBillPaymentOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных создания операции оплаты по счету
    """

class MakeCashWithdrawalOperationRequestDict(BaseOperationRequestDict):
    """
    Структура данных создания операции снятия наличных денег
    """

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


