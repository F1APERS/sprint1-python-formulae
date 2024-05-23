
"""

equipes = []
pilotos = []

def criar_equipe(nome, piloto1, piloto2, pilotoR, carro, diretor, wins, podiums, races, poles):
    equipe = [nome, piloto1, piloto2, pilotoR, carro, diretor, wins, podiums, races, poles]
    equipes.append(equipe)

def criar_piloto(nome, equipe, naturalidade, idade, estreia, wins, podiums, races, poles):
    piloto = [nome, equipe, naturalidade, idade, estreia, wins, podiums, races, poles]
    pilotos.append(piloto)

def exibir_equipe(equipe):
    print(f"Informações da Equipe:\n\n"
          f"Equipe: {equipe[0]}\n"
          f"Piloto 1: {equipe[1]}\n"
          f"Piloto 2: {equipe[2]}\n"
          f"Piloto de Reserva: {equipe[3]}\n"
          f"Carro: {equipe[4]}\n"
          f"Diretor: {equipe[5]}\n\n"
          f"Estaísticas da Equipe:\n\n"
          f"Vitórias: {equipe[6]}\n"
          f"Pódios: {equipe[7]}\n"
          f"Corridas: {equipe[8]}\n"
          f"Poles: {equipe[9]}")

def exibir_piloto(piloto):
    print(f"Informações do Piloto:\n\n"
          f"Nome: {piloto[0]}\n"
          f"Equipe: {piloto[1]}\n"
          f"Naturalidade: {piloto[2]}\n"
          f"Idade: {piloto[3]}\n"
          f"Estreia: {piloto[4]}\n\n"
          f"Estatísticas do Piloto:\n\n"
          f"Vitórias: {piloto[5]}\n"
          f"Pódios: {piloto[6]}\n"
          f"Corridas: {piloto[7]}\n"
          f"Poles: {piloto[8]}")

# Exemplo de uso
criar_equipe("Mahindra Racing", "Edoardo Mortara", "Nyck de Vries", "Jordan King, Kush Maini", "Mahindra M10Electro", "Frederic Bertrand", 5, 24, 125, 11)
criar_piloto("Jake Dennis", "Andretti", "Reino Unido", 28, 2021, 6, 21, 24, 6)

exibir_equipe(equipes[0])
exibir_piloto(pilotos[0])


"""

# Classe que define uma equipe
class Equipe:

    # Lista de equipes
    equipes = []

    # Inicializa a equipe
    def __init__(self, nome, piloto1, piloto2, pilotoR, carro, diretor, wins, podiums, races, poles):

        # Essenciais
        self.nome = nome
        self.piloto1 = piloto1
        self.piloto2 = piloto2
        self.pilotoR = pilotoR
        self.carro = carro
        self.diretor = diretor

        # Estatísticas
        self.wins = wins
        self.podiums = podiums
        self.races = races
        self.poles = poles

        # Adiciona a equipe à lista de equipes
        Equipe.equipes.append(self)

    # Exibe as informações da equipe
    def __str__(self):
        return (f"Informações da Equipe:\n\n"
                f"Equipe: {self.nome}\n"
                f"Piloto 1: {self.piloto1}\n"
                f"Pilot 2: {self.piloto2}\n"
                f"Piloto de Reserva: {self.pilotoR}\n"
                f"Carro: {self.carro}\n"
                f"Diretor: {self.diretor}\n\n"
                f"Estaísticas da Equipe:\n\n"
                f"Vitórias: {self.wins}\n"
                f"Pódios: {self.podiums}\n"
                f"Corridas: {self.races}\n"
                f"Poles: {self.poles}")


# Classe que define um piloto
class Piloto:

    # Lista de pilotos
    pilotos = []

    # Inicializa o piloto
    def __init__(self, nome, equipe, naturalidade, idade, estreia, wins, podiums, races, poles):

        # Essenciais
        self.nome = nome
        self.equipe = equipe
        self.naturalidade = naturalidade
        self.idade = idade
        self.estreia = estreia

        # Estatísticas
        self.wins = wins
        self.podiums = podiums
        self.races = races
        self.poles = poles

        # Adiciona o piloto à lista de pilotos
        Piloto.pilotos.append(self)

    # Exibe as informações do piloto
    def __str__(self):
        return (f"Informações do Piloto:\n\n"
                f"Nome: {self.nome}\n"
                f"Equipe: {self.equipe}\n"
                f"Naturalidade: {self.naturalidade}\n"
                f"Idade: {self.idade}\n"
                f"Estreia: {self.estreia}\n\n"
                f"Estatísticas do Piloto:\n\n"
                f"Vitórias: {self.wins}\n"
                f"Pódios: {self.podiums}\n"
                f"Corridas: {self.races}\n"
                f"Poles: {self.poles}")


# Dados das equipes

