# 📝 DailyJournalPy

![Python](https://img.shields.io/badge/python-3.10+-blue?logo=python) ![License](https://img.shields.io/badge/license-MIT-green)

**DailyJournalPy** é um aplicativo simples em Python para criar e organizar anotações diárias. Ele cria automaticamente uma estrutura de pastas organizada por **ano, mês e dia**, e salva suas notas em arquivos `.md` (Markdown).

---

## ✨ Funcionalidades

- Criar anotações diárias de forma rápida.
- Estrutura de pastas automática:
DailyJournalPy/
└── 2025/
└── Agosto/
└── 22/
└── nota.md
- Salvar as anotações em **Markdown** para fácil leitura e edição.
- Personalizar nomes das pastas.
- Organização simples e escalável sem banco de dados.

---

## 🛠 Tecnologias

- Python 3.10+
- Biblioteca `os` (manipulação de arquivos e pastas)
- `datetime` (manipulação de datas)

---

## 📁 Estrutura do projeto
diario/
│── main.py # Script principal
│── storage/
│ └── file_manager.py # Funções para criar pastas e salvar notas
│── utils/
│ └── date_utils.py # Funções auxiliares para datas
│── settings/ # Configurações futuras do app

---

## 🚀 Como usar

### 1️⃣ Criar ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
python main.py

3️⃣ Passos no app
Digite a data da anotação no formato AAAA-MM-DD.
Digite sua anotação.
A pasta e o arquivo .md serão criados automaticamente.

🔧 Como contribuir
Crie uma branch de feature:
```git checkout -b feature/nome-da-feature```
```git push origin feature/nome-da-feature```


