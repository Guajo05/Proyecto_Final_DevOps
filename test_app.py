import unittest
from app import app

class TestHolaMundo(unittest.TestCase):

    def setUp(self):
        # Configura un cliente de prueba para la aplicación
        self.app = app.test_client()
        self.app.testing = True

    def test_mensaje_hola_mundo(self):
        # Realiza una solicitud GET a la ruta principal
        response = self.app.get('/')
        # Verifica que la respuesta sea 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Verifica que el texto de respuesta sea el correcto
        self.assertIn('¡Hola Mundo desde DevOps!'.encode('utf-8'), response.data)

if __name__ == '__main__':
    unittest.main()