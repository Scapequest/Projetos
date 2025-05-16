# Destaque

A função destacada aqui tinha a seguinte proposta: 
> "Faça um programa para gerar automaticamente números entre 0 e 99 de uma cartela de bingo. Sabendo que cada cartela deverá conter 5 linhas de 5 números (matriz 5 x 5), gere estes dados de modo a não ter números repetidos dentro das cartelas. O programa deve apresentar a cartela gerada."

Porém eu quis fazer uma cartala de bingo de verdade, não só uma matriz 5x5. Para isso segui algumas regras:
* A primeira linha é composta da palavra "BINGO", com cada letra em uma coluna;
* O centro da 'cartela' não pode ser um número (usei "BG" para ficar alinhado corretamente);
* Cada coluna tem um range de 14 números: Coluna B é de 1 a 15, Coluna I é de 16 a 30, Coluna N é de 31 a 45, Coluna G é de 46 a 60 e Coluna O é de 61 a 75;

Como a matriz é formada linha por linha, o maior desafio foi conseguir gerar aleatóriamente cada número da linha seguindo a regra de cada coluna, e o centro como "BG".