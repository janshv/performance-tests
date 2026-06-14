from enum import StrEnum
from pydantic import BaseModel, ConfigDict, Field


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """
    Описание структуры операции.
    """
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationResponseSchema(BaseModel):
    operation: OperationSchema


class OperationReceiptSchema(BaseModel):
    """
    Описание структуры чека.
    """
    url: str
    document: str


class OperationsSummarySchema(BaseModel):
    """
    Описание структуры статистики.
    """
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")

class OperationsSummaryResponseSchema(BaseModel):
    summary: OperationsSummarySchema


class GetOperationsResponseSchema(BaseModel):
    operations: list[OperationSchema]


class GetOperationsQuerySchema(BaseModel):
    """
    Структура query параметров запроса для получения списка операций по счёту.
    """
    model_config = ConfigDict(populate_by_name=True)
    account_id: str


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура query параметров запроса для получения статистики по операциям счёта.
    """
    model_config = ConfigDict(populate_by_name=True)
    account_id: str


class MakeOperationRequestSchema(BaseModel):
    """
    Базовая структура тела запроса для создания финансовой операции.
    """
    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus
    amount: float
    card_id: str
    account_id: str


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции комиссии.
    """
    model_config = ConfigDict(populate_by_name=True)
    pass

class MakeFeeOperationResponseSchema(OperationResponseSchema):
    """
    Структура ответа для создания операции комиссии.
    """
    pass


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции пополнения.
    """
    model_config = ConfigDict(populate_by_name=True)
    pass

class MakeTopUpOperationResponseSchema(OperationResponseSchema):
    """
    Структура ответа для создания операции пополнения.
    """
    pass


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции кэшбэка.
    """
    model_config = ConfigDict(populate_by_name=True)
    pass

class MakeCashbackOperationResponseSchema(OperationResponseSchema):
    """
    Структура ответа для создания операции кэшбэка.
    """
    pass


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции перевода.
    """
    model_config = ConfigDict(populate_by_name=True)
    pass

class MakeTransferOperationResponseSchema(OperationResponseSchema):
    """
    Структура ответа для создания операции перевода.
    """
    pass


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции покупки.

    Дополнительное поле:
    - category: категория покупки.
    """
    model_config = ConfigDict(populate_by_name=True)
    category: str

class MakePurchaseOperationResponseSchema(OperationResponseSchema):
    """
    Структура ответа для создания операции покупки.
    """
    pass


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции оплаты по счёту.
    """
    model_config = ConfigDict(populate_by_name=True)
    pass

class MakeBillPaymentOperationResponseSchema(OperationResponseSchema):
    """
    Структура ответа для создания операции оплаты счёта.
    """
    pass


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура запроса для создания операции снятия наличных.
    """
    model_config = ConfigDict(populate_by_name=True)
    pass

class MakeCashWithdrawalOperationResponseSchema(OperationResponseSchema):
    """
    Структура ответа для создания операции выдачи наличных.
    """
    pass