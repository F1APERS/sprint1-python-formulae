class Equipe:

    equipes = []

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

        Equipe.equipes.append(self)

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
                f"Poles: {self.poles}\n")


mahindra = Equipe("Mahindra Racing", "Edoardo Mortara", "Nyck de Vries", "Jordan King, Kush Maini", "Mahindra M10Electro", "Frederic Bertrand", 5, 24, 125, 11)
mito = Equipe("mito", "Edoardo Mortara", "Nyck de Vries", "Jordan King, Kush Maini", "Mahindra M10Electro", "Frederic Bertrand", 5, 24, 125, 11)
mito2 = Equipe("jabaquara", "Edoardo Mortara", "Nyck de Vries", "Jordan King, Kush Maini", "Mahindra M10Electro", "Frederic Bertrand", 5, 24, 125, 11)
mito3 = Equipe("rihap", "Edoardo Mortara", "Nyck de Vries", "Jordan King, Kush Maini", "Mahindra M10Electro", "Frederic Bertrand", 5, 24, 125, 11)



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
        equipes_start()
    elif fazer == 2:
        pilotos_start()
    elif fazer == 3:
        end()

def end():
    print("Até mais!")
    return None


def equipes_start():
    print("Aqui estão as equipes da Fórmula E:\n")

    for i in Equipe.equipes:
        print(f" - {i.nome}")

    fazer = input("Digite o número correspondente à equipe que deseja acessar.\n"
                  "-> ")

def pilotos_start():
    return None


start()