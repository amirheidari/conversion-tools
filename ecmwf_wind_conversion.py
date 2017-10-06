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

f=Dataset('ECMWF 2015-16.nc','r')
g=Dataset('new_ecmwf42.nc','w',format='NETCDF4') 
                                      
# To copy the global attributes of the netCDF file  

#for attname in f.ncattrs():
#    setattr(g,attname,getattr(f,attname))

# To copy the dimension of the netCDF file

#for dimname,dim in f.dimensions.iteritems():
#        g.createDimension(dimname,len(dim))

g.createDimension('time',0)
g.createDimension('lon',129)
g.createDimension('lat',65)
        
        
#Create new variables and attributes:

t=f.variables['time']
lat1=f.variables['latitude']
lon1=f.variables['longitude']
u1=f.variables['u10']
v1=f.variables['v10']

lon = g.createVariable(u'lon', np.float32,('lon',))
for attname in lon1.ncattrs():  
    setattr(lon,attname,getattr(lon1,attname))
    
lat = g.createVariable(u'lat', np.float32,('lat',))
for attname in lat1.ncattrs():  
    setattr(lat,attname,getattr(lat1,attname)) 

time=g.createVariable(u'time',np.float32, ('time',))
dtime = num2date(t[:],t.units)
tt=date2num(dtime,units='Hour since 2000-01-01 00:00:00',calendar=t.calendar)

time[:]=tt[:]
time.units='Hour since 2000-01-01 00:00:00'
time.long_name='time'
time.calendar='gregorian'


u=g.createVariable(u'u', np.float32,('time','lat','lon'))
u.scale_factor = 3.8022043110768293E-4
u.add_offset= 1.2040435361772683
u.fill_value = -32767
u.missing_value = -32767
u.units="m s**-1"
u.long_name="10 metre U wind component"


v=g.createVariable(u'v', np.float32,('time','lat','lon'))
v.scale_factor =4.897429549328246E-4
v.add_offset=0.8791768394905511
v.fill_value =-32767
v.missing_value =-32767
v.units="m s**-1"
v.long_name="10 metre V wind component"

#for attname in u1.ncattrs():  
#    setattr(u,attname,getattr(u1,attname))
#for attname in v1.ncattrs():  
#    setattr(v,attname,getattr(v1,attname))

lon[:]=lon1[:]
lat[:]=lat1[:]
u[:,:,:]=u1[:,:,:]
v[:,:,:]=v1[:,:,:]


#i=0
#e=0
#while i<122:
#    dt=t[i+1]-t[i]
#    if dt!=6:
#        print i, t[i], dt
#        e+=1
#    i+=1          
#if e==0: print "Data are increasing and regular"
#
#start=num2date(time[0],time.units)
#end=num2date(time[121],time.units)
#print "data start time:", start
#print "data end time:", end

#print g.dimensions.keys()
#print f.dimensions.keys()
#print f.variables.keys()
#print g.variables.keys()

#g.renameVariable('u','air_u')
#g.renameVariable('v','air_v')


f.close()
g.close()