mahindra = Equipe("Mahindra Racing", "Edoardo Mortara", "Nyck de Vries", "Jordan King, Kush Maini", "Mahindra M10Electro", "Frederic Bertrand", 5, 24, 125, 11)
cupra = Equipe("Abt Cupra", "Lucas Di Grassi", "Nico Müller", "Kelvin van der Linde", "Mahindra M10Electro", "Thomas Biermaier", 14, 47, 109, 6)
andretti = Equipe("Andretti", "Jake Dennis", "Norman Nato", "Zane Maloney", "Porsche 99X Electric Gen3", "Roger Griffiths", 11, 39, 126, 13)
penske = Equipe("Ds Penske", "Jean-Éric Vergne", "Stoffel Vandoorne", "Oliver Turvey", "DS E-TENSE FE23", "Jay Penske", 3, 16, 126, 5)
envision = Equipe("Envision Racing", "Sébastien Buemi", "Robin Frijns", None, "Jaguar I-Type 6", "Sylvain Filippi", 16, 50, 126, 15)
ert = Equipe("ERT", "Dan Ticktum", "Sérgio Sette Câmara", None, "ERT X24", "Alex Hui", 2, 6, 126, 2)
jaguar = Equipe("Jaguar TCS Racing", "Mitch Evans", "Nick Cassidy", "Joel Eriksson, Tom Dillmann", "Jaguar I-Type 6", "James Barclay", 15, 41, 105, 8)
maserati = Equipe("Maserati MSG Racing", "Jehan Daruvala", "Maximilian Günther", None, "Maserati Tipo Folgore", None, 10, 27, 126, 5)
mcLaren = Equipe("Neom McLaren", "Jake Hughes", "Sam Bird", "Taylor Barnard", "Nissan e-4ORCE 04", "Ian James", 8, 25, 81, 12)
tagHeuerPorsche = Equipe("Tag Heuer Porsche", "Pascal Wehrlein", "António Félix da Costa", "André Lotterer, David Beckmann", "Porsche 99X Electric Gen3", "Florian Modlinger", 8, 16, 68, 6)
nissan = Equipe("Nissan", "Oliver Rowland", "Sacha Fenestraz", "Caio Collet", "Nissan e-4ORCE 04", "Tommaso Volpe", 18, 46, 126, 24)

# Dados dos pilotos

JakeDennis = Piloto("Jake Dennis", "Andretti", "Reino Unido", 28, 2021, 6, 21, 24, 6)
StoffelVandoorne = Piloto("Stoffel Vandoorne", "Ds Penske", "Bélgica", 32, 2018, 3, 16, 81, 8)
SetteCamara = Piloto("Sérgio Sette Câmara", "ERT", "Brasil", 26, 2020, 0, 0, 60, 0)
RobinFrijns = Piloto("Robin Frijns", "Envision Racing", "Holanda", 32, 2015, 2, 14, 96, 2)
JoelEriksson = Piloto("Joel Eriksson", "Jaguar TCS Racing", "Suécia", 25, 2021, 0, 0, 10, 0)
JakeHughes = Piloto("Jake Hughes", "Neom McLaren", "Reino Unido", 30, 2023, 0, 0, 25, 3)
MaximiianGunther = Piloto("Maximilian Günther", "Maserati MSG Racing", "Alemanha", 26, 2018, 5, 10, 77, 2)
samBird = Piloto("Sam Bird", "Neom McLaren", "Reino Unido", 37, 2014, 10, 25, 126, 8)
taylorbarnard = Piloto("Taylor Barnard", "Neom McLaren", "Reino Unido", 19, 2024, 0, 0, 0, 0)
mitchEvans = Piloto("Mitch Evans", "Jaguar TCS Racing", "Nova Zelândia", 29, 2016, 5, 16, 126, 3)
lucasDiGrassi = Piloto("Lucas Di Grassi", "Abt Cupra", "Brasil", 39, 2014, 14, 47, 126, 6)
dacosta = Piloto("António Félix da Costa", "Tag Heuer Porsche", "Portugal", 32, 2014, 8, 16, 126, 6)
paularon = Piloto("Paul Aron", "Tag Heuer Porsche", "Estônia", 20, 2024, 0, 0, 0, 0)
sebastiaan = Piloto("Sébastien Buemi", "Envision Racing", "Suíça", 35, 2014, 16, 50, 126, 15)
normanNato = Piloto("Norman Nato", "Andretti", "França", 31, 2021, 0, 0, 24, 0)
jehanDaruvala = Piloto("Jehan Daruvala", "Maserati MSG Racing", "Índia", 25, 2022, 0, 0, 26, 0)
nyckDeVries = Piloto("Nyck de Vries", "Mahindra Racing", "Holanda", 29, 2021, 5, 24, 126, 11)
jordanKing = Piloto("Jordan King", "Mahindra Racing", "Reino Unido", 30, 2021, 0, 0, 0, 0)
oliverRowland = Piloto("Oliver Rowland", "Nissan", "Reino Unido", 31, 2018, 3, 18, 126, 3)
sachaFenestraz = Piloto("Sacha Fenestraz", "Nissan", "França", 24, 2022, 0, 0, 0, 0)
jeanEricVergne = Piloto("Jean-Éric Vergne", "Ds Penske", "França", 33, 2014, 3, 16, 126, 5)
danticktum = Piloto("Dan Ticktum", "ERT", "Reino Unido", 25, 2021, 2, 6, 126, 2)
nickcast = Piloto("Nick Cassidy", "Jaguar TCS Racing", "Nova Zelândia", 29, 2021, 0, 0, 26, 0)
edoardo = Piloto("Edoardo Mortara", "Mahindra Racing", "Suíça", 37, 2017, 5, 24, 126, 11)
nicomuller = Piloto("Nico Müller", "Abt Cupra", "Suíça", 31, 2021, 14, 47, 126, 6)
vanderlinde = Piloto("Kelvin van der Linde", "Abt Cupra", "África do Sul", 27, 2022, 0, 0, 0, 0)
pascalwehrlein = Piloto("Pascal Wehrlein", "Tag Heuer Porsche", "Alemanha", 29, 2018, 8, 16, 126, 6)


