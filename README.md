# Situação Proposta

Devemos realizar uma requisição ao servidor/API do Github para obter dados de um usuário.



## Passo 1

Temos o seguinte método stub criado para o teste: get_username(username:str) Esse método espera receber o nome de um usuario do GitHub. Em seguida deve ser realizada a consulta dos dados do usuário. A saída deve ser um dict com os dados retornados pela API.

obs: Pode realizar a requisição do modo que preferir.



## Passo 2

Queremos que você crie um objeto/classe para representar alguns dos dados retornados. Escolha quais os elementos principais do dict do passo anterior para serem armazenados. Faça um teste simples para saber se os valores estão de acordo com o que é esperado para o campo.

`import unittest

def get_username(username: str) -> dict:

...

class User: ...

class TestMethods(unittest.TestCase):

"""Classe de testes unitários. Crie seus testes aqui."""

def test_this_test_words(self):

self.assertTrue(True)

def test_username_parameters(self):

parameters = ['login', 'id', 'avatar_url', 'html_url']

response = get_username('githubuser')

for param in parameters:

   self.assertTrue(param in response.keys())



def test_user_object(self):

...

if __name__ == "__main__":

  unittest.main()`