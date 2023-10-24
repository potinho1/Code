# Importe as bibliotecas necessárias
from flask import Flask, request, jsonify
from shapely.geometry import Polygon
from shapely.geometry import Point

app = Flask(__name)

# Dados fictícios que representam polígonos de culturas em coordenadas fictícias
dados_mapbiomas = {
    '2021': [
        {
            'cultura': 'Milho',
            'area': 1000,  # em hectares
            'origem': 'MapBiomas',
            'poligono': Polygon([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])
        }
    ],
    '2022': [
        {
            'cultura': 'Soja',
            'area': 1500,  # em hectares
            'origem': 'MapBiomas',
            'poligono': Polygon([(2, 2), (2, 3), (3, 3), (3, 2), (2, 2)])
        }
    ]
}

# Função para consultar as culturas com base em coordenadas
def consultar_culturas_em_coordenadas(coordinates):
    resultado = {}
    point = Point(coordinates)  # Cria um objeto Point com as coordenadas fornecidas

    # Percorre os dados fictícios do MapBiomas para 2021 e 2022
    for ano, dados in dados_mapbiomas.items():
        for dado in dados:
            # Verifica se o ponto está dentro do polígono
            if point.within(dado['poligono']):
                resultado[ano] = {
                    'ano': int(ano),
                    'cultura': dado['cultura'],
                    'area': dado['area'],
                    'origem': dado['origem'],
                    'poligono': dado['poligono']
                }

    return resultado

@app.route('/consultar_culturas', methods=['POST'])
def consultar_culturas():
    data = request.get_json()
    coordinates = data.get('coordinates')
    
    # Chama a função para consultar as culturas com base nas coordenadas
    resultado = consultar_culturas_em_coordenadas(coordinates)
    
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
