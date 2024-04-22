import random
import tkinter as tk

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

# Criando o menu principal
root = tk.Tk()
root.title("Gerador de CPF")

# # Cria um campo para exibir o CPF
# entry_label = tk.Label(root, text="Number of CPFs to generate:")
# entry_label.pack()
# entry = tk.Entry(root)
# entry.pack()

# Criando o botão pra gerar CPF
generate_button = tk.Button(root, text="Gerar", command=generate_cpf)
generate_button.pack()

# Gerar o resultado
result_label = tk.Label(root, text="")
result_label.pack()

# Refaz o processo do zero
root.mainloop()