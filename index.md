---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: py5
  language: python
  name: py5
---

# Introdução à programação em um contexto visual
> com Python e Processing, usando a biblioteca [py5](py5.ixora.io)

```{code-cell} ipython3
def setup():
    size(500, 500, P3D)
```

```{code-cell} ipython3
def draw():
    translate(250, 250, 0)
    background(255)
    rotate_y(mouse_x / 4.0) # 22.5 graus
    for x in range(-100, 101, 50):
        for y in range(-100, 101, 50):
            for z in range(-100, 101, 50):
                fill(100 + x, 100 + y, 100 + z)
                my_box(x, y, z, 25 + 25 * sin(x + y + frame_count / 20.0))
```

```{code-cell} ipython3
def my_box(x, y, z, tamanho):
    push()
    translate(x, y, z)
    box(tamanho)
    pop()
```

```{code-cell} ipython3
run_sketch()  # chama o setup() uma vez, e o draw() em repetição.

# Para ver o resultado, usando o mybinder.org o Thebe Live Code no Jupyter book
portal = py5_tools.sketch_portal(quality=75, scale=1.0)
portal
```

```{code-cell} ipython3

```
