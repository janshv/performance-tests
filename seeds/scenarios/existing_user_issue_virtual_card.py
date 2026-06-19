from seeds.scenario import SeedsScenario
from seeds.schema.plan import SeedsPlan, SeedUsersPlan, SeedCardsPlan, SeedAccountsPlan


class ExistingUserIssueVirtualCardSeedsScenario(SeedsScenario):
    """
    Сценарий сидинга, который будет создавать 300 пользователей и открывать для каждого из них
    один дебетовый счёт и вируальную карту.
    """

    @property
    def plan(self) -> SeedsPlan:
        """
        План сидинга, который описывает, сколько пользователей нужно создать
        и какие именно данные для них генерировать.
        В данном случае создаём 300 пользователей, каждому даём 1 дебетовый счёт.
        """
        return SeedsPlan(
            users=SeedUsersPlan(
                count=300,  # Количество пользователей
                debit_card_accounts=SeedAccountsPlan(
                    count=1,  # Количество счётов на пользователя
                    virtual_cards=SeedCardsPlan(count=1)  # Количество физических карт
                )
            ),
        )

    @property
    def scenario(self) -> str:
        """
        Название сценария сидинга, которое будет использоваться для сохранения данных.
        """
        return "existing_user_issue_virtual_card"


if __name__ == '__main__':
    # Если файл запускается напрямую, создаём объект сценария и запускаем его.
    seeds_scenario = ExistingUserIssueVirtualCardSeedsScenario()
    seeds_scenario.build() # Стартуем процесс сидинга
