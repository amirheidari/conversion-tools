# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 07:26:00 2017

@author: USER!
"""

from netCDF4 import Dataset, num2date, date2num
import numpy as np
# Read en existing NetCDF file and create a new one
# f is going to be the existing NetCDF file from where we want to import data
# and g is going to be the new file.

f1=Dataset('15-1.nc','r')
f2=Dataset('15-2.nc','r')
f3=Dataset('15-3.nc','r')
f4=Dataset('15-4.nc','r')
f5=Dataset('15-5.nc','r')
f6=Dataset('15-6.nc','r')
f7=Dataset('15-7.nc','r')
f8=Dataset('15-8.nc','r')
f9=Dataset('15-9.nc','r')
f10=Dataset('15-10.nc','r')
f11=Dataset('15-11.nc','r')
f12=Dataset('15-12.nc','r')
f13=Dataset('16-1.nc','r')
f14=Dataset('16-2.nc','r')

f=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14]

g=Dataset('CMEMS_converted.nc','w',format='NETCDF4') 
                                      
# To copy the global attributes of the netCDF file  

#for attname in f.ncattrs():
#    setattr(g,attname,getattr(f,attname))

# To copy the dimension of the netCDF file

#for dimname,dim in f.dimensions.iteritems():
#        g.createDimension(dimname,len(dim))

g.createDimension('time',0)
g.createDimension('lon',193)
g.createDimension('lat',97)
        
        
#Create new variables and attributes:

#for attname in lon1.ncattrs():  
#    setattr(lon,attname,getattr(lon1,attname))

lon = g.createVariable(u'lon', np.float32,('lon',))
#lon.step = 0.08333588
lon.units = "degrees_east"
#lon.unit_long = "Degrees East"
#lon.long_name = "Longitude"
#lon.standard_name = "longitude"
#lon.axis = "X"
#lon.CoordinateAxisType = "Lon"
    
lat = g.createVariable(u'lat', np.float32,('lat',))
#lat.step = 0.08333588
lat.units = "degrees_north"
#lat.unit_long = "Degrees North"
#lat.long_name = "Latitude"
#lat.standard_name = "latitude"
#lat.axis = "Y"
#lat.CoordinateAxisType = "Lat"


time=g.createVariable(u'time',np.float32, ('time',))
time.units='Hour since 2000-01-01 00:00:00'
time.long_name='time'
time.calendar='gregorian'


u=g.createVariable(u'u', np.float32,('time','lat','lon'))
u.scale_factor = 6.103701889514923E-4
u.add_offset= 0.0
u.fill_value = -32767
u.missing_value = -32767
u.units="m s**-1"
u.unit_long="meters per second"
u.long_name="Eastward velocity"
u.standard_name = "eastward_sea_water_velocity"
u.cell_methods="area: mean"


v=g.createVariable(u'v', np.float32,('time','lat','lon'))
v.scale_factor = 6.103701889514923E-4
v.add_offset= 0.0
v.fill_value = -32767
v.missing_value = -32767
v.units="m s**-1"
v.unit_long="meters per second"
v.long_name="Northward velocity"
v.standard_name = "northward_sea_water_velocity"
v.cell_methods="area: mean"



lat1=f[0].variables['latitude']
lon1=f[0].variables['longitude']    
lon[:]=lon1[:]
lat[:]=lat1[:]


time_dish=[]

for i in range(len(f[:])):
    t=f[i].variables['time']  
    dtime = num2date(t[:],t.units)
    tt=date2num(dtime,units='Hour since 2000-01-01 00:00:00',calendar=t.calendar)
    for j in range(len(tt[:])):
        time_dish.append(tt[j])  
    f[i].close()
    
time[:]=time_dish[:]   

#print len(time[:])
print "time is OK"

f1=Dataset('15-1.nc','r')
f2=Dataset('15-2.nc','r')
f3=Dataset('15-3.nc','r')
f4=Dataset('15-4.nc','r')
f5=Dataset('15-5.nc','r')
f6=Dataset('15-6.nc','r')
f7=Dataset('15-7.nc','r')
f8=Dataset('15-8.nc','r')
f9=Dataset('15-9.nc','r')
f10=Dataset('15-10.nc','r')
f11=Dataset('15-11.nc','r')
f12=Dataset('15-12.nc','r')
f13=Dataset('16-1.nc','r')
f14=Dataset('16-2.nc','r')

f=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14]



init=0
for i in range(len(f[:])):
    t=f[i].variables['time']
    dtime = num2date(t[:],t.units)
    tt=date2num(dtime,units='Hour since 2000-01-01 00:00:00',calendar=t.calendar)
    u1=f[i].variables['uo']
    v1=f[i].variables['vo']
    u[init:(init+len(t[:])),:,:]=u1[:,0,:,:]
    v[init:(init+len(t[:])),:,:]=v1[:,0,:,:]
    init+=len(t[:])
    
    
    f[i].close()

g.close()