```markdown
# 🍽️ Restaurant Name & Menu Generator

A fun, AI-powered app that generates **unique restaurant names** and curated menu items for any cuisine you choose! Built with **Streamlit**, **LangChain**, and **OpenAI**, this project is perfect for entrepreneurs, hobbyists, and anyone dreaming up their next food venture.

---

## 🚀 Features

- **Automatic Name Generation**: Instantly get a creative, fancy name for your restaurant based on the selected cuisine.
- **Menu Suggestions**: AI-curated menu items tailored to your restaurant’s theme.
- **Streamlit UI**: Interactive web app with sidebar controls for easy cuisine selection.
- **Custom Cuisine Input**: Don’t see your preferred cuisine? Type your own for personalized results.
- **Modern Styling**: Clean, colorful layout for an engaging UX.

---

## 🛠️ Tech Stack

- **LangChain** (`llms`, `prompts`, `chains`, `community`)
- **OpenAI** (LLM for creative output)
- **Streamlit** (for quick interactive web apps)
- **dotenv** (manage API keys securely)

---

## ⚡ How It Works

1. **Select or Enter a Cuisine** in the sidebar.
2. **Click "Generate Restaurant"**.
3. The app uses a **LangChain SequentialChain** to:
   - Generate a creative restaurant name.
   - Suggest a comma-separated menu for that theme.
4. Instantly see the AI-generated restaurant and menu!

---

## 🧑‍💻 Quickstart

**1. Install dependencies:**
```
pip install openai langchain langchain-community langchain-chains streamlit python-dotenv
```

**2. Set up your OpenAI API key:**
Create a `.env` file in your project:
```
OPENAI_API_KEY=your_openai_key_here
```

**3. Run the app:**
```
streamlit run app.py
```
*(Make sure your helper functions are in `langchain_helper.py` as per the main code.)*

---

## 📦 File Structure

```
├── app.py                 # Main Streamlit UI
├── langchain_helper.py    # Contains `generate_restaurant_name_and_items()`
├── .env.example           # Environment variable template
```

---

## 🎨 Sample Output

```
Cuisine: Italian

Restaurant Name: La Bella Tavola

Menu Items:
- Truffle Risotto
- Sicilian Caponata
- Burrata Caprese Salad
- Gnocchi all’Amatriciana
- Pistachio Tiramisu
```

```
