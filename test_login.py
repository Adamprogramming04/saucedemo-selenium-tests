"""
Selenium WebDriver Test Suite - Sauce Demo Login Function
Author: Adam O'Donoghue
GitHub: https://github.com/Adamprogramming04
Description: Automated tests for login functionality on saucedemo.com
"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class SauceDemoLoginTests(unittest.TestCase):
    """Test suite for Sauce Demo login functionality"""
    
    BASE_URL = "https://www.saucedemo.com/"
    VALID_USERNAME = "standard_user"
    VALID_PASSWORD = "secret_sauce"
    
    def setUp(self):
        """Initialize WebDriver before each test"""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.BASE_URL)
    
    def tearDown(self):
        """Close browser after each test"""
        time.sleep(1)
        self.driver.quit()
    
    # ========== GODKÄNT (G) TEST ==========
    def test_successful_login_with_valid_credentials(self):
        """
        Test successful login with correct username and password.
        Verifies that user is redirected to inventory page after login.
        """
        print("\n🔵 Kör test: Lyckad inloggning med korrekta uppgifter")
        
        # Hitta och fyll i användarnamn
        username_field = self.driver.find_element(By.ID, "user-name")
        username_field.clear()
        username_field.send_keys(self.VALID_USERNAME)
        print(f"   ✓ Fyllde i användarnamn: {self.VALID_USERNAME}")
        
        # Hitta och fyll i lösenord
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(self.VALID_PASSWORD)
        print("   ✓ Fyllde i lösenord")
        
        # Klicka på login-knappen
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        print("   ✓ Klickade på login-knappen")
        
        # Vänta på att sidan laddas och verifiera redirect
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("/inventory.html")
            )
            print("   ✓ Redirected till inventory-sidan")
        except TimeoutException:
            self.fail("Login misslyckades - redirectades inte till inventory-sidan")
        
        # Verifiera att vi är på rätt sida
        current_url = self.driver.current_url
        self.assertIn("/inventory.html", current_url, 
                     "Användaren ska redirectas till inventory-sidan efter lyckad inloggning")
        print(f"   ✓ Verifierade URL: {current_url}")
        
        # Extra verifiering: Kontrollera att inventory_container visas
        inventory_container = self.driver.find_element(By.CLASS_NAME, "inventory_container")
        self.assertTrue(inventory_container.is_displayed(), 
                       "Inventory container ska vara synlig efter lyckad inloggning")
        print("   ✓ Inventory container är synlig")
        
        print("   ✅ TEST GODKÄNT: Lyckad inloggning\n")
    
    # ========== VÄL GODKÄNT (VG) TEST 1 ==========
    def test_login_with_invalid_username(self):
        """
        Test login attempt with incorrect username.
        Verifies that appropriate error message is displayed.
        """
        print("\n🟡 Kör test: Inloggning med felaktigt användarnamn")
        
        invalid_username = "invalid_user_123"
        
        # Fyll i felaktigt användarnamn
        username_field = self.driver.find_element(By.ID, "user-name")
        username_field.clear()
        username_field.send_keys(invalid_username)
        print(f"   ✓ Fyllde i felaktigt användarnamn: {invalid_username}")
        
        # Fyll i korrekt lösenord
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(self.VALID_PASSWORD)
        print("   ✓ Fyllde i korrekt lösenord")
        
        # Klicka på login-knappen
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        print("   ✓ Klickade på login-knappen")
        
        # Vänta på att felmeddelandet visas
        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
            )
            print("   ✓ Felmeddelande hittades")
        except TimeoutException:
            self.fail("Felmeddelande visades inte efter felaktigt användarnamn")
        
        # Verifiera att felmeddelandet är synligt
        self.assertTrue(error_message.is_displayed(), 
                       "Felmeddelande ska vara synligt")
        
        # Verifiera innehållet i felmeddelandet
        error_text = error_message.text
        self.assertIn("Username and password do not match", error_text,
                     "Felmeddelandet ska innehålla text om felaktig inloggning")
        print(f"   ✓ Felmeddelande verifierat: {error_text[:50]}...")
        
        # Verifiera att användaren är kvar på login-sidan
        current_url = self.driver.current_url
        self.assertEqual(current_url, self.BASE_URL,
                        "Användaren ska stanna kvar på login-sidan")
        print("   ✓ Användaren är kvar på login-sidan")
        
        print("   ✅ TEST GODKÄNT: Felmeddelande för felaktigt användarnamn\n")
    
    # ========== VÄL GODKÄNT (VG) TEST 2 ==========
    def test_login_with_invalid_password(self):
        """
        Test login attempt with incorrect password.
        Verifies that appropriate error message is displayed.
        """
        print("\n🟠 Kör test: Inloggning med felaktigt lösenord")
        
        invalid_password = "wrong_password_456"
        
        # Fyll i korrekt användarnamn
        username_field = self.driver.find_element(By.ID, "user-name")
        username_field.clear()
        username_field.send_keys(self.VALID_USERNAME)
        print(f"   ✓ Fyllde i korrekt användarnamn: {self.VALID_USERNAME}")
        
        # Fyll i felaktigt lösenord
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(invalid_password)
        print("   ✓ Fyllde i felaktigt lösenord")
        
        # Klicka på login-knappen
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()
        print("   ✓ Klickade på login-knappen")
        
        # Vänta på att felmeddelandet visas
        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
            )
            print("   ✓ Felmeddelande hittades")
        except TimeoutException:
            self.fail("Felmeddelande visades inte efter felaktigt lösenord")
        
        # Verifiera att felmeddelandet är synligt
        self.assertTrue(error_message.is_displayed(),
                       "Felmeddelande ska vara synligt")
        
        # Verifiera innehållet i felmeddelandet
        error_text = error_message.text
        self.assertIn("Username and password do not match", error_text,
                     "Felmeddelandet ska innehålla text om felaktig inloggning")
        print(f"   ✓ Felmeddelande verifierat: {error_text[:50]}...")
        
        # Verifiera att användaren är kvar på login-sidan
        current_url = self.driver.current_url
        self.assertEqual(current_url, self.BASE_URL,
                        "Användaren ska stanna kvar på login-sidan")
        print("   ✓ Användaren är kvar på login-sidan")
        
        print("   ✅ TEST GODKÄNT: Felmeddelande för felaktigt lösenord\n")


if __name__ == "__main__":
    print("=" * 70)
    print("STARTAR SAUCE DEMO TEST SUITE")
    print("Author: Adam O'Donoghue")
    print("GitHub: https://github.com/Adamprogramming04")
    print("=" * 70)
    unittest.main(verbosity=2)
