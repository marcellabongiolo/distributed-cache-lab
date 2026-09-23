"""
Módulo: Sistema de Cache LRU (Least Recently Used) de Alta Performance
Autor: Marcella Bongiolo
Descrição: Implementa uma estrutura de dados de cache com limite de capacidade,
           removendo automaticamente os itens menos recentemente utilizados O(1).
"""

from collections import OrderedDict

class CacheLRU:
    """Gerencia um cache em memória com política de expiração LRU."""
    
    def __init__(self, capacidade: int = 3):
        self.capacidade = capacidade
        self.cache = OrderedDict()

    def obter(self, chave: str):
        """Retorna o valor de uma chave se ela existir, movendo-a para o topo (mais recente)."""
        if chave not in self.cache:
            return f"❌ Cache Miss: A chave '{chave}' não foi encontrada."
        
        # Move o item para o final indicando que foi acessado recentemente
        self.cache.move_to_end(chave)
        return f"🎯 Cache Hit: '{chave}' -> {self.cache[chave]}"

    def inserir(self, chave: str, valor: str):
        """Insere ou atualiza um dado no cache, aplicando a regra de capacidade máxima."""
        if chave in self.cache:
            self.cache.move_to_end(chave)
        
        self.cache[chave] = valor
        
        # Se ultrapassar a capacidade, remove o item mais antigo (primeiro da lista)
        if len(self.cache) > self.capacidade:
            item_removido = self.cache.popitem(last=False)
            print(f"🗑️ Capacidade máxima atingida. Removido o mais antigo: {item_removido[0]}")

    def status_atual(self):
        """Exibe o estado atual do cache ordenado do menos para o mais recente."""
        return dict(self.cache)

def main():
    print("=" * 60)
    print(" ⚡ DISTRIBUTED CACHE LAB: SIMULADOR LRU 🗄️")
    print("=" * 60)

    # Criando um cache pequeno de capacidade 3 para testar a substituição
    meu_cache = CacheLRU(capacidade=3)

    print("\n1️⃣ Inserindo dados no cache...")
    meu_cache.inserir("usuario_101", "Dados de Telemetria A")
    meu_cache.inserir("usuario_102", "Dados de Telemetria B")
    meu_cache.inserir("usuario_103", "Dados de Telemetria C")
    print(f"Estado do Cache: {meu_cache.status_atual()}")

    print("\n2️⃣ Acessando o 'usuario_101' (torna-se o mais recente)...")
    print(meu_cache.obrender("usuario_101") if hasattr(meu_cache, 'obrender') else meu_cache.obter("usuario_101"))

    print("\n3️⃣ Inserindo um novo dado ('usuario_104') ultrapassando o limite...")
    meu_cache.inserir("usuario_104", "Dados de Telemetria D")
    print(f"Estado do Cache após inserção: {meu_cache.status_atual()}")
    print("💡 Note que o 'usuario_102' foi removido automaticamente por ser o menos recentemente usado.")

    print("=" * 60)

if __name__ == "__main__":
    main()
  Add high-performance LRU cache implementation
