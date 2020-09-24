#!/usr/bin/env python
# coding: utf-8

# # Accessing IBM Cloud Databases Using Python

# ## 1. IBM Cloud Basics
# 1. Create an account at https://cloud.ibm.com/
# 2. Go to https://cloud.ibm.com/resources
# 3. **Create resource** > **Db2** > Select **London** region and click on **Create**
# 4. To create credentials to access your database instance, go to https://cloud.ibm.com/resources
# 5. Click on your **Db2-xx** service listed under **Services**
# 6. Click on **Service Credentials** in the left menu
# 7. Click on the button to create **New credentials**
# 8. Click the **Add** button in the bottom right
# 9. Copy and save the credentials making a note of the following:
#     * **port** is the database port
#     * **db** is the database name
#     * **host** is the hostname of the database instance
#     * **username** is the username you'll use to connect
#     * **password** is the password you'll use to connect
#     * **URI** (you will need this for Jupyter notebooks when using SQL Magic)

# ## 2. Connect to Db2 database on Cloud using Python

# ### 2.1. Import the `ibm_db` Python library

# In[8]:


import ibm_db


# ### 2.2. Identify the database connection credentials

# In[7]:


#Replace the placeholder values with your actual Db2 hostname, username, and password:
dsn_hostname = "dashdb-txn-sbox-yp-lon02-02.services.eu-gb.bluemix.net" # "YourDb2Hostname"
dsn_uid = "kzg44056"              # "YourDb2Username"
dsn_pwd = "t2vj-12jmmtfrtrl"      # "YoueDb2Password"

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            # "BLUDB"
dsn_port = "50000"                # "50000" 
dsn_protocol = "TCPIP"            # "TCPIP"


# ### 2.3. Identify the database connection credentials

# In[2]:


# DO NOT MODIFY THIS PART
# Create the dsn connection string
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

#print the connection string to check correct values are specified
print(dsn)


# ### 2.4. Create the DB2 database connection

# In[3]:


#DO NOT MODIFY THIS PART
#Create database connection

try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )


# In[4]:


#Retrieve Metadata for the Database Server
server = ibm_db.server_info(conn)

print ("DBMS_NAME: ", server.DBMS_NAME)
print ("DBMS_VER:  ", server.DBMS_VER)
print ("DB_NAME:   ", server.DB_NAME)


# In[5]:


#Retrieve Metadata for the Database Client / Driver
client = ibm_db.client_info(conn)

print ("DRIVER_NAME:          ", client.DRIVER_NAME) 
print ("DRIVER_VER:           ", client.DRIVER_VER)
print ("DATA_SOURCE_NAME:     ", client.DATA_SOURCE_NAME)
print ("DRIVER_ODBC_VER:      ", client.DRIVER_ODBC_VER)
print ("ODBC_VER:             ", client.ODBC_VER)
print ("ODBC_SQL_CONFORMANCE: ", client.ODBC_SQL_CONFORMANCE)
print ("APPL_CODEPAGE:        ", client.APPL_CODEPAGE)
print ("CONN_CODEPAGE:        ", client.CONN_CODEPAGE)


# ### 2.5. Close the Connection

# In[6]:


#Close the connection
ibm_db.close(conn)


# ## 3. Access DB2 on Cloud using Python

# In[ ]:




