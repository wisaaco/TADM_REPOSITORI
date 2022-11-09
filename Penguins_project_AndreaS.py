#!/usr/bin/env python
# coding: utf-8

# ## Mi primer proyecto: Penguins_project_AndreaS
# Volvemos a encontrarnos con el conjunto de datos de pingüinos `PalmerPenguins`. Esta vez trabajaremos con ellos desde `Python`, para ello instalaremos el paquete que nos permitirá cargarlo:
# 

# In[1]:


#%pip install palmerpenguins


# En segundo lugar, importaremos las librerías necesarias:

# In[2]:


import pandas as pd
from palmerpenguins import load_penguins


# Ahora ya estamos en posición de empezar a trabajar con los datos.
# 
# 1. Vamos a cargar el conjunto de datos. Muestra por pantalla el número de observaciones y sus características. Mira el tipo de datos de cada una de sus columnas.

# In[4]:


penguins = load_penguins()

penguins


# 2. Ya sabemos que este conjunto de datos tiene observaciones `NA`. Vamos a eliminarlas y a verificar que efectivamente no queda ninguno:

# In[5]:


penguins.isna().any() #comprobamos que sí existen NA


# In[6]:


penguins1=penguins.dropna() #eliminamos NA


# In[7]:


penguins1.isna().any() #comprobamos que el nuevo data.frame no tiene NA


# 3. ¿Cuántos individuos hay de cada sexo? Puedes obtener la longitud media del pico según el sexo:

# In[9]:


p0=penguins1.groupby(['sex']).describe()
print(p0)


# Para realizar este ejercicio, observamos que existen diferentes formas de realizarlo. 

# In[10]:


p1=penguins1.groupby(['sex'])['sex'].count()
print(p1)


# In[11]:


p2=pd.value_counts(penguins1['sex'])
print(p2)


# In[12]:


p3=penguins['sex'].value_counts()
print(p3)


# Observamos que las tres formas dan el mismo resultado.

# El siguiente data.frame muestra la longitud media según el sexo:

# In[13]:


p4=penguins1.groupby(['sex'])['bill_length_mm'].mean() 
print(p4)


# 4. Vamos a añadir una columna, vamos a realizar una estimación (muy grosera) del área del pico de los pingüinos (bill) tal como si esta fuese un rectángulo. Esta nueva columnas se llama `bill_area` y debe encontrarse en la última posición. Verifica que es correcto.

# Esta es la variable que vamos a crear: La área de un rectangulo: a*b

# In[15]:


bill_area=((penguins1['bill_length_mm']*penguins1['bill_length_mm']))


# Creamos un nuevo dataframe "penguins2" añadiendo la columna "bill_area" en el dataframe "penguins1"

# In[16]:


penguins2=penguins1.assign(bill_area=((penguins1['bill_length_mm']*penguins1['bill_length_mm'])))


# Observamos que este dataframe tiene la columna 'bill_area' en la última posición:

# In[18]:


penguins2.columns.values


# 5. Hagamos algo un poco más elaborado, vamos a realizar una agrupación en función del sexo y de la especie de cada observación. Queremos obtener solamente la información referente al sexo Femenino.

# Primero vamos a crear una nueva variable 'bySex_Spe' que la vamos a agrupar dependiendo del sexo y la especie.

# In[19]:


bySex_Spe=penguins1.groupby(['sex'])['species'] 


# In[21]:


type(bySex_Spe)
bySex_Spe.groups#diccionario


# Seguidamente, vamos a seleccionar solamente la información femenina:

# In[29]:


Penguins_Female_Species=penguins1.loc[bySex_Spe.groups['female']]


# Los siguientes dataframes muestran que solo existen valores femeninos.

# In[33]:


Penguins_Female_Species_Value=penguins1.loc[bySex_Spe.groups['female'].values]


# In[32]:


Penguins_Female_Species_Value.sex.describe() #observamos que solo existen valores femeninos


# 6. Como ya sabemos, la variable peso, se encuentra en gramos, la pasaremos a kg. Para ello crearemos una nueva columna llamada `body_mass_kg` y eliminaremos `body_mass_g`.

# Primero vamos a realizar la operación:

# Vamos a passar de kg a gramos ==> kg=gramos/1000

# In[35]:


body_mass_kg=penguins2['body_mass_g']/1000
print(body_mass_kg)


# Vamos crear un nuevo dataframe 'penguins4' y vamos a añadir la nueva columna que hemos creado 'body_mass_kg' al dataframe realizado en el ejercicio 4, 'penguins2.

# In[37]:


penguins4=penguins2.assign(body_mass_kg=penguins2['body_mass_g']/1000)
penguins4


# Vamos a crear un nuevo dataframe, en el que vamos a eliminar la columna 'body_mass_g' para finalizar el ejercicio. 

# In[38]:


penguins5=penguins4.drop(['body_mass_g'], axis=1)
penguins5


# Hemos comprobado que la columna 'body_mass_g' no está presente en el dataframe penguins5.

# In[42]:


penguins5.columns.values

