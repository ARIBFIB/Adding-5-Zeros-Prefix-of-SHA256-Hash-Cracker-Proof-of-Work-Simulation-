# 🔐 Adding 5-Zeros Prefix of SHA-256 Hash Cracker (Proof-of-Work Simulation)

A Python-based proof-of-work simulator that uses SHA-256 hashing to find a nonce (number) such that the resulting hash begins with **five leading zeros**. This mimics the mining process used in blockchain technology to validate data blocks.

---

## 📸 Screenshots

### ✅ Successful Hash Found

![Found Hash](https://github.com/user-attachments/assets/f6a6e702-9c06-497f-929a-466ae09e2c3a)

### 🧠 Sample Hash Visualization (via Online Tool)

![SHA256 Tool](https://github.com/user-attachments/assets/b766ade0-e8ee-4bcf-a202-283dce233da7)

---

## 💡 What is Proof-of-Work?

Proof-of-work is a consensus mechanism used in blockchain systems like Bitcoin. It requires participants (miners) to solve a computational puzzle. This puzzle involves finding a number (called a **nonce**) that, when hashed along with other data, produces a hash that meets specific criteria — such as starting with a certain number of zeros.

---

## 🛠️ How It Works

1. A long and random `prefix` string is defined.
2. A counter `i` (nonce) is initialized to 0.
3. In a loop:
    - `prefix + i` is hashed using SHA-256.
    - If the hash begins with `"00000"`, it's accepted.
    - Otherwise, the counter increments and the loop continues.
4. Once found, the input and its matching hash are printed.

---

## 🧪 Example Code

```python
import hashlib

prefix = "Abdul Rehman Irfan Saima 2000 Saima Ali 100 Saqib Saqib 1500 Sara Sara This is me and tell me oajiodachpiahcpoasjpoaskdpojaspodjaspodjaspodjaspodjaspodjpoaskdpoaskdpasodkaspojdpociasjpocasjdhello text send block chain"

i = 0

while True:
    text = f"{prefix}{i}"
    hash_result = hashlib.sha256(text.encode()).hexdigest()
    if hash_result.startswith("00000"):
        print(f"Found! Input: {text} → Hash: {hash_result}")
        break
    i += 1
