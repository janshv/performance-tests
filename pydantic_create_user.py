from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserSchema(BaseModel):
    """
     Модель данных пользователя
    """
    model_config = ConfigDict(validate_by_alias=True)
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserRequestSchema(BaseModel):
    """
     Модель данных запроса на создание пользователя : POST /api/v1/users
    """
    model_config = ConfigDict(validate_by_alias=True)
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserResponseSchema(BaseModel):
    """
    Модель данных ответа на создание пользователя : POST /api/v1/users
    """
    user: UserSchema
