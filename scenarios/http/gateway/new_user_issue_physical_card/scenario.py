from locust import task

from clients.http.gateway.users.schema import CreateUserResponseSchema
from clients.http.gateway.accounts.schema import OpenDebitCardAccountResponseSchema
from clients.http.gateway.locust import GatewayHTTPSequentialTaskSet
from tools.locust.user import LocustBaseUser


# Класс сценария: описывает последовательный флоу нового пользователя
class IssuePhysicalCardSequentialTaskSet(GatewayHTTPSequentialTaskSet):
    # Храним ответы от предыдущих шагов, чтобы использовать их в следующих задачах
    create_user_response: CreateUserResponseSchema | None = None
    open_debit_card_account_response: OpenDebitCardAccountResponseSchema | None = None

    @task
    def create_user(self):
        # Первый шаг — создать нового пользователя
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_debit_card_account(self):
        # Невозможно открыть счёт без созданного пользователя
        if not self.create_user_response:
            return

        # Открываем дебетовый счёт для нового пользователя
        self.open_debit_card_account_response = self.accounts_gateway_client.open_debit_card_account(
            user_id=self.create_user_response.user.id
        )

    @task
    def create_physical_card_operation(self):
        # Проверяем, что счёт успешно открыт
        if not self.open_debit_card_account_response:
            return

        self.cards_gateway_client.issue_physical_card(
            user_id=self.create_user_response.user.id,
            account_id=self.open_debit_card_account_response.account.id
        )


# Класс пользователя — связывает TaskSet со средой исполнения Locust
class IssuePhysicalCardScenarioUser(LocustBaseUser):
    # сценарий выполнения
    tasks = [IssuePhysicalCardSequentialTaskSet]