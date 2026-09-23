import unittest

from lru_cache import CacheLRU


class TestCacheLRU(unittest.TestCase):
    def test_insere_e_obtem_valor(self):
        cache = CacheLRU(2)
        cache.inserir("a", "1")

        self.assertEqual(cache.obter("a"), "1")

    def test_cache_miss_retorna_none(self):
        cache = CacheLRU(2)

        self.assertIsNone(cache.obter("inexistente"))

    def test_acesso_atualiza_ordem_lru(self):
        cache = CacheLRU(2)
        cache.inserir("a", "1")
        cache.inserir("b", "2")

        cache.obter("a")
        cache.inserir("c", "3")

        self.assertIsNone(cache.obter("b"))
        self.assertEqual(cache.obter("a"), "1")
        self.assertEqual(cache.obter("c"), "3")

    def test_atualizacao_nao_aumenta_capacidade(self):
        cache = CacheLRU(2)
        cache.inserir("a", "1")
        cache.inserir("b", "2")
        cache.inserir("a", "atualizado")

        self.assertEqual(cache.status_atual(), {"b": "2", "a": "atualizado"})

    def test_capacidade_invalida(self):
        with self.assertRaises(ValueError):
            CacheLRU(0)

        with self.assertRaises(ValueError):
            CacheLRU(-1)


if __name__ == "__main__":
    unittest.main()
