import random
import string

class TipoCliente:
  cod_cli = 0
  nome = ''
  fone = ''

class TipoDocumento:
  num_doc = 0
  cod_cli = 0
  dia_venc = 0
  dia_pag = 0
  valor = 0.0
  juros = 0.0

def menu():
  print('\nSistema de Gerenciamento de Documentos e Clientes')
  print('1 - Cadastrar clientes')
  print('2 - Relatório de clientes')
  print('3 - Cadastrar documentos')
  print('4 - Relatório de documentos')
  print('5 - Excluir clientes sem documentos')
  print('6 - Excluir documento por número')
  print('7 - Excluir documento por cliente')
  print('8 - Excluir documento por período')
  print('9 - Alterar dados de cliente')
  print('10 - Quantidade de Documentos por Cliente')
  print('11 - Sair')
  print('12 - Função Teste - Gerar n clientes com documentos aleatóriamente')
  return int(input('Qual opção deseja? '))

def cadastroCliente(clientesV, codigos, doc_dic):
  while True:
    cliente = TipoCliente()
    cliente.nome = input("\nDigite o nome do cliente: ").title()
    cliente.fone = int(input("Digite o telefone do cliente: "))
    doc_dic[codigos[0]] = [] #Criação da chave do dicionário com o código que será usado para o cliente.
    cliente.cod_cli = codigos.pop(0) #Aqui eu tiro o primeiro elemento do vetor com códigos de clientes disponíveis, assim nunca terá dois clientes com o mesmo código, e todos os clientes ficaram organizados pelo código de forma crescente na ordem em que foram cadastrados. (A menos que um código seja excluído e um novo cliente seja cadastrado depois, assim usando o código que foi disponibilizado novamente primeiro)
    clientesV.append(cliente)
    if input("Deseja cadastrar mais? (S/N) ").upper() != "S":
      break
  return clientesV, codigos, doc_dic

def maior(clientesV):
  #Essa função é usada apenas para retornar o tamanho da maior string dentro do vetor de parâmetro.
  m_nome = len(clientesV[0].nome)
  for i in range(len(clientesV)):
    if len(clientesV[i].nome) > m_nome:
      m_nome = len(clientesV[i].nome)
  return m_nome

def relatorioClientes(clientesV, doc_dic):
  if len(clientesV) > 0:
    m_nome = maior(clientesV)
    print(f'\n|{"CÓDIGO":^8}|{"CLIENTE":^{m_nome + 4}}|{"TELEFONE":^12}|{"QTDE DOCUMENTOS":^19}|')
    for i in range(len(clientesV)):
      cliente = clientesV[i]
      print(f'|{cliente.cod_cli:^8}|{cliente.nome:^{m_nome + 4}}|{cliente.fone:^12}|{len(doc_dic[cliente.cod_cli]):^19}|')
  else:
    print("\nNão há clientes cadastrados")

def cadastrarDocumentos(doc_dic, num_doc):
  chave = int(input("\nDigite o código do cliente: ")) #Para cadastrar um documento, peço primeiro o código do cliente e verifico se ele existe no dicionário.
  if chave in doc_dic:
    while True:
      documento = TipoDocumento()
      documento.num_doc = num_doc.pop(0) #Aqui é onde tiro do vetor de números de documentos disponíveis para utilizar a mesma lógica do código de cliente, onde nunca haverá dois documentos com o mesmo número.
      documento.cod_cli = chave
      documento.valor = float(input("Digite o valor do documento: R$ "))
      documento.dia_pag = int(input("Digite o dia do pagamento: "))
      documento.dia_venc = int(input("Digite o dia do vencimento: "))
      if documento.dia_pag > documento.dia_venc:
        documento.juros = documento.valor * 0.05
      doc_dic[chave].append(documento)
      if input("Deseja cadastrar mais? (S/N) ").upper() != "S":
        break
  else:
    print("Código inválido!")
  return doc_dic, num_doc

def relatorioDocumentos(doc_dic):
  print(f'\n|{"Nº DOC":^8}|{"CÓD CLIENTE":^13}|{"VALOR SEM JUROS":^20}|{"VALOR COM JUROS":^20}|{"DIA PAGAMENTO":^15}|{"DIA VENCIMENTO":^16}|')
  for i in doc_dic:
    for j in doc_dic[i]:
      print(f'|{j.num_doc:^8}|{j.cod_cli:^13}|{f"R$ {j.valor:.2f}":^20}|{f"R$ {j.valor+j.juros:.2f}":^20}|{f"{j.dia_pag:02}":^15}|{f"{j.dia_venc:02}":^16}|')

def teste(clientes, doc_dic, codigos, num_doc, quant):
  # Essa é a função de teste, que facilitou testar o código várias vezes, sempre que eu criava e modificava uma função.
  for i in range(quant):
    cliente = TipoCliente()
    cliente.nome = ''.join(random.choices(string.ascii_letters, k=random.randint(5, 10))).title() #Aqui é gerado sequencia de letras aleatórias que simulo como nomes
    cliente.fone = 39030000+ random.randint(1, 9999)
    doc_dic[codigos[0]] = []
    if random.randint(0,10) % 2 == 0: #Para conseguir um resultado mais aleatório pro caso de um cliente ter ou não documentos cadastrados, permiti apenas quando o número gerado fosse par.
      for j in range(random.randint(1,2)):
        documento = TipoDocumento()
        documento.num_doc = num_doc.pop(0)
        documento.cod_cli = codigos[0]
        documento.valor = random.random() * 1000
        documento.dia_pag = random.randint(1,31)
        documento.dia_venc = random.randint(1,31)
        if documento.dia_pag > documento.dia_venc:
          documento.juros = documento.valor * 0.05
        doc_dic[codigos[0]].append(documento)
    cliente.cod_cli = codigos.pop(0)
    clientes.append(cliente)
  return clientes, doc_dic, codigos, num_doc

def excluirVazios(clientes, doc_dic, codigos):
  for i in doc_dic:
    if len(doc_dic[i]) == 0:
      codigos.append(int(i)) #Aqui é onde retorno o código do cliente que vai ser excluído de volta para a lista de códigos disponíveis. Preciso converter para int pois o i está como chave inicialmente.
      for indice, cliente in enumerate(clientes):
        if cliente.cod_cli == int(i):
          clientes.pop(indice)
  return clientes, doc_dic, codigos

def excluirDocumento(doc_dic, num_doc):
  num = int(input("\nDigite o número do documento que deseja excluir: "))
  if num in num_doc:
    print("Documento não encontrado!")
  else:
    for i in doc_dic:
      for indice, objeto in enumerate(doc_dic[i]):
        if objeto.num_doc == num:
          num_doc.append(num) #Mesma lógica do código de cliente, aqui é onde retorno o número de documento para o vetor de números disponíveis
          doc_dic[i].pop(indice)
    print(f"Documento Nº {num} excluído!")
  return doc_dic, num_doc

def excluirDocumentoCliente(doc_dic, codigos, num_doc):
  num = int(input("\nDigite o código do cliente: "))
  if num in codigos:
    print("Cliente não encontrado!")
  else:
    doc_deletados = []
    #Nessa função como precisava excluir todos os documentos do cliente, primeiro eu passo por cada um coletando os números para que sejam disponibilizados para uso.
    for j, i in enumerate(doc_dic[num]):
      doc_deletados.append(int(i.num_doc))
    doc_dic[num] = [] #Então ao invés de excluir cada um, apenas defino o valor da chave para um valor vazio novamente.
    print(doc_deletados)
    num_doc.extend(doc_deletados) #Aqui retorno todos os números de documentos coletados para o vetor de números disponíveis.
  return doc_dic, num_doc

def excluirDocumentoPeriodo(doc_dic, num_doc):
  periodo_inicio = int(input('\nDigite o início do período:'))
  periodo_fim = int(input('Digite o final do período:'))
  periodo = list(range(periodo_inicio,periodo_fim+1)) #Para excluir todos os documentos de um período, uso a entrada do usuário de inicio e final para criar um vetor com todos os números entre esses dois, com eles inclusos, e então verifico se o '.dia_pag' de cada documento possui um valor dentr desse vetor.
  doc_deletados = []
  for i in doc_dic:
    for indice, objeto in enumerate(doc_dic[i]):
      if objeto.dia_venc in periodo:
        doc_deletados.append(objeto.num_doc)
        doc_dic[i].pop(indice)
  print(f"Documentos Excluídos: {len(doc_deletados)}")
  num_doc.extend(doc_deletados)
  return doc_dic, num_doc

def alterarDadosCliente(clientes, codigos):
  while True:
    cliente = int(input("\nDigite o código do cliente para alterar: "))
    if cliente in codigos:
      print("Cliente não cadastrado!")
    else:
      for i in clientes:
        if i.cod_cli == cliente:
          novo_nome = input("Digite o novo nome do cliente (Deixe vazio para manter): ").title()
          novo_fone = int(input("Digite o novo telefone do cliente (Digite 0 para manter): "))
          if len(novo_nome) > 0:
            i.nome = novo_nome
          if novo_fone != 0:
            i.fone = novo_fone
    if input("Desejar alterar outro (S/N)? ").title() != "S":
      break
  return clientes

def relatorioDocumentosClientes(clientesV, doc_dic, codigos):
  cliente = int(input("\nDigite o código do cliente desejado: "))
  if cliente not in codigos:
    for i in clientesV:
      if i.cod_cli == cliente:
        print(f'\n|{"CÓDIGO":^8}|{"CLIENTE":^{len(i.nome)}}|{"TELEFONE":^12}|{"QTDE DOCUMENTOS":^19}|')
        print(f'|{i.cod_cli:^8}|{i.nome:^{len(i.nome)}}|{i.fone:^12}|{len(doc_dic[i.cod_cli]):^19}|')
  else:
    print("\nCliente não cadastrado")

def main():
  clientes = []
  doc_dic = {}
  codigos = list(range(1000,2000))
  num_doc = list(range(200,2200))
  while True:
    codigos.sort()
    num_doc.sort()
    clientes.sort(key=lambda x: x.cod_cli)
    opcao = menu()
    if opcao == 1:
      clientes, codigos, doc_dic = cadastroCliente(clientes, codigos, doc_dic)
    elif opcao == 2:
      relatorioClientes(clientes, doc_dic)
    elif opcao == 3:
      doc_dic, num_doc = cadastrarDocumentos(doc_dic, num_doc)
    elif opcao == 4:
      relatorioDocumentos(doc_dic)
    elif opcao == 5:
      clientes, doc_dic, codigos = excluirVazios(clientes, doc_dic, codigos)
    elif opcao == 6:
      doc_dic, num_doc = excluirDocumento(doc_dic, num_doc)
    elif opcao == 7:
      doc_dic, num_doc = excluirDocumentoCliente(doc_dic, codigos, num_doc)
    elif opcao == 8:
      doc_dic, num_doc = excluirDocumentoPeriodo(doc_dic, num_doc)
    elif opcao == 9:
      clientes = alterarDadosCliente(clientes, codigos)
    elif opcao == 10:
      relatorioDocumentosClientes(clientes, doc_dic, codigos)
    elif opcao == 11:
      break
    elif opcao == 12:
      quant = int(input("Digite a quantidade de clientes para gerar: "))
      clientes, doc_dic, codigos, num_doc = teste(clientes, doc_dic, codigos, num_doc, quant)
    else:
      print("Opção Inválida")

main()