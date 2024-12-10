import streamlit as st
import base64

st.set_page_config(page_title="Educação em Cibersegurança", layout="wide")

query_params = st.query_params
if "home" in query_params:
    st.session_state['pagina_atual'] = "Home"

if 'module1_completed' not in st.session_state:
    st.session_state['module1_completed'] = False

if 'module2_completed' not in st.session_state:
    st.session_state['module2_completed'] = False

if 'pagina_atual' not in st.session_state:
    st.session_state['pagina_atual'] = "Home"


def checar_quiz(respostas_certas, respostas_usuario):
    acertos = 0
    for correta, usuario in zip(respostas_certas, respostas_usuario):
        if usuario == correta:
            acertos += 1
    return acertos, (acertos / len(respostas_certas)) * 100


num_modulos = 2
completados = sum([
    st.session_state['module1_completed'],
    st.session_state['module2_completed']
])
progresso = (completados / num_modulos) * 100

with open("Logo.png", "rb") as img_file:
    img_data = img_file.read()
img_base64 = base64.b64encode(img_data).decode()

st.sidebar.markdown(
    f"""
    <a href="?home=true" target="_self">
    <img src="data:image/png;base64,{img_base64}" style="max-width:100%; margin-bottom:20px; border-radius:8px;"/>
    </a>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("Módulos")

# CSS para estilos gerais
st.markdown("""
<style>
.stButton>button {
    border-radius: 5px;
    background-color: #e9ecef;
    color: #333;
    border: 1px solid #ccc;
    padding: 0.5em 1em;
    margin-top: 0.5em;
    font-size: 0.95em;
    transition: background-color 0.2s ease, border-color 0.2s ease;
}
.stButton>button:hover {
    background-color: #dee2e6;
    border-color: #bbb;
}

/* Quiz button styles */
.quiz-btn {
    background: #f8f9fa;
    color: #333;
    border: 1px solid #ccc;
    padding: 0.6em;
    border-radius: 4px;
    font-size: 1em;
    cursor: pointer;
    transition: background-color 0.2s ease, border-color 0.2s ease;
    text-align: center;
    margin: 0.5em;
    width: 200px;
    box-sizing: border-box;
    white-space: normal;
}

.quiz-btn:hover {
    background-color: #e9ecef;
    border-color: #bbb;
}

.quiz-btn.selected {
    background-color: #d4edda;
    border-color: #c3e6cb;
    font-weight: bold;
    color: #155724;
}

/* Quiz question style */
.quiz-question {
    margin-bottom: 1em;
    font-weight: bold;
    color: #00695C;
    font-size: 1.3em;
    margin-top: 1.5em;
    font-family: Arial, sans-serif;
}

/* Container for quiz */
.quiz-container {
    margin-top: 2em;
    margin-bottom: 2em;
    max-width: 900px;
}

.quiz-options-container {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 1em;
    align-items: flex-start;
}

/* Send button */
.send-button-container {
    text-align: center;
    margin-top: 2em;
}

.send-button-container button {
    background-color: #00695C;
    color: #fff;
    border: none;
    padding: 0.7em 1.5em;
    font-size: 1em;
    border-radius: 5px;
    cursor: pointer;
}

.send-button-container button:hover {
    background-color: #005f54;
}

/* Título dos módulos */
.module-title {
    text-align: center;
    font-size: 2em;
    color: #00695C;
    font-weight: bold;
    margin-bottom: 1.2em;
    font-family: Arial, sans-serif;
    position: relative;
    margin-top: 0.5em;
}

.module-title::after {
    content: "";
    display: block;
    width: 100px;
    height: 4px;
    background: #80cbc4;
    margin: 0.5em auto 0;
    border-radius: 2px;
}

/* Frase abaixo do video */
.after-video-text {
    text-align: center;
    font-size: 1.15em;
    color: #444;
    margin-top: 1.5em;
    margin-bottom: 2em;
    font-family: Arial, sans-serif;
}

/* Container para centralizar o iframe */
.video-container {
    text-align: center; 
    margin-bottom: 2em; 
}
</style>
""", unsafe_allow_html=True)

if st.sidebar.button("🎣 Módulo 1: Phishing"):
    st.session_state['pagina_atual'] = "Módulo 1: Introdução ao Phishing"

if st.sidebar.button("🔐 Módulo 2: Senhas"):
    st.session_state['pagina_atual'] = "Módulo 2: Senhas Seguras"

st.sidebar.markdown("---")
st.sidebar.write("<b>Progresso Geral:</b>", unsafe_allow_html=True)
st.sidebar.progress(int(progresso))

if completados == 0:
    st.sidebar.write("Você completou 0 de 2 módulos.")
elif completados == 1:
    st.sidebar.write("Você completou 1 de 2 módulos.")
else:
    st.sidebar.write("Você completou todos os módulos! 🎉")

pagina_selecionada = st.session_state['pagina_atual']

if pagina_selecionada == "Home":
    home_html = f"""
    <html>
    <head>
    <style>
    body {{
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
        background: #ffffff;
    }}
    .card {{
        background: #ffffff;
        border-radius: 10px;
        width: 90vw;
        padding: 3em;
        margin: 3em auto;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        color: #333;
    }}
    .title {{
        font-size: 2.2em;
        color: #00695C;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1.2em;
        font-family: Arial, sans-serif;
    }}
    .title::after {{
        content: "";
        display: block;
        width: 80px;
        height: 4px;
        background: #80cbc4;
        margin: 0.7em auto 0;
        border-radius: 2px;
    }}
    .highlight {{
        color: #00695C;
        font-weight: bold;
    }}
    .line {{
        margin-bottom: 1.3em;
        font-size: 1.15em;
        line-height: 1.7;
        color: #444;
    }}
    .line strong {{
        color: #00695C;
    }}
    .steps {{
        margin-top: 1em;
        margin-bottom: 1.5em;
    }}
    .steps div {{
        margin-bottom: 0.8em;
        font-size: 1.05em;
    }}
    .emoji {{
        font-size: 1.2em;
        margin-right: 0.4em;
        vertical-align: middle;
    }}
    </style>
    </head>
    <body>
        <div class="card">
            <div class="title">🚀 Bem-vindo(a) ao Curso de Educação em Cibersegurança! 🚀</div>

            <div class="line">
                Este aplicativo foi desenvolvido para ajudá-lo(a) a aprender sobre conceitos importantes de 
                <span class="highlight">cibersegurança</span> de forma interativa e gamificada.
            </div>

            <div class="line"><strong>Como funciona:</strong></div>
            <div class="steps">
                <div><span class="emoji">👉</span>Selecione o primeiro módulo na barra lateral.</div>
                <div><span class="emoji">🎬</span>Assista ao vídeo educativo.</div>
                <div><span class="emoji">❓</span>Responda ao quiz de múltipla escolha sobre o conteúdo, sem respostas pré-selecionadas.</div>
                <div><span class="emoji">🏆</span>Obtenha pelo menos 70% de acertos no quiz para ter seu progresso reconhecido.</div>
            </div>

            <div class="line"><strong>Progresso:</strong></div>
            <div class="line">
                À medida que você conclui um módulo com sucesso, o progresso aumenta.<br>
                Conclua todos para atingir 100%.
            </div>

            <div class="line" style="text-align:center; font-size:1.15em;">
                Clique em "<span class="highlight">🎣 Módulo 1: Phishing</span>" na barra lateral para começar!
            </div>
        </div>
    </body>
    </html>
    """

    st.components.v1.html(home_html, height=900, scrolling=False)

elif pagina_selecionada == "Módulo 1: Introdução ao Phishing":
    st.markdown("<div class='module-title'>🎣 Módulo 1: Introdução ao Phishing</div>", unsafe_allow_html=True)

    # Insira o iframe manualmente definindo o width e height desejado
    st.markdown("""
    <div class="video-container">
        <iframe width="1000" height="600" src="https://www.youtube.com/embed/eFwSHxWyOp0" frameborder="0" allowfullscreen></iframe>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='after-video-text'>Depois de assistir ao vídeo, responda ao quiz abaixo:</div>", unsafe_allow_html=True)

    perguntas_modulo1 = [
        "1) O que é phishing?",
        "2) Qual o principal objetivo de um ataque de phishing?",
        "3) Qual dessas é uma boa prática para evitar cair em phishing?"
    ]

    opcoes_modulo1 = [
        ["Um ataque de hardware", "Um tipo de ataque de engenharia social", "Um antivírus", "Uma ferramenta de segurança"],
        ["Roubar dados pessoais", "Melhorar a velocidade da conexão", "Proteger o usuário", "Corrigir falhas de software"],
        ["Clicar em todos os links sem verificar", "Fornecer dados de login sem pensar", "Verificar o remetente do email e desconfiar de anexos suspeitos", "Ignorar completamente todas as mensagens recebidas"]
    ]

    respostas_corretas_mod1 = [
        "Um tipo de ataque de engenharia social",
        "Roubar dados pessoais",
        "Verificar o remetente do email e desconfiar de anexos suspeitos"
    ]

    if 'respostas_mod1' not in st.session_state:
        st.session_state['respostas_mod1'] = [None] * len(perguntas_modulo1)

    st.markdown("<div class='quiz-container'>", unsafe_allow_html=True)
    for i, pergunta in enumerate(perguntas_modulo1):
        st.markdown(f"<div class='quiz-question'>{pergunta}</div>", unsafe_allow_html=True)
        st.markdown("<div class='quiz-options-container'>", unsafe_allow_html=True)
        for op in opcoes_modulo1[i]:
            if st.button(op, key=f"mod1_q{i}_op{op}"):
                st.session_state['respostas_mod1'][i] = op
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='send-button-container'>", unsafe_allow_html=True)
    if st.button("Enviar Respostas do Módulo 1"):
        if any(r is None for r in st.session_state['respostas_mod1']):
            st.error("Por favor, selecione uma resposta para todas as perguntas antes de enviar.")
        else:
            acertos, porcentagem = checar_quiz(respostas_corretas_mod1, st.session_state['respostas_mod1'])
            st.write(f"Você acertou {acertos} de {len(perguntas_modulo1)} perguntas. ({porcentagem:.2f}%)")
            if porcentagem >= 70:
                st.success("Parabéns! Você concluiu o Módulo 1 com sucesso.")
                st.session_state['module1_completed'] = True
                st.info("Agora você já pode tentar o Módulo 2!")
            else:
                st.error("Você não atingiu a pontuação necessária. Por favor, revise o conteúdo e tente novamente.")
    st.markdown("</div>", unsafe_allow_html=True)

elif pagina_selecionada == "Módulo 2: Senhas Seguras":
    if not st.session_state['module1_completed']:
        st.error("Você precisa concluir o Módulo 1 primeiro para acessar o Módulo 2.")
    else:
        st.markdown("<div class='module-title'>🔐 Módulo 2: Senhas Seguras</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="video-container">
            <iframe width="1000" height="600" src="https://youtu.be/hWC5EBKQoUs" frameborder="0" allowfullscreen></iframe>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div class='after-video-text'>Depois de assistir ao vídeo, responda ao quiz abaixo:</div>", unsafe_allow_html=True)

        perguntas_modulo2 = [
            "1) Qual característica é importante em uma senha segura?",
            "2) É recomendado usar a mesma senha para todos os serviços?",
            "3) Qual ferramenta pode ajudar na gestão segura de múltiplas senhas?"
        ]

        opcoes_modulo2 = [
            ["Ser curta, com menos de 4 caracteres", "Incluir caracteres especiais, números e letras maiúsculas e minúsculas", "Ser apenas números", "Ser apenas letras"],
            ["Sim, para facilitar a memorização", "Não, pois isso aumenta o risco de violação", "Sim, se a senha for muito forte", "Não há problema desde que o serviço seja seguro"],
            ["Armazenar todas as senhas em um bloco de notas", "Um gerenciador de senhas", "Memorizar todas as senhas de cabeça", "Enviar as senhas por email para si mesmo"]
        ]

        respostas_corretas_mod2 = [
            "Incluir caracteres especiais, números e letras maiúsculas e minúsculas",
            "Não, pois isso aumenta o risco de violação",
            "Um gerenciador de senhas"
        ]

        if 'respostas_mod2' not in st.session_state:
            st.session_state['respostas_mod2'] = [None] * len(perguntas_modulo2)

        st.markdown("<div class='quiz-container'>", unsafe_allow_html=True)
        for i, pergunta in enumerate(perguntas_modulo2):
            st.markdown(f"<div class='quiz-question'>{pergunta}</div>", unsafe_allow_html=True)
            st.markdown("<div class='quiz-options-container'>", unsafe_allow_html=True)
            for op in opcoes_modulo2[i]:
                if st.button(op, key=f"mod2_q{i}_op{op}"):
                    st.session_state['respostas_mod2'][i] = op
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='send-button-container'>", unsafe_allow_html=True)
        if st.button("Enviar Respostas do Módulo 2"):
            if any(r is None for r in st.session_state['respostas_mod2']):
                st.error("Por favor, selecione uma resposta para todas as perguntas antes de enviar.")
            else:
                acertos, porcentagem = checar_quiz(respostas_corretas_mod2, st.session_state['respostas_mod2'])
                st.write(f"Você acertou {acertos} de {len(perguntas_modulo2)} perguntas. ({porcentagem:.2f}%)")
                if porcentagem >= 70:
                    st.success("Parabéns! Você concluiu o Módulo 2 com sucesso.")
                    st.session_state['module2_completed'] = True
                    st.balloons()
                    st.info("Você concluiu todos os módulos disponíveis! Obrigado por participar.")
                else:
                    st.error("Você não atingiu a pontuação necessária. Por favor, tente novamente.")
        st.markdown("</div>", unsafe_allow_html=True)
