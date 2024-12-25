from astral import LocationInfo
from astral.sun import sun
import datetime

# Configurar a localização
city = LocationInfo("Porto Velho", "Brasil", "America/Rondonia", latitude=-8.7608, longitude=-63.9004)

# Exibir informações
print(f"Informações sobre {city.name}, {city.region}:")
print(f"Latitude: {city.latitude}, Longitude: {city.longitude}, Fuso horário: {city.timezone}")

# Obter horários do nascer e pôr do sol
today = datetime.date.today()
s = sun(city.observer, date=today)

print("Horários solares:")
print(f"Nascer do Sol: {s['sunrise'].strftime('%H:%M:%S')}")
print(f"Pôr do Sol: {s['sunset'].strftime('%H:%M:%S')}")
print(f"Luz do dia: {s['dawn'].strftime('%H:%M:%S')} - {s['dusk'].strftime('%H:%M:%S')}")
