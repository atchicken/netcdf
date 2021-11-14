import netCDF4

nc = netCDF4.Dataset('netcdf.nc', 'r')
temp = nc.variables['t'][:]
print(temp)
print("=========")
print(temp[0])