# Inicializa o programa
def start():
    print("Olá, seja bem-vindo(a) à database das equipes e pilotos da Fórmula E!!\n")
    print("1 - Acessar equipes\n"
          "2 - Acessar pilotos\n"
          "3 - Sair\n")

    fazer = input("O que deseja fazer? (Digite o número correspondente)\n"
                  "-> ")

    while not fazer.isnumeric() or int(fazer) < 1 or int(fazer) > 3:
        fazer = input("Opção inválida. Digite novamente.\n"
          "-> ")

    fazer = int(fazer)

    if fazer == 1:
        start_infos('equipes')
    elif fazer == 2:
        start_infos('pilotos')
    elif fazer == 3:
        end()

# Finaliza o programa
def end():
    print("Até mais!")
    return None


# Mostra os dados das equipes ou dos pilotos e chama a função de forçar escolha
def start_infos(who):
    print(f"Aqui estão as fichas de {who} da Fórmula E:\n")

    lista = []

    if who == 'equipes':
        lista = Equipe.equipes
    elif who == 'pilotos':
        lista = Piloto.pilotos

    index = 1
    for i in lista:
        print(f"{index} - {i.nome}")
        index += 1

    print(f"\n- Voltar\n"
          f"- Sair\n")

    escolha = input("Digite o número correspondente à ficha que deseja acessar.\n"
                    "Caso contrário, digite 'voltar' para voltar ao menu ou 'sair' para encerrar o programa.\n"
                    "-> ")

    forcar_escolha(index, escolha, who)


# Força a escolha do usuário, chama a função de acessar informações e dá opção de voltar para o menu ou finalizar o programa
def forcar_escolha(Index, Escolha, who):

    escolha = Escolha
    index = Index

    while True:
        if escolha.isnumeric():
            escolha_num = int(escolha)

            if 1 <= escolha_num <= index - 1:
                if who == 'equipes':
                    exibir_infos(escolha_num, 'equipe')
                    break
                elif who == 'pilotos':
                    exibir_infos(escolha_num, 'piloto')
                    break
                break
            else:
                escolha = input("Opção inválida. Digite novamente.\n"
                                "-> ")
                continue

        elif escolha.lower() == 'voltar':
            start()
            break
        elif escolha.lower() == 'sair':
            end()
            break
        escolha = input("Opção inválida. Digite novamente.\n"
                        "-> ")


# Exibe as informações da equipe ou do piloto escolhido
def exibir_infos(Escolha, who):

    escolha = Escolha

    if who == 'equipe':
        print(Equipe.equipes[escolha - 1])
        voltar_sair('equipe')
    elif who == 'piloto':
        print(Piloto.pilotos[escolha - 1])
        voltar_sair('piloto')


# Dá opção de voltar para o menu anterior, voltar para o menu principal ou encerrar o programa
def voltar_sair(local):
    print("\n- Voltar\n"
          "- Sair\n"
          "- Menu\n")

    fazer = input("Digite 'voltar' para voltar ao menu anterior, 'sair' para encerrar o programa ou 'menu' para acessar o menu principal.\n"
                  "-> ")

    while True:
        if fazer.lower() == 'voltar':
            if local == 'equipe':
                start_infos('equipes')
                break
            elif local == 'piloto':
                start_infos('pilotos')
                break
        elif fazer.lower() == 'sair':
            end()
            break
        elif fazer.lower() == 'menu':
            start()
            break

        fazer = input("Opção inválida. Digite novamente.\n"
                        "-> ")


# Inicializa o programa
start()