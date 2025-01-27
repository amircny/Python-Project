from math import radians,sin,sqrt,cos
import utm
from utm import from_latlon as from_latlong
a=6378132
f=298.257222101
data={"lat":{},"long":{},"hight":None}

def get_data():
    information_latitude_D= float(input("Minute of latitude Geography: "))
    information_latitude_M= float(input("Secand of latitude Geography: "))
    information_latitude_S= float(input("Position of latitude Geography: "))
    information_length_D= float(input("Minute of length Geography: "))
    information_length_M= float(input("Secand of length Geography: "))
    information_length_S= float(input("Position of length Geography: "))
    information_h=float(input("Insert high: "))
    data["lat"].update({
        "degree":information_latitude_D,
        "minutes":information_latitude_M,
        "seconds":information_latitude_S
    })
    data["long"].update({
        "degree":information_length_D,
        "minutes":information_length_M,
        "seconds":information_length_S
    })
    data["hight"]=information_h

def calculate_decimal_degree(degree,minutes,seconds):
    resualt=degree+minutes/60+seconds/3600
    return resualt

def calculate_radian_degree():
    degree_lat=calculate_decimal_degree(**data["lat"])
    degree_long=calculate_decimal_degree(**data["long"])
    degree_lat=round(degree_lat,3)
    degree_long=round(degree_long,3)
    radian_lat=radians(degree_lat)
    radian_long=radians(degree_long)
    return round(radian_lat,3),round(radian_long,3)

def alpha():
    result=round(1/f,3)
    return result

def e():
   result=2*alpha()-alpha()**2
   return round(result,3)

def w():
   #SQRT(1-C8*(SIN(RADIANS(C9)))^2)
    degree_lat=calculate_decimal_degree(**data["lat"])
    result=sqrt(1-e()*(sin(degree_lat))**2)
    return round(result,3)

def n():
    #N = a/W
    result=a/w()
    return round(result,3)

def big():
    #H=N-h;
    h=data["hight"]
    result=n()-h
    return round(result,3)

def  x():
    #(N+h)*COS(RADIANS(deg lat))*COS(RADIANS(deg long))
    h=data["hight"]
    degree_lat=calculate_decimal_degree(**data["lat"])
    degree_long=calculate_decimal_degree(**data["long"])
    result=(n()+h)*cos(radians(degree_lat))*cos(radians(degree_long))
    return round(result,3)

def  y():
     #(N+h)*COS(RADIANS(deg lat))*SIN(RADIANS(deg long))
    h=data["hight"]
    degree_lat=calculate_decimal_degree(**data["lat"])
    degree_long=calculate_decimal_degree(**data["long"])
    result=(n()+h)*cos(radians(degree_lat))*sin(radians(degree_long))
    return round(result,3)   
    

def  z(): 
    #(N*(1-e2)+h)*sin(RADIANS(deg lat))  
    h=data["hight"]
    degree_lat=calculate_decimal_degree(**data["lat"])
    result=(n()*(1-e())+h)*sin(radians(degree_lat))
    return round(result,3)

def utm() -> dict:
    degree_lat=calculate_decimal_degree(**data["lat"])
    degree_long=calculate_decimal_degree(**data["long"])
    utm_result=from_latlong(degree_lat,degree_long)  
    easting = utm_result[0]
    northing = utm_result[1]
    zone_number = utm_result[2]
    zone_letter = utm_result[3]

    return {
        'easting': easting,
        'northing': northing,
        'zone_number': zone_number,
        'zone_letter': zone_letter,
        }   
    
def main():
    get_data()
    print(data)
    while True:
        print("1:Conver Information to Decimal degrees")
        print("2:Conver Information to Radians degrees")
        print("3:Convert W")
        print("4:show Eleva1on H and Geoid height N")
        print("5:show Eleva1on H and Geoid height H")
        print("6:Display Location")
        print("7:Display Location UTM")
        cmd = input("your promt: ")
        if cmd == "1":
            degree_lat=calculate_decimal_degree(**data["lat"])
            degree_long=calculate_decimal_degree(**data["long"])
            degree_lat=round(degree_lat,3)
            degree_long=round(degree_long,3)
            print(5*"-"+"Decimal degrees"+5*"-")
            print(f"La1tude: {degree_lat}\nLongitude:{degree_long}\n")
        elif cmd == "2":
            radian_lat,radian_long=calculate_radian_degree()
            print(5*"-"+"Radian degrees"+5*"-")
            print(f"La1tude: {radian_lat}\nLongitude:{radian_long}\n")
            
        elif cmd == "3":
            result=w()
            print(5*"-"+"W"+5*"-")
            print(result,"\n")

        elif cmd == "4":
            result=n()
            print(5*"-"+"N"+5*"-")
            print(result,"\n")

        elif cmd == "5":
            result=big()
            print(5*"-"+"H"+5*"-")
            print(result,"\n")

        elif cmd == "6":
            data_x,data_y,data_z=x(),y(),z()
            print(5*"-"+"Information X,Y,Z"+5*"-")
            print(f"X: {data_x}\nY:{data_y}\nz:{data_z}\n")
        elif cmd == "7":
            info = utm()
            print(f'easting: {info['easting']}')
            print(f'northing: {info['northing']}')
            print(f'zone number: {info['zone_number']}')
            print(f'letter number: {info['zone_letter']}')

        elif cmd == "-1":
            break
        elif cmd == "":
            continue 
        else:
            print(f"{cmd}: Not Found!")  
main()


