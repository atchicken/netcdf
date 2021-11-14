import argparse
import netCDF4 as nc4


def main():
    """
    createNetCDF.py'main
    """
    
    args = Parse()
    createNC(args)


def createNC(args):
    """
    Create Input Data and Save NetCDF File
    """

    
    if args.ncNum == 1:
        nc = nc4.Dataset(args.ncPath, "w", format="NETCDF4")
    elif args.ncNum == 2:
        nc = nc4.Dataset(args.ncPath, "w", format="NETCDF4_CLASSIC")
    elif args.ncNum == 3:
        nc = nc4.Dataset(args.ncPath, "w", format="NETCDF3_CLASSIC")
    elif args.ncNum == 4:
        nc = nc4.Dataset(args.ncPath, "w", format="NETCDF3_64BIT_OFFSET")
    elif args.ncNum == 5:
        nc = nc4.Dataset(args.ncPath, "w", format="NETCDF3_64BIT_DATA")
    else:
        nc = nc4.Dataset(args.ncPath, "w")

    latList, lonList, tempList = [], [], []

    for lon in range(0, 360, 10):
        lonList.append(lon)


    for lat in range(-60, 61, 10):
        latList.append(lat)
        tmpTempList = []
        for lon in range(0, 360, 10):
            temp = (60 - abs(lat)) * 0.6
            tmpTempList.append(temp)

        tempList.append(tmpTempList)


    nc.createDimension("lon", len(lonList))
    nc.createDimension("lat", len(latList))

    lon = nc.createVariable("lon", "i1", "lon")
    lat = nc.createVariable("lat", "i1", "lat")
    temp = nc.createVariable("t", "i1", ("lat", "lon"), fill_value=99999)

    lon[:], lat[:], temp[:, :] = lonList, latList, tempList

    # Add Settings
    nc.history = "Create New"
    lon.long_name = "Longitude"
    lon.units = "Degree"
    lat.long_name = "Latitude"
    lat.units = "Degree"
    temp.long_name = "Temperature"
    temp.units = "Degree of Celsius"
    
    nc.close()



def Parse():
    """
    CommandLine Arguments Settings

    Note:
        ncNum: Kind of NetCDF Version
               1: NetCDF4
               2: NetCDF4 Classic
               3: NetCDF3 Classic
               4: NetCDF3 64Bit_Classic
               5: NetCDF3 64Bit_Data
               Others: NetCDF
    """
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--ncNum", type=int, default=0)
    parser.add_argument("-p", "--ncPath", type=str, default="./netcdf.nc")
    args = parser.parse_args()

    return args

    

if __name__ == "__main__":
    main()
