from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                  "Chrome/112.0.0.0 Safari/537.36") # создаем экземпляр геокодера

location = geolocator.geocode(" Ростов-на-Дону, Ростовская область, ул. Берберовская, д. 4, лит. 8") # задаем адрес для получения координат

print((location.latitude, location.longitude)) # выводим координаты
