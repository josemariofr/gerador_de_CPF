import random
import tkinter as tk
import pyperclip

cpf_history = []

def generate_cpf():
    # Gerando os primeiros 9 dígitos do CPF
    cpf = [random.randint(0, 9) for _ in range(9)]

    # Calcula o primeiro dígito verificador
    sum = 0
    for i in range(10, 1, -1):
        if i - 1 < 0 or i - 1 >= len(cpf):
            continue
        sum += cpf[i - 1] * i
    digit1 = (11 - (sum % 11)) % 11
    cpf.append(digit1)

    # Calcula o segundo dígito verificador
    sum = 0
    for i in range(11, 1, -1):
        if i - 1 < 0 or i - 1 >= len(cpf):
            continue
        sum += cpf[i - 1] * i
    digit2 = (11 - (sum % 11)) % 11
    cpf.append(digit2)

    # Formata a string do CPF
    cpf_str = "".join(str(digit) for digit in cpf)
    cpf_str = "{}.{}.{}-{}".format(cpf_str[:3], cpf_str[3:6], cpf_str[6:9], cpf_str[9:])

    # Interface gráfica do CPF
    result_label.config(text=cpf_str)
    pyperclip.copy(cpf_str)  # Copy the generated CPF to the clipboard

    # Adicionando histórico dos CPF´s gerados
    cpf_history.append(cpf_str)

def show_cpf_history():
    # Display do histórico
    history_window = tk.Toplevel(root)
    history_window.title("Histórico de CPFs")

    history_label = tk.Label(history_window, text="\n".join(cpf_history))
    history_label.pack()

# Criando o menu principal
root = tk.Tk()
root.title("Gerador de CPF")

# Criando o botão pra gerar CPF
generate_button = tk.Button(root, text="Gerar", command=generate_cpf)
generate_button.pack()

# Criando o botão pra copiar o CPF
copy_button = tk.Button(root, text="Copiar", command=lambda: pyperclip.copy(result_label.cget("text")))
copy_button.pack()

# Criando o menu para exibir o histórico
menu = tk.Menu(root)
root.config(menu=menu)

history_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Histórico", menu=history_menu)
history_menu.add_command(label="Exibir histórico", command=show_cpf_history)

# Gerar o resultado
result_label = tk.Label(root, text="")
result_label.pack()

# Refaz o processo do zero
root.mainloop()