import json

pessoas = [
  {
    "nome": "Vinícius",
    "cargo": "Pleno",
    "Salário": "2800",
    "documento": "990011334"
  },
  {
    "nome": "Wesley",
    "cargo": "Pleno",
    "Salário": "5100",
    "documento": "101112334"
  },
    {
    "nome": "Ximena",
    "cargo": "Estagio",
    "Salário": "1250",
    "documento": "112233445"
  },
  {
    "nome": "Alef",
    "cargo": "Pleno",
    "Salário": "2000",
    "documento": "123456789"
  },
  {
    "nome": "Becker",
    "cargo": "Senior",
    "Salário": "4000",
    "documento": "987654321"
  },
  {
    "nome": "Alan",
    "cargo": "Estagio",
    "Salário": "1000",
    "documento": "456789123"
  },
  {
    "nome": "Carlos",
    "cargo": "Pleno",
    "Salário": "2500",
    "documento": "112233445"
  },
  {
    "nome": "Diana",
    "cargo": "Senior",
    "Salário": "4500",
    "documento": "223344556"
  },
  {
    "nome": "Elena",
    "cargo": "Estagio",
    "Salário": "1200",
    "documento": "334455667"
  },
  {
    "nome": "Felipe",
    "cargo": "Pleno",
    "Salário": "2300",
    "documento": "445566778"
  },
  {
    "nome": "Gustavo",
    "cargo": "Pleno",
    "Salário": "5000",
    "documento": "556677889"
  },
  {
    "nome": "Helena",
    "cargo": "Estagio",
    "Salário": "1100",
    "documento": "667788990"
  },
  {
    "nome": "Igor",
    "cargo": "Pleno",
    "Salário": "2700",
    "documento": "778899001"
  },
  {
    "nome": "Julia",
    "cargo": "Senior",
    "Salário": "4800",
    "documento": "889900112"
  },
  {
    "nome": "Kaique",
    "cargo": "Estagio",
    "Salário": "1300",
    "documento": "990011223"
  },
  {
    "nome": "Larissa",
    "cargo": "Pleno",
    "Salário": "2200",
    "documento": "101112223"
  },
  {
    "nome": "Marcelo",
    "cargo": "Pleno",
    "Salário": "4700",
    "documento": "112233334"
  },
  {
    "nome": "Natália",
    "cargo": "Estagio",
    "Salário": "1050",
    "documento": "223344445"
  },
  {
    "nome": "Otávio",
    "cargo": "Pleno",
    "Salário": "2400",
    "documento": "334455556"
  },
  {
    "nome": "Paula",
    "cargo": "Pleno",
    "Salário": "4900",
    "documento": "445566667"
  },
  {
    "nome": "Quintino",
    "cargo": "Estagio",
    "Salário": "1150",
    "documento": "556677778"
  },
  {
    "nome": "Rafael",
    "cargo": "Pleno",
    "Salário": "2600",
    "documento": "667788889"
  },
  {
    "nome": "Sofia",
    "cargo": "Pleno",
    "Salário": "4600",
    "documento": "778899990"
  },
  {
    "nome": "Tânia",
    "cargo": "Estagio",
    "Salário": "1400",
    "documento": "889900001"
  }
]

def pessoass():
  for pessoa in pessoas:
      pessoa =  print(f'''
Colaborador: 
    {pessoa['nome']}
Documento: 
    {pessoa['documento']}
 ''')
  return pessoa


def pessoas_Alfabetica():
    ordem = sorted(pessoas, key=lambda pessoa: pessoa["nome"])

    for pessoa in ordem:
        certo = print(f'''
Colaborador: 
    {pessoa['nome']}
Documento: 
    {pessoa['documento']}
 ''')
    return certo
 

def pessoas_Salario():
    salario = sorted(pessoas, key=lambda pessoa: pessoa['Salário'])

    for pessoa in salario:
        valor = print(f'''
Colaborador: 
    {pessoa['nome']}
Salário: 
    {pessoa['Salário']}
 ''')
    return valor

 
def listar_por_cargo(cargo):
    # Filtra as pessoas pelo cargo e retorna apenas nome e cargo
    filtrados = [{"nome": pessoa["nome"], "cargo": pessoa["cargo"]} for pessoa in pessoas if pessoa["cargo"].lower() == cargo.lower()]
    return filtrados
def cargos_Filter():
    cargos = [pessoa["cargo"] for pessoa in pessoas]
    cargo = input("Digite o cargo (Pleno, Senior, Estagio): ")
    pessoas_filtradas = listar_por_cargo(cargo)
    
    if pessoas_filtradas:
        for pessoa in pessoas_filtradas:
          pessoa = print(f'''
Colaborador: 
    {pessoa['nome']}
Cargo: 
    {pessoa['cargo']}
 ''')
        return pessoa
    else:
      erro = print("Nenhuma pessoa encontrada para o cargo informado.")
      return erro