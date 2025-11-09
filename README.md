# saucedemo-selenium-tests
Automatiserade tester för inloggningsfunktionaliteten för Sauce Demo


# Sauce Demo - Selenium Test Automation Suite

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.15.2-green.svg)
![Tests](https://img.shields.io/badge/Tests-3%20Passing-brightgreen.svg)

Automatiserad testsvit för att validera inloggningsfunktionen på [Sauce Demo](https://www.saucedemo.com/) med Selenium WebDriver.

**Författare:** Adam O'Donoghue  
**GitHub:** [Adamprogramming04](https://github.com/Adamprogramming04)  
**Repository:** [saucedemo-selenium-tests](https://github.com/Adamprogramming04/saucedemo-selenium-tests)

---

## 📋 Projektöversikt

Detta projekt innehåller automatiserade testfall för inloggningsfunktionen på Sauce Demo. Testerna är byggda med Python, Selenium WebDriver och unittest-ramverket.

### Testtäckning

Testsviten innehåller **3 automatiserade testfall**:

#### ✅ GODKÄNT (G)
1. **Lyckad inloggning** - Validerar inloggning med korrekta uppgifter och verifierar redirect till startsidan

#### ✅ VÄL GODKÄNT (VG)
2. **Felaktigt användarnamn** - Validerar felhantering när felaktigt användarnamn anges
3. **Felaktigt lösenord** - Validerar felhantering när felaktigt lösenord anges

---

## 🚀 Kom igång

### Förutsättningar

- Python 3.8 eller högre
- Google Chrome webbläsare
- Git (för att klona projektet)

### Installation

**1. Klona projektet:**
```bash
git clone https://github.com/Adamprogramming04/saucedemo-selenium-tests.git
cd saucedemo-selenium-tests
```

**2. Skapa virtuell miljö (rekommenderas):**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

**3. Installera beroenden:**
```bash
pip install -r requirements.txt
```

### Kör testerna

**Kör alla tester:**
```bash
python test_login.py
```

**Kör med verbose output:**
```bash
python test_login.py -v
```

**Kör specifikt test:**
```bash
python -m unittest test_login.SauceDemoLoginTests.test_successful_login_with_valid_credentials
```

---

## 📁 Projektstruktur

```
saucedemo-selenium-tests/
│
├── test_login.py           # Huvudfil med alla testfall
├── requirements.txt        # Python-beroenden
├── README.md              # Dokumentation
└── .gitignore            # Git ignore-fil
```

---

## 🧪 Testfall i detalj

### Test 1: Lyckad inloggning (G)
**Metod:** `test_successful_login_with_valid_credentials`

**Syfte:** Verifiera att användaren kan logga in med korrekta uppgifter

**Steg:**
1. Öppna https://www.saucedemo.com/
2. Fyll i användarnamn: "standard_user"
3. Fyll i lösenord: "secret_sauce"
4. Klicka på login-knappen
5. Verifiera redirect till /inventory.html
6. Kontrollera att inventory_container är synlig

**Förväntat resultat:** Användaren loggas in och hamnar på startsidan

---

### Test 2: Felaktigt användarnamn (VG)
**Metod:** `test_login_with_invalid_username`

**Syfte:** Verifiera att felmeddelande visas vid felaktigt användarnamn

**Steg:**
1. Öppna https://www.saucedemo.com/
2. Fyll i felaktigt användarnamn
3. Fyll i korrekt lösenord
4. Klicka på login-knappen
5. Verifiera att felmeddelande visas
6. Kontrollera att användaren stannar på login-sidan

**Förväntat resultat:** Felmeddelande "Username and password do not match" visas

---

### Test 3: Felaktigt lösenord (VG)
**Metod:** `test_login_with_invalid_password`

**Syfte:** Verifiera att felmeddelande visas vid felaktigt lösenord

**Steg:**
1. Öppna https://www.saucedemo.com/
2. Fyll i korrekt användarnamn
3. Fyll i felaktigt lösenord
4. Klicka på login-knappen
5. Verifiera att felmeddelande visas
6. Kontrollera att användaren stannar på login-sidan

**Förväntat resultat:** Felmeddelande "Username and password do not match" visas

---

## 🛠️ Tekniska detaljer

### Teknologier

- **Python 3.8+** - Programmeringsspråk
- **Selenium WebDriver 4.15.2** - Webbautomatisering
- **unittest** - Testramverk
- **ChromeDriver** - WebDriver för Chrome

### Funktioner

✅ Explicit waits för pålitlig element-detektion  
✅ setUp och tearDown för ren teststruktur  
✅ Omfattande assertions för alla verifieringar  
✅ Felhantering med TimeoutException  
✅ Detaljerad loggning och utskrifter  
✅ Tydlig testdokumentation

---

## 📊 Testresultat

När alla tester passerar ser output ut så här:

```
======================================================================
STARTAR SAUCE DEMO TEST SUITE
Author: Adam O'Donoghue
GitHub: https://github.com/Adamprogramming04
======================================================================

🔵 Kör test: Lyckad inloggning med korrekta uppgifter
   ✓ Fyllde i användarnamn: standard_user
   ✓ Fyllde i lösenord
   ✓ Klickade på login-knappen
   ✓ Redirected till inventory-sidan
   ✓ Verifierade URL
   ✓ Inventory container är synlig
   ✅ TEST GODKÄNT: Lyckad inloggning

🟡 Kör test: Inloggning med felaktigt användarnamn
   ✓ Fyllde i felaktigt användarnamn
   ✓ Fyllde i korrekt lösenord
   ✓ Klickade på login-knappen
   ✓ Felmeddelande hittades
   ✓ Felmeddelande verifierat
   ✓ Användaren är kvar på login-sidan
   ✅ TEST GODKÄNT: Felmeddelande för felaktigt användarnamn

🟠 Kör test: Inloggning med felaktigt lösenord
   ✓ Fyllde i korrekt användarnamn
   ✓ Fyllde i felaktigt lösenord
   ✓ Klickade på login-knappen
   ✓ Felmeddelande hittades
   ✓ Felmeddelande verifierat
   ✓ Användaren är kvar på login-sidan
   ✅ TEST GODKÄNT: Felmeddelande för felaktigt lösenord

----------------------------------------------------------------------
Ran 3 tests in 18.456s

OK
```

---

## 📝 Licens

Detta projekt är öppen källkod och tillgängligt under MIT-licensen.

---

## 👤 Författare

**Adam O'Donoghue**

- GitHub: [@Adamprogramming04](https://github.com/Adamprogramming04)
- Repository: [saucedemo-selenium-tests](https://github.com/Adamprogramming04/saucedemo-selenium-tests)

---



**Skapad för:** Testautomatisering - Del 2 Inlämningsuppgift  
**Datum:** November 2025
