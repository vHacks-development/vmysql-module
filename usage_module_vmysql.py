import os, sys, time, requests, json

sys.path.append(os.path.abspath("module"))
import vmysql

fetchAll = vmysql.mysqlFetchAll()

# get data with no json loads
print("\nGet all data with no json.loads\n{}".format(fetchAll))

# get data with json loads
print("\nGet all data with json.loads\n{}".format(json.loads(fetchAll)))

# get data with single columns
print("\nGet all data with one column")
fetchAllUsername = vmysql.mysqlFetchAll()
for data in json.loads(fetchAllUsername)["data"]:
	print(data["id"])

#get data with single user
users = "vxinaru"
fetchOne = vmysql.mysqlFetchOne(users)
print("\nGet data from {}\n{}".format(users, fetchOne))

# mysql table
print("\nDisplays table data")
print(vmysql.mysqlTable("users"))