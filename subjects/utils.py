from django.db import connection
import random
import nltk
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_create():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf_8')
    buffer.close()
    return graph


def get_plot( E, M, H ,d):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5, 5))
    label= ['Easy','Medium','Hard']
    usage = [E, M, H]
    Z = range(len(label))
    plt.title('mark')
    plt.bar(Z, usage)
    plt.xticks(Z,label)
    plt.xlabel(d)
    plt.ylabel('score')
    plt.tight_layout()
    graph = get_create()
    return graph



def get_create():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf_8')
    buffer.close()
    return graph


def get_plot( E, M, H ,d):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5, 5))
    label= ['Easy','Medium','Hard']
    usage = [E, M, H]
    Z = range(len(label))
    plt.title('mark')
    plt.bar(Z, usage)
    plt.xticks(Z,label)
    plt.xlabel(d)
    plt.ylabel('score')
    plt.tight_layout()
    graph = get_create()
    return graph

