import osmnx as ox
import requests
import urllib.parse


place = 'Paris, France'

url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(place) +'?format=json'

response = requests.get(url).json()

lat = float(response[0]["lat"])
lon = float(response[0]["lon"])

point = (lat, lon)

print(f"Creando mapa para {place}")

G = ox.graph_from_point(point, dist=10000, retain_all=True, simplify = True, network_type='all')

#Agua
'''G2 = ox.graph_from_point(point, dist=15000, dist_type='bbox', network_type='all', 
                         simplify=True, retain_all=True, truncate_by_edge=False, 
                         clean_periphery=False, custom_filter='["waterway"~"river"]')'''
                


u = []
v = []
key = []
data = []
for uu, vv, kkey, ddata in G.edges(keys=True, data=True):
    u.append(uu)
    v.append(vv)
    key.append(kkey)
    data.append(ddata)    

'''tipos = []
for item in data:
    if "name" in item.keys():
        if 'La Seine' == item['name']:
            item['name']'''
    


# List to store colors
roadColors = []
roadWidths = []

for item in data:
    if "length" in item.keys():
        if item["length"] <= 100:
            linewidth = 0.10
            color = "#a6a6a6" 
            
        elif item["length"] > 100 and item["length"] <= 200:
            linewidth = 0.15
            
            color = "#666666"
            
        elif item["length"] > 200 and item["length"] <= 400:
            linewidth = 0.25
            color = "#4d4d4d"
            
            
        elif item["length"] > 400 and item["length"] <= 800:
            color = '#000000'
            linewidth = 0.35
        else:
            color = "#000000"
            linewidth = 0.45
    else:
        color = "#a6a6a6"
        linewidth = 0.10

    roadColors.append(color)
    roadWidths.append(linewidth)

bgcolor = "#ffffff"

print("Creando mapa")

fig, ax = ox.plot_graph(G, node_size=0,figsize=(27, 40), 
                        dpi = 300,bgcolor = bgcolor,
                        save = False, edge_color=roadColors,
                        edge_linewidth=roadWidths, edge_alpha=1)

print("Guardando mapa")
fig.tight_layout(pad=0)
fig.savefig("output/paris.pdf", dpi=300, bbox_inches='tight', format="pdf", facecolor=fig.get_facecolor(), transparent=False)


#color para el río Sena
'''if "name" in item.keys():
    if 'La Seine' == item['name']:
        color = "#00ace6"
        linewidth = 0.45'''