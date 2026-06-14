from pydantic import BaseModel

class DocumentSchema(BaseModel):
    """
    Описание структуры документа.
    """
    url: str
    document: str

class GetTariffDocumentResponseSchema(BaseModel):
    tariff: DocumentSchema

class GetContractDocumentResponseSchema(BaseModel):
    contract: DocumentSchema