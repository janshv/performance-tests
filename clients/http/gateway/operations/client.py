from typing import TypedDict
from urllib.request import Request

from httpx import Response, QueryParams
from clients.http.client import HTTPClient


class GetOperationsRequestDict(TypedDict):
    """
    Структура данных для получения списка операций для определенного счёта.
    """
    accountId: str


class MakeOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции комиссии.
    """
    status: str
    amount: str
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции покупки.
    """
    category: str



class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operations_api(self, query: GetOperationsRequestDict) -> Response:
        """
        Получить список операций для счёта.

        :param query: Словарь с данными списка операций по счёту (accountId).
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))


    def get_operations_summary_api(self, query: GetOperationsRequestDict) -> Response:
        """
        Получить статистику по операциям для счёта.

        :param query: Словарь с данными статистики операций по счёту (accountId).
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations-summary", params=QueryParams(**query))

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получение чека по операции по operation_id.

        :param operation_id: идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получение информации об операции по operation_id.

        :param operation_id: идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def make_fee_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции комиссии.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции пополнения.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции кэшбэка.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции перевода.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создание операции покупки.

        :param request: Словарь с status, amount, cardId, accountId, category.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции оплаты по счету.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции снятия наличных денег.

        :param request: Словарь с status, amount, cardId, accountId.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)






