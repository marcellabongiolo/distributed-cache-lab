"""Implementação de um cache LRU (Least Recently Used) em memória.

A estrutura usa collections.OrderedDict para manter a ordem de uso e
realizar inserções, atualizações e acessos em tempo O(1) amortizado.
"""

from collections import OrderedDict


class CacheLRU:
    """Cache em memória com capacidade limitada e política de descarte LRU."""

    def __init__(self, capacidade: int = 3) -> None:
        if capacidade <= 0:
            raise ValueError("A capacidade deve ser maior que zero.")

        self.capacidade = capacidade
        self.cache: OrderedDict[str, str] = OrderedDict()

    def obter(self, chave: str) -> str | None:
        """Retorna o valor associado à chave e a marca como recentemente usada."""
        if chave not in self.cache:
            return None

        self.cache.move_to_end(chave)
        return self.cache[chave]

    def inserir(self, chave: str, valor: str) -> None:
        """Insere ou atualiza um valor, removendo o menos recentemente usado se necessário."""
        self.cache[chave] = valor
        self.cache.move_to_end(chave)

        if len(self.cache) > self.capacidade:
            self.cache.popitem(last=False)

    def status_atual(self) -> dict[str, str]:
        """Retorna uma cópia do estado atual do cache."""
        return dict(self.cache)


def main() -> None:
    """Executa uma demonstração simples do comportamento do cache."""
    print("=" * 60)
    print("⚡ DISTRIBUTED CACHE LAB: SIMULADOR LRU 🗄️")
    print("=" * 60)

    cache = CacheLRU(capacidade=3)

    print("\n1. Inserindo dados no cache...")
    cache.inserir("usuario_101", "Dados de Telemetria A")
    cache.inserir("usuario_102", "Dados de Telemetria B")
    cache.inserir("usuario_103", "Dados de Telemetria C")
    print(f"Estado do cache: {cache.status_atual()}")

    print("\n2. Acessando 'usuario_101'...")
    print(f"Cache Hit: {cache.obter('usuario_101')}")

    print("\n3. Inserindo 'usuario_104' e ultrapassando a capacidade...")
    cache.inserir("usuario_104", "Dados de Telemetria D")
    print(f"Estado do cache: {cache.status_atual()}")
    print("💡 'usuario_102' foi removido por ser o menos recentemente usado.")

    print("=" * 60)


if __name__ == "__main__":
    main()
