# Importar Libreria
from flask import Flask, render_template, Response
import cv2
import mediapipe as mp

# Realizar nuestra VideoCaptura
cap = cv2.VideoCaptura(1)
