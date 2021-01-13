import gmplot
import webbrowser

#imports done

#change paths according to your own system

def show_route(route):
    def change_zoom(file):
        f=open('C:\\Users\\rauna\\Desktop\\internship\\'+str(file),'r',encoding='utf-8')
        x=f.readlines()
        for i in range(len(x)):
            if('zoom' in x[i]):
                num=str()
                for j in x[i]:
                    if(j=='0' or j=='1' or j=='2' or j=='3' or j=='4' or j=='5' or j=='6' or j=='7' or j=='8' or j=='9'):
                        num=num+j
                x[i]=x[i].replace(num,str(int(num)/294)) #divide by a number to get an appropriate zoom. in this case 294
                break
        f.close()
        f=open('C:\\Users\\rauna\\Desktop\\internship\\'+str(file),'w',encoding='utf-8')
        for i in x:
            f.write(i)
        f.close()
    kml_file = open('C:\\Users\\rauna\\Desktop\\internship\\kml\\'+str(route),'r',encoding='utf-8')
    # kml_file=str(kml_file)
    latitude=list()
    longitude=list()
    altitude=list()
    time_of_location=list()
    for i in kml_file:
        if('coord' in i):
            coordinates=i[20:-12].split(' ')
            altitude.append(float(coordinates[2]))
            latitude.append(float(coordinates[1]))
            longitude.append(float(coordinates[0]))
        if('when' in i):
            time_of_location.append(i[27:35])
    gmapOne=gmplot.GoogleMapPlotter(latitude[0],longitude[0],5000)
    gmapOne.draw('C:\\Users\\rauna\\Desktop\\internship\\map.html')
    gmapOne.scatter(latitude,longitude,'#ff0000',size=1,marker=False)
    gmapOne.plot(latitude,longitude,'blue',edge_width=2.5)
    gmapOne.draw('C:\\Users\\rauna\\Desktop\\internship\\map.html')
    change_zoom('map.html')
    webbrowser.open('file:///C:/Users/rauna/Desktop/internship/map.html')

show_route('05-Jan-2021_3_56_23_pm.kml')
