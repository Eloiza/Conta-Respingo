# Conta-Respingo

### Descrição
O objetivo deste projeto é medir a proteção oferecida por diferentes tipos de máscara faceshield. Foram avaliados dois modelos, um deles disponível no mercado em abril de 2020 e um novo modelo desenvolvido por pesquisadores da UNESP. Para simular o uso das máscaras foi utilizado uma cabeça de manequim branca. Os testes foram feitos com o uso de um liquido vermelho para borrifar o manequim em três condições diferentes: com a máscara disponível no mercado, com a máscara desenvolvida pelos pesquisadores e sem máscara. Após a borrifada, foram feitas seções de fotos com o manequim sem a máscara testada, nos ângulos 0, 45 e 90 graus. Com o uso do algoritmo disponível aqui, foi avaliado a porcentagem de tinta vermelha que atingiu diretamente o manequim com relação a área da cabeça do manequim.

O código principal pode ser encontrado no arquivo `main.py` e a implementação das principais funções usadas pode ser encontrada no arquivo `contarespingo.py`. O mesmo código presente nos arquivos `.py` também está disponível em forma de python notebook e pode ser acessado pelo arquivo deste repositório `ContaRespingo.ipynb` ou acessando o google colaboratory [clicando aqui!](https://colab.research.google.com/drive/1U6iijQLX70jgwnVNHzfAJ9yhC-jjS7gq) ou pelo arquivo python notebook presente no repositório. 

    
### Dependências
Para executar o código é preciso ter instalado a biblioteca `opencv` e `numpy`. Você pode instalar a biblioteca `opencv` executando o código abaixo:

```
pip3 install opencv-python
```

E a biblioteca `numpy` pode ser instalada com o comando abaixo:
```
pip3 install numpy
```

### Executando o Código
Para executar o código basta executar o comando abaixo:
```
python3 main.py
```
