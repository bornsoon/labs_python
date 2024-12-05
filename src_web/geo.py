from geopy.geocoders import Nominatim

add = '서울특별시 종로구 청계천로 11'

geoloc = Nominatim(user_agent = 'South Korea', timeout=None)    # 사용자 에이전트를 설정
geo = geoloc.geocode(add)     # 주소로 위치 정보 가져오기
lat = str(geo.latitude)
log = str(geo.longitude)

print(lat)
print(log)