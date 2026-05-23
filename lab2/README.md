# Lab 2 - Mat ma hoc co dien, Flask API, Postman

Lab 2 tap trung vao viec cai dat cac thuat toan mat ma hoc co dien va dua chung len Flask API de test bang Postman.

## Noi dung

- Caesar cipher
- Vigenere cipher
- Rail Fence cipher
- Playfair cipher
- Transposition cipher
- Flask API
- Postman

## Cai dat

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r lab2/requirements.txt
```

## Chay API

```bash
python lab2/app.py
```

API mac dinh chay tai:

```text
http://127.0.0.1:5000
```

## Endpoint mau

- `POST /api/caesar/encrypt`
- `POST /api/caesar/decrypt`
- `POST /api/vigenere/encrypt`
- `POST /api/vigenere/decrypt`
- `POST /api/railfence/encrypt`
- `POST /api/railfence/decrypt`
- `POST /api/playfair/encrypt`
- `POST /api/playfair/decrypt`
- `POST /api/transposition/encrypt`
- `POST /api/transposition/decrypt`

## Vi du Postman

### Caesar encrypt

```json
{
  "plain_text": "HELLO",
  "key": 3
}
```

### Vigenere encrypt

```json
{
  "plain_text": "ATTACKATDAWN",
  "key": "LEMON"
}
```

### Rail Fence encrypt

```json
{
  "plain_text": "WEAREDISCOVERED",
  "key": 3
}
```

### Playfair encrypt

```json
{
  "plain_text": "HIDETHEGOLD",
  "key": "MONARCHY"
}
```

### Transposition encrypt

```json
{
  "plain_text": "HELLO WORLD",
  "key": 4
}
```
