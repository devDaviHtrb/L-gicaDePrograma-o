estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut","ca",
"az"]) 
estacoes = {}
estacoes["kum"] = set(["id", "nv", "ut"])
estacoes["kdois"] = set(["wa", "id", "mt"])
estacoes["ktres"] = set(["or", "nv", "ca"])
estacoes["kquatro"] = set(["nv", "ut"])
estacoes["kcinco"] = set(["ca", "az"])
estacoes_final = set()
#Enquanto ainda ouverem estados a serem supridos
while estados_abranger:
    topStation = None
    topStationStates = set()
    #percorre todas as estaçoes
    for station in estacoes:
        estacoesCobertas = set()
        print(station)
        #percorr todos os estados da estação
        for states in estacoes[station]:
            print(states)
            #adiciona apenas os estados que não foram supridos
            if states in estados_abranger:
                estacoesCobertas.add(states)
        #Se os estados supridos pela estação anterior foram inferiores a atual, a mesma é substituida
        if topStationStates < estacoesCobertas:
            topStation = station
            topStationStates = estacoesCobertas
    #Remove os estaados ja supridos e adiciona a melhor estação a lista
    estados_abranger-=topStationStates
    estacoes_final.add(topStation)
print(estacoes_final)

