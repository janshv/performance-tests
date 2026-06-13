from typing import TypedDict
from httpx import Response, QueryParams
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """
    Описание структуры операции.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationReceiptDict(TypedDict):
    """
    Описание структуры чека.
    """
    url: str
    document: str


class OperationsSummaryDict(TypedDict):
    """
    Описание структуры статистики.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationsResponseDict(TypedDict):
    operations: list[OperationDict]


class GetOperationsQueryDict(TypedDict):
    """
    Структура query параметров запроса для получения списка операций по счёту.
    """
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура query параметров запроса для получения статистики по операциям счёта.
    """
    accountId: str


class MakeOperationRequestDict(TypedDict):
    """
    Базовая структура тела запроса для создания финансовой операции.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """
    Структура запроса для создания операции комиссии.
    """
    pass

class MakeFeeOperationResponseDict(OperationDict):
    """
    Структура ответа для создания операции комиссии.
    """
    pass


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
    Структура запроса для создания операции пополнения.
    """
    pass

class MakeTopUpOperationResponseDict(OperationDict):
    """
    Структура ответа для создания операции пополнения.
    """
    pass


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """
    Структура запроса для создания операции кэшбэка.
    """
    pass

class MakeCashbackOperationResponseDict(OperationDict):
    """
    Структура ответа для создания операции кэшбэка.
    """
    pass


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
    Структура запроса для создания операции перевода.
    """
    pass

class MakeTransferOperationResponseDict(OperationDict):
    """
    Структура ответа для создания операции перевода.
    """
    pass


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура запроса для создания операции покупки.

    Дополнительное поле:
    - category: категория покупки.
    """
    category: str

class MakePurchaseOperationResponseDict(OperationDict):
    """
    Структура ответа для создания операции покупки.
    """
    pass


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """
    Структура запроса для создания операции оплаты по счёту.
    """
    pass

class MakeBillPaymentOperationResponseDict(OperationDict):
    """
    Структура ответа для создания операции оплаты счёта.
    """
    pass


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """
    Структура запроса для создания операции снятия наличных.
    """
    pass

class MakeCashWithdrawalOperationResponseDict(OperationDict):
    """
    Структура ответа для создания операции выдачи наличных.
    """
    pass


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получает информацию об операции по её идентификатору.

        :param operation_id: Уникальный идентификатор операции.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получает чек по заданной операции.

        :param operation_id: Уникальный идентификатор операции.
        :return: Объект httpx.Response с чеком по операции.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получает список операций по счёту.

        :param query: Словарь с параметром accountId.
        :return: Объект httpx.Response с операциями по счёту.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Получает сводную статистику операций по счёту.

        :param query: Словарь с параметром accountId.
        :return: Объект httpx.Response с агрегированной информацией.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Создаёт операцию комиссии.

        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Создаёт операцию пополнения счёта.

        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Создаёт операцию начисления кэшбэка.

        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Создаёт операцию перевода средств.

        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создаёт операцию покупки.

        :param request: Тело запроса с параметрами операции, включая категорию.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Создаёт операцию оплаты счёта.

        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Создаёт операцию снятия наличных средств.

        :param request: Тело запроса с параметрами операции.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operation(self, operation_id: str) -> OperationDict:
        response = self.get_operation_api(operation_id=operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> OperationReceiptDict:
        response = self.get_operation_receipt_api(operation_id=operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> OperationsSummaryDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=56.78,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=57.79,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=58.80,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=59.81,
            cardId=card_id,
            accountId=account_id,
            category="taxi"
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=60.11,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_payment_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=61.22,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())