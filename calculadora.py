import math
from flask import render_template, request

def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]
    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro: número negativo"
            etapas = f"Não existe raiz real de {num1}."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"
    elif operacao == "log":
            resultado = math.log(num1, 10)
            etapas = f"{num1} na base 10 = {resultado} pois 10 elevado a {resultado} = {num1}"
    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados="",
            )
        num2 = float(num2_valor)
        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"
        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"
        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} * {num2} = {resultado}"
        elif operacao == "/":
            if num2 == 0:
                etapas = "Impossivel dividir um  numero por 0"
                resultado = "Erro: Divisão por 0"
            else:
                resultado = num1 / num2
                etapas = f"{num1} / {num2} = {resultado}"
        elif operacao == "**":
            resultado = num1 ** num2
            etapas = f"{num1} ** {num2} = {resultado}"
        else:
            num3 = float(request.form["num3"])
            delta = (num2 ** 2)-4*num1*num3
            if delta < 0:
                resultado = "Não possui raiz real"
                etapas = f"{num2}^2 - 4{num1}{num3}  = {delta}"
            elif delta == 0:
                x = ((num2*-1)+delta)/(2*num1)
                resultado = x
                etapas = f"- {num2} +-  √{delta} / 2{num1} = {x}"
            else:
                x1 = ((num2*-1)+math.sqrt(delta))/(2*num1)
                x2 = ((num2*-1)-math.sqrt(delta))/(2*num1)
                resultado = f"X1 = {x1} e X2 = {x2}"
                etapas = f"- {num2} +-  √{delta} / 2*{num1} = {x1} ou {x2}"
        
    return render_template(
                "calculadora.html",
                etapas=etapas,
                resultados=resultado,
            )
    
