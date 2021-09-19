#!/usr/bin/env python
# coding: utf-8

# # Introdução à programação em um contexto visual
# > com Python e Processing, usando a biblioteca [py5](py5.ixora.io)

# In[1]:


def setup():
    size(500, 500, P3D)


# In[2]:


def draw():
    translate(250, 250, 0)
    background(255)
    rotate_y(mouse_x / 4.0) # 22.5 graus
    for x in range(-100, 101, 50):
        for y in range(-100, 101, 50):
            for z in range(-100, 101, 50):
                fill(100 + x, 100 + y, 100 + z)
                my_box(x, y, z, 25 + 25 * sin(x + y + frame_count / 20.0))


# In[3]:


def my_box(x, y, z, tamanho):
    push()
    translate(x, y, z)
    box(tamanho)
    pop()


# In[4]:


run_sketch()  # chama o setup() uma vez, e o draw() em repetição.

# Para ver o resultado, usando o mybinder.org o Thebe Live Code no Jupyter book
portal = py5_tools.sketch_portal(quality=75, scale=1.0)
portal


# In[ ]:




