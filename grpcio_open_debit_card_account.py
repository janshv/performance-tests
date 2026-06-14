import grpc
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountRequest, \
    OpenDebitCardAccountResponse
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from tools.fakers import fake


# Устанавливаем соединение с gRPC-сервером по адресу localhost:9003
channel = grpc.insecure_channel("localhost:9003")

# Создаём gRPC-клиент для UsersGatewayService
users_gateway_service = UsersGatewayServiceStub(channel)

# Создаём gRPC-клиент для AccountsGatewayService
debit_account_service = AccountsGatewayServiceStub(channel)

# Формируем запрос на создание пользователя с рандомными данными
create_user_request = CreateUserRequest(
    email=fake.email(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name(),
    phone_number=fake.phone_number()
)

# Отправляем запрос и получаем ответ на создание пользователя
create_user_response: CreateUserResponse = users_gateway_service.CreateUser(create_user_request)
print('Create user response:', create_user_response)

# Формирование запроса на открытие дебетового счёта; указывается user.id, полученный из ответа создания пользователя
create_account_request = OpenDebitCardAccountRequest(user_id=create_user_response.user.id)

# Создание дебетового счёта и получение ответа
debit_account_response: OpenDebitCardAccountResponse = debit_account_service.OpenDebitCardAccount(create_account_request)
print('Open debit card account response:', debit_account_response)