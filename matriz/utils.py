import matplotlib.pyplot as plt
import base64
from io import BytesIO


def getText(x, y):
    if 8 <= x <= 12 and 8 <= y <= 12:
        return "BAJA"
    elif 20 <= x <= 24 or 20 <= y <= 24:
        return "ALTA"
    else:
        return "MEDIA"


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()

    return graph


def get_plot(x, y):
    fig = plt.figure()
    fig.suptitle(
        f'Matriz Complejidad de Negocio vs Matriz Complejidad de Tecnología\nComplejidad {getText(x, y)}')
    plt.plot(x, y, marker="o", color="mediumspringgreen", markersize=10)
    plt.fill_between(x=[8, 12], y1=8, y2=12, color="hotpink")
    plt.fill_between(x=[12, 20], y1=8, y2=20, color="goldenrod")
    plt.fill_between(x=[8, 12], y1=12, y2=20, color="goldenrod")
    plt.fill_between(x=[20, 24], y1=8, y2=24, color="mediumblue")
    plt.fill_between(x=[8, 24], y1=20, y2=24, color="mediumblue")
    plt.xlabel('NEGOCIO')
    plt.ylabel('TECNOLÓGICA')
    plt.xlim([8, 24])
    plt.ylim([8, 24])
    texto = f"({x}, {y})"
    plt.text(x+0.2, y+0.2, texto, color="blue")

    graph = get_graph()
    return graph
