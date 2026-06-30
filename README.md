# 🛍️ AI-Powered Fashion Product Intelligence System

An AI-powered fashion product intelligence system built using the **OpenAI CLIP** model. This project helps improve the online shopping experience by recommending related products, creating a clean product catalog, and allowing users to search products using simple text descriptions.

---

# 📖 About the Project

Online shopping platforms contain thousands of fashion products uploaded by different sellers. Customers often find it difficult to discover related products, duplicate products make the catalog confusing, and normal keyword search does not always return the best results.

To solve these problems, this project uses the **OpenAI CLIP** model, which understands both images and text. The project is divided into three main tasks that work together to make product discovery faster, smarter, and more user-friendly.

---

# ✨ Features

### 🛒 Task 1 – Smart Product Recommendation Engine

* Recommends products based on visual similarity.
* Suggests complementary products using product information.
* Displays recommended product images.

---

### 📦 Task 2 – Unique Product Catalog Creation

* Identifies similar or duplicate products.
* Groups similar products into a single catalog.
* Selects one representative product for each group.
* Creates a clean and organized product catalog.

---

### 🔍 Task 3 – Reverse Product Search

* Allows users to search products using text.
* Understands natural language queries like:

  * *Blue Casual Shirt*
  * *Red Running Shoes*
  * *Black Backpack*
* Displays the most relevant matching products with images.

---

# ⚙️ Technologies Used

* Python
* OpenAI CLIP
* PyTorch
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Pillow (PIL)
* Kaggle Notebook

---

# 🚀 How It Works

### Task 1

* Load the fashion dataset.
* Generate CLIP embeddings for all product images.
* Compare image embeddings using cosine similarity.
* Recommend visually similar and complementary products.

---

### Task 2

* Reuse the CLIP embeddings generated in Task 1.
* Compare similar products using cosine similarity.
* Group duplicate products together.
* Keep one representative product for each unique group.
* Build a clean product catalog.

---

### Task 3

* Accept a text query from the user.
* Convert the text into a CLIP text embedding.
* Compare it with all image embeddings.
* Display the most relevant products.

---

# 📂 Project Structure

```text
AI-Fashion-Product-Intelligence/
│
├── Dataset/
├── Notebook.ipynb
├── Outputs/
├── README.md
└── requirements.txt
```

---

# 📸 Sample Inputs

### Task 1

**Input**

```
Running Shoe
```

**Output**

```
Sports Socks
Fitness Watch
Water Bottle
Sports T-Shirt
```

---

### Task 2

**Input**

```
Blue Shirt A
Blue Shirt B
Blue Shirt C
```

**Output**

```
Catalog Name:
Blue Shirts

Representative Product:
Blue Casual Shirt

Similar Products:
Blue Checked Shirt
Slim Fit Blue Shirt
Blue Cotton Shirt
```

---

### Task 3

**Input**

```
Blue Casual Shirt
```

**Output**

```
1. Men's Blue Casual Shirt
2. Blue Checked Shirt
3. Slim Fit Blue Shirt
4. Blue Cotton Shirt
5. Casual Blue Shirt

```

📸 Output Images
<img width="620" height="287" alt="Screenshot 2026-06-29 161711" src="https://github.com/user-attachments/assets/9b3a3743-3828-4ce4-a250-4b6dcff679cf" />
<img width="738" height="338" alt="Screenshot 2026-06-29 161736" src="https://github.com/user-attachments/assets/9f58b407-17be-4a95-9d7a-5bd7d6e67a48" />
<img width="674" height="224" alt="Screenshot 2026-06-29 161755" src="https://github.com/user-attachments/assets/7337a35e-dddb-41f4-aacc-8ee7bfc2374e" />
<img width="681" height="236" alt="Screenshot 2026-06-29 161803" src="https://github.com/user-attachments/assets/dd522ba4-7f91-42f5-966a-5c0303ca48e9" />

---

# 💡 Future Improvements

* Build a web application using Streamlit.
* Add image upload for product search.
* Use a vector database like FAISS for faster search.
* Improve recommendations using customer purchase history.
* Deploy the project online.

---

# 👨‍💻 Author

**Srikara Karthikeya**

B.Tech – Computer Science Engineering (AI & ML)

---

⭐ *If you found this project useful, feel free to give it a star on GitHub!*
