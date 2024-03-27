import tkinter as tk

def calcular():
    try:
        # Obter os valores dos campos de entrada e converter para float
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        # Realizar a operação selecionada
        if operacao.get() == "+":
            resultado = num1 + num2
        elif operacao.get() == "-":
            resultado = num1 - num2
        elif operacao.get() == "*":
            resultado = num1 * num2
        elif operacao.get() == "/":
            resultado = num1 / num2

        # Atualizar o rótulo com o resultado
        label_resultado.config(text="Resultado: " + str(resultado))
    except ValueError:
        label_resultado.config(text="Erro: Insira números válidos")

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Criar os campos de entrada
entry_num1 = tk.Entry(janela)
entry_num1.pack()

entry_num2 = tk.Entry(janela)
entry_num2.pack()

# Criar os botões de operação
operacao = tk.StringVar()
operacao.set("+")

add_button = tk.Radiobutton(janela, text="+", variable=operacao, value="+")
add_button.pack()

subtract_button = tk.Radiobutton(janela, text="-", variable=operacao, value="-")
subtract_button.pack()

multiply_button = tk.Radiobutton(janela, text="*", variable=operacao, value="*")
multiply_button.pack()

divide_button = tk.Radiobutton(janela, text="/", variable=operacao, value="/")
divide_button.pack()

# Criar o botão de calcular
calcular_button = tk.Button(janela, text="Calcular", command=calcular)
calcular_button.pack()

# Criar o rótulo para exibir o resultado
label_resultado = tk.Label(janela, text="")
label_resultado.pack()

# Iniciar o loop de eventos da janela
janela.mainloop()