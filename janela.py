import customtkinter as tk

# Configurações iniciais do CustomTkinter
tk.set_appearance_mode("dark")  # "Light", "Dark", "System"
tk.set_default_color_theme("dark-blue")  # Themes: "blue", "green", "dark-blue", "light-blue", "dark-green" 
 
# Criação da janela principal 
janela = tk.CTk()   
janela.title("Janela de Login")
janela.geometry("500x300")

def validar_login():
    usuario = email.get()  # Obtém o valor do campo de email
    senha_usuario = senha.get()  # Obtém o valor do campo de senha
    
    if usuario == "Usuario@gmail.com" and senha_usuario == "123456":  # Validação simples
        resultado.configure(text="Login realizado com sucesso!", fg_color="green") # Exibe mensagem de sucesso
    elif usuario != "Usuario@gmail.com" or senha_usuario != "123456":  # Validação de usuário e senha diferente 
        resultado.configure(text="E-mail ou senha incorreta.", fg_color="red")    

# Criação dos campos de entrada e botões
texto = tk.CTkLabel(janela, text="Usuário") # Label para o campo de usuário
texto.pack(pady=10, padx=10) 

email = tk.CTkEntry(janela, placeholder_text="Digite seu email") # Label para o campo de email
email.pack(pady=10, padx=10) 

senha = tk.CTkEntry(janela, placeholder_text="Digite sua senha", show="*") # Label para o campo de senha
senha.pack(pady=10, padx=10)

checkbox = tk.CTkCheckBox(janela, text="Lembrar Login") # Checkbox para lembrar o login
checkbox.pack(pady=10, padx=10), 

botao = tk.CTkButton(janela, text="Login", command=validar_login) # Botão de login
botao.pack(pady=10, padx=10)

resultado = tk.CTkLabel(janela, text="")  # Label para exibir o resultado do login
resultado.pack(pady=10, padx=10)

janela.mainloop()








