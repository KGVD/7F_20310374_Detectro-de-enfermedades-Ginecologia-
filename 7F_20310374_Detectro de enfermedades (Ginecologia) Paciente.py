# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 03:11:38 2023

@author: LoboM
"""
import json

class Sintomas:
    def __init__(self, Enfermedad, Sintoma1, Sintoma2, Sintoma3, Sintoma4, Sintoma5, Sintoma6, Sintoma7, Sintoma8, Sintoma9, Sintoma10, Sintoma11, Sintoma12, Sintoma13, Sintoma14, Sintoma15, Sintoma16):
        self.Enfermedad = Enfermedad
        self.Sintoma1 = Sintoma1
        self.Sintoma2 = Sintoma2
        self.Sintoma3 = Sintoma3
        self.Sintoma4 = Sintoma4
        self.Sintoma5 = Sintoma5
        self.Sintoma6 = Sintoma6
        self.Sintoma7 = Sintoma7
        self.Sintoma8 = Sintoma8
        self.Sintoma9 = Sintoma9
        self.Sintoma10 = Sintoma10
        self.Sintoma11 = Sintoma11
        self.Sintoma12 = Sintoma12
        self.Sintoma13 = Sintoma13
        self.Sintoma14 = Sintoma14
        self.Sintoma15 = Sintoma15
        self.Sintoma16 = Sintoma16

def load_Enfermedades(filename):
    Enfermedades = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                sintomas_dict = json.loads(line)
                Enfermedades.append(Sintomas(**sintomas_dict))
    except FileNotFoundError:
        pass

    return Enfermedades

def save_Enfermedades(filename, Enfermedades):
    with open(filename, 'w') as file:
        for Sintomas in Enfermedades:
            sintomas_dict = {
                "Enfermedad": Sintomas.Enfermedad,
                "Sintoma1": Sintomas.Sintoma1,
                "Sintoma2": Sintomas.Sintoma2,
                "Sintoma3": Sintomas.Sintoma3,
                "Sintoma4": Sintomas.Sintoma4,
                "Sintoma5": Sintomas.Sintoma5,
                "Sintoma6": Sintomas.Sintoma6,
                "Sintoma7": Sintomas.Sintoma7,
                "Sintoma8": Sintomas.Sintoma8,
                "Sintoma9": Sintomas.Sintoma9,
                "Sintoma10": Sintomas.Sintoma10,
                "Sintoma11": Sintomas.Sintoma11,
                "Sintoma12": Sintomas.Sintoma12,
                "Sintoma13": Sintomas.Sintoma13,
                "Sintoma14": Sintomas.Sintoma14,
                "Sintoma15": Sintomas.Sintoma15,
                "Sintoma16": Sintomas.Sintoma16
            }
            file.write(json.dumps(sintomas_dict) + '\n')
            
def guess_Enfermedades(user_input, Enfermedades):
    for Sintomas in Enfermedades:
        match = all(
            str(getattr(Sintomas, f"Sintoma{i}")) == user_input[f"Sintoma{i}"] or user_input[f"Sintoma{i}"] == "3"
            for i in range(1, 17)
        )
        if match:
            return Sintomas
    return None

def Main():
    Enfermedades = load_Enfermedades('Doctor.txt')

    print("Bienvenido al consultorio clínico de ginecología\n\nPara agilizar la diagnósticación se le pide que ingrese los síntomas, oh si desea un chequeo físico pase con la secretaria\n1.-Ingresar Síntomas\n2.-Chequeo Médico")
    Eleccion = int(input())

    if Eleccion == 1:
        while True:
            print("\nIniciaremos con un grupo de preguntas para hacer el diagnóstico")
            
            Sintoma1 = input("¿Ha experimentado un sangrado anormal por los genitales?\n1.-Si\n2.-No\n3.-Lo experimenté hace tiempo\nR:").strip()
            Sintoma2 = input("¿Ha experimentado una presión en el área pélvica?\n1.-Si\n2.-No\n3.-Lo experimenté hace tiempo\nR:").strip()
            Sintoma3 = input("¿Ha experimentado dificultades al querer quedar embarazada?\n1.-Si\n2.-No\nR:").strip()
            Sintoma4 = input("¿Ha experimentado flujo de sangrado alto durante la menstruación?\n1.-Si\n2.-No\n3.-Lo experimenté hace tiempo\nR:").strip()
            Sintoma5 = input("¿Ha experimentado alguna sensación de distensión (hinchazón o sensación de llenura en el abdomen)?\n1.-Si\n2.-No\n3.-Lo experimenté hace tiempo\nR:").strip()
            Sintoma6 = input("¿Ha experimentado de Menstruación irregular?\n1.-Si\n2.-No\n3.-Lo experimenté hace tiempo\nR:").strip()
            Sintoma7 = input("¿Ha experimentado Dificultades para retener la orina?\n1.-Si\n2.-No\nR:").strip()
            Sintoma8 = input("¿Ha sentido oh visto de hernias (bultos) por la zona genital?\n1.-Si\n2.-No\nR:").strip()
            Sintoma9 = input("¿Ha experimentado dolor al realizar acciones como orinar o tener relaciones sexuales?\n1.-Si\n2.-No\nR:").strip()
            Sintoma10 = input("¿Ha visto algún tipo de secreción anormal de sus genitales (color extraño, viscosidad dudosa, etc)?\n1.-Si\n2.-No\nR:").strip()
            Sintoma11 = input("¿Ha experimentado algún tipo de picazón o ardor en su zona genital?\n1.-Si\n2.-No\n3.-Lo experimenté hace tiempo\nR:").strip()
            Sintoma12 = input("¿Se ha enfermado mucho últimamente?\n1.-Si\n2.-No\nR:").strip()
            Sintoma13 = input("¿Ha experimentado cansancio o fatiga?\n1.-Si\n2.-No\n3.-Lo experimenté hace tiempo\nR:").strip()
            Sintoma14 = input("¿Ha experimentado una pérdida de peso inexplicable?\n1.-Si\n2.-No\nR:").strip()
            Sintoma15 = input("¿Ha sentido oh visto llagas indoloras en su cuerpo?\n1.-Si\n2.-NoR:").strip()
            Sintoma16 = input("¿Ha sufrido de una inflamación en los ganglios (estructura en forma de frijol, puede sentir unos en la zona posterior de su cuello)?\n1.-Si\n2.-No\nR:").strip()
        
            user_input = {
                "Sintoma1": Sintoma1,
                "Sintoma2": Sintoma2,
                "Sintoma3": Sintoma3,
                "Sintoma4": Sintoma4,
                "Sintoma5": Sintoma5,
                "Sintoma6": Sintoma6,
                "Sintoma7": Sintoma7,
                "Sintoma8": Sintoma8,
                "Sintoma9": Sintoma9,
                "Sintoma10": Sintoma10,
                "Sintoma11": Sintoma11,
                "Sintoma12": Sintoma12,
                "Sintoma13": Sintoma13,
                "Sintoma14": Sintoma14,
                "Sintoma15": Sintoma15,
                "Sintoma16": Sintoma16,
            }

            guessed_Sintomas = guess_Enfermedades(user_input, Enfermedades)

            if guessed_Sintomas:
                print(f"\n\nPor los datos proporcionados, usted padece de:\n{guessed_Sintomas.Enfermedad} ")
            else:
                print("\n\nPerdone, parece ser que los sintomas puestos no concuerdan con ninguna enfermedad en mi base de datos, porfavor pase con el medico y comentele la situacion para que la atienda y de paso mi base de datos ea actualizada\nPerdone las molestias, Que tenga buen dia1")
                
            break
        
    if Eleccion == 2:
            print("\n\nMuy bien, por favor pase con la secretaria para que le toma presion sanguinea y peso, que tenga buen dia")

if __name__ == "__main__":
    Main()   

