# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18KS_Tp23onpqjpCyXkog_8JB_rAaspe1
"""

pip install rx

# Lista de usuarios conectados
usuarios_conectados = []

def new_user_notification(user):
    print(f"[Notificación] Nuevo usuario conectado: {user.upper()}")

# Simulación de usuarios conectándose (manualmente)
usuarios_conectados.append("Alpha")
new_user_notification("ALpha")

usuarios_conectados.append("Bravo")
new_user_notification("Bravo")

usuarios_conectados.append("Charlie")
new_user_notification("Charlie")