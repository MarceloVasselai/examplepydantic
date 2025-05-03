from pydantic import BaseModel

# Definindo um modelo de usuário
class User(BaseModel):
    name: str
    email: str
    age: int

# Criando uma instância do modelo
user_data = {
    "name": "João",
    "email": "joao@example.com",
    "age": 30
}
user = User(**user_data)

# Verificando se os dados são válidos (o Pydantic valida automaticamente os tipos)
print(user)  # Imprime os dados do usuário em formato JSON
print(user.name) # Imprime apenas o nome do usuário
print(user.model_dump_json()) # Imprime os dados do usuário em formato JSON

# Validação de dados: tentar criar uma instância com dados inválidos
try:
    invalid_user_data = {
        "name": "Maria",
        "email": "invalid_email",
        "age": "32" # Tentar passar um string em vez de um int  
    }
    invalid_user = User(**invalid_user_data)
    print(invalid_user)
except Exception as e:
    print(f"Erro de validação: {e}")
    print("Dados inválidos não foram aceitos.")

# Serialização e desserialização 
user_json = user.model_dump_json()
print(f"JSON: {user_json}") # Imprime os dados em formato JSON  
new_user = User.model_validate(user_json) # Desserializa de volta para um objeto 
print(f"Objeto: {new_user}") # Imprime o objeto criado 