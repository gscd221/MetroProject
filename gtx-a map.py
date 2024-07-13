import folium

center=[37.4,127.1]
m=folium.Map(location=center,zoom_start=13)

lines=[[37.487260862968,127.10155515462],[37.394724096,127.119652136],[37.298340438,127.104203899],[37.200138454,127.09553409]]
gtxastn = ["수서역","성남역","구성역","동탄역"]

folium.Marker(lines[0],popup="표시",tooltip=gtxastn[0]).add_to(m)
folium.Marker(lines[1],popup="표시",tooltip=gtxastn[1]).add_to(m)
folium.Marker(lines[2],popup="표시",tooltip=gtxastn[2]).add_to(m)
folium.Marker(lines[3],popup="표시",tooltip=gtxastn[3]).add_to(m)

folium.Marker

folium.PolyLine(locations=lines,color="magenta",).add_to(m)

m.save("gtxa1.html")
