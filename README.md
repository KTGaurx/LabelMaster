# LabelMaster

A Streamlit-based app for labeling and model management.

---

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/LabelMaster.git
cd LabelMaster
```

### 2. Install dependencies

#### Core install
```bash
pip install .
```

#### With developer tools
```bash
pip install .[dev]
```

#### With machine learning stack
```bash
pip install .[ml]
```

#### With visualization extras
```bash
pip install .[viz]
```

#### Install everything
```bash
pip install .[all]
```

---

## ▶️ Running the App

Start the Streamlit app with:

```bash
streamlit run app/streamlit_app/main.py
```

By default, the app will be available at [http://localhost:8501](http://localhost:8501).

---

## 🛠 Project Structure

```
LabelMaster
├── app
│   ├── api              # REST or internal API endpoints
│   ├── config           # Settings, environment variables, constants
│   ├── core             # Business logic, utilities, services
│   ├── infra            # Infrastructure integrations (DB, storage, logging, auth)
│   └── streamlit_app    # Streamlit-specific code
│       ├── components   # Reusable UI components/widgets
│       └── pages        # Streamlit pages
├── docker               # Dockerfiles, compose, and related scripts
├── models               # Trained ML models, weights, preprocessing
└── tests                # Unit/integration tests
```

---

## 🧪 Development

Run tests with:
```bash
pytest
```

Format code with:
```bash
black .
isort .
```

Lint with:
```bash
pylint app
```

---

## 📜 License
MIT License. See [LICENSE](LICENSE) for details.
