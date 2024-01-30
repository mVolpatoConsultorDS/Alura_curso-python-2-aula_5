from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
parto_paozinho = Prato('Paozinho', 2.00, 'O melhor pao da cidade')

def main():
    print(bebida_suco)
    print(parto_paozinho)

if __name__ == '__main__':
    main()