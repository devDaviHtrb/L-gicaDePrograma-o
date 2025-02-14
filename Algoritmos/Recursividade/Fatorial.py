def fatorial(x):
    if x == 1:
        return 1
    else:
        return x*fatorial(x-1)
    
#explicando de traz pra frente, quando a função é executada é criada uma pilha onde o topo possui um Fatorial(1), ou seja, retorna 1, então a que está abaixo retorna n*1 repetindo esse processo n vezes até que n seja igual a x

#em geral a recursividade não adiciona velocidade ao algoritmo entretanto torna-o mais suscinto, porém pode causar problemas de memória pelo acúmulo de funções