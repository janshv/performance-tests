from typing import TypedDict
from httpx import Response
from clients.http.client import HTTPClient


class IssueCardRequestDict(TypedDict):
    """
    Структура данных для выпуска виртуальной и физических карт пользователя.
    """
    userId : str
    accountId : str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Выпуск виртуальной карты для пользователя.

        :param request: Словарь с данными пользователя (userId, accountId).
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Выпуск физической карты для пользователя.

        :param request: Словарь с данными пользователя (userId, accountId).
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)
