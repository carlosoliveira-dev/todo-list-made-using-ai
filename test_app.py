import unittest
import json
from app import app  # Supondo que o seu arquivo Flask se chama app.py

class TestAddTask(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Inicia a aplicação Flask em modo de teste
        cls.client = app.test_client()

    def test_add_task_valid(self):
        # Dados válidos para enviar
        task_data = {"task": "Learn Flask Testing"}

        # Envia a requisição POST com os dados no formato JSON
        response = self.client.post('/tasks', data=json.dumps(task_data), content_type='application/json')

        # Verifica se o código de status é 201 (Criado)
        self.assertEqual(response.status_code, 201)

        # Verifica se o ID e o nome da tarefa estão no corpo da resposta
        response_json = json.loads(response.data)
        self.assertEqual(response_json["task"], "Learn Flask Testing")
        self.assertIn("id", response_json)

    def test_add_task_missing_content(self):
        # Dados faltando o campo 'task'
        task_data = {}

        # Envia a requisição POST com dados inválidos
        response = self.client.post('/tasks', data=json.dumps(task_data), content_type='application/json')

        # Verifica se o código de status é 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Verifica se a mensagem de erro está correta
        response_json = json.loads(response.data)
        self.assertEqual(response_json["error"], "Task content is required")

if __name__ == '__main__':
    unittest.main()
