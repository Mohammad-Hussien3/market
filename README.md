# Market & Telegram Bot System

A comprehensive e-commerce backend built with Django and Django REST Framework, designed to operate in conjunction with a Telegram Bot. This system manages an online store (specifically tailored for dental supplies), user profiles via Telegram, order processing, and a loyalty point/referral system.

**🤖 Try the Live Bot:** [https://t.me/dental_kit_store_bot](https://t.me/dental_kit_store_bot)

## 🚀 Features

### 🤖 Telegram Bot Integration (`telegram_bot` app)
* **Seamless Onboarding:** Automatically creates user profiles based on Telegram ID when they interact with the bot (`/start`).
* **Interactive Menu:** Provides an inline keyboard menu for easy navigation:
    * 🛍️ Visit Web App Store
    * 📍 View Points
    * 📢 Get Referral Link
    * 📌 View Pending Orders
    * 🛒 Purchase History.
* **Web App Support:** Integrates with a frontend Web App for the browsing and purchasing experience.

### 🛒 E-Commerce & Store Management (`item` app)
* **Categorization:** Items are divided into categories (e.g., **Student**, **Doctor**) to target specific user groups.
* **Product Types:**
    * **Items:** Standard products with prices.
    * **Packages:** Bundles of items sold together.
    * **Point Items:** Special items purchasable only with loyalty points.
* **Cloud Storage:** Uses **Cloudinary** for hosting product and package images.
* **Search:** Search functionality for items and packages by name.

### 📦 Order Management (`item` app)
* **Dual Payment Methods:** Supports orders paid via **Price** (Cash) or **Points**.
* **Order Lifecycle:** Tracks orders through statuses: `pending` → `delivery` → `finished`.
* **Cart System:** Orders can contain multiple Items, Packages, and Point Items simultaneously.
* **History:** Users can view their pending and completed orders directly through the Telegram bot.

### 💎 Loyalty & Referral System (`usermanagament` & `item` app)
* **Referral Links:** Generates unique Telegram referral links for every user.
* **Point Earning:**
    * **Purchase Rewards:** Users earn points when their order status becomes 'finished'.
    * **Referral Rewards:** Users earn points when someone they referred completes a purchase.
* **Global Configuration:** Admins can configure the point conversion rates for referrals and purchases.

### 🛡️ Administration (`usermanagament` app)
* **Custom Admin Auth:** A custom authentication system for Admin and Sub-Admin roles.
* **Password Management:** Endpoints to update admin and sub-admin passwords securely.

## 🛠️ Technology Stack
* **Framework:** Django 5.1.3
* **API:** Django REST Framework
* **Database:** SQLite (default)
* **Image Storage:** Cloudinary
* **Bot Interface:** Telegram Bot API
* **CORS:** `django-cors-headers` enabled for frontend integration.

## 📦 Installation

1.  **Clone the repository**
    ```bash
    git clone <repository-url>
    cd market
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Environment Setup**
    Set up your Cloudinary credentials and Telegram Bot Token. It is recommended to use environment variables, though defaults are present in `settings.py`.
    * `CLOUDINARY_CLOUD_NAME`
    * `CLOUDINARY_API_KEY`
    * `CLOUDINARY_API_SECRET`
    * `SECRET_KEY`

4.  **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

5.  **Run the Server**
    ```bash
    python manage.py runserver
    ```
