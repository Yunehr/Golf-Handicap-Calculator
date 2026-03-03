# ⛳ Golf Handicap Calculator

A modern, user-friendly desktop application for calculating and tracking golf handicaps. Built with Python and KivyMD for a smooth, responsive experience across multiple platforms.

---

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Development Progress](#development-progress)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Update Logs](#update-logs)

---

## 🎯 Project Overview

The **Golf Handicap Calculator** is a personal project designed to provide golfers with an easy way to calculate and manage their handicap indices. The application features an intuitive UI built with KivyMD, secure user authentication, and a smooth navigation experience between screens.

**Key Features:**
- User authentication system (Login/Registration)
- Clean, modern Material Design interface
- Cross-platform compatibility (Windows, macOS, Linux)
- Responsive screen management

---

## 🔄 Development Progress

### Before Development
- ❌ No application infrastructure
- ❌ No user interface
- ❌ No screen navigation system

### During Development
- ✅ Set up Kivy/KivyMD framework
- ✅ Created login screen with Material Design components
- ✅ Configured screen navigation and ScreenManager
- 🔄 **In Progress:** Implement Registration screen
- 🔄 **In Progress:** Implement Home screen
- 🔄 **In Progress:** User authentication backend
- ⚠️ **Upcoming:** Golf handicap calculation logic
- ⚠️ **Upcoming:** Golf Course Storage
- ⚠️ **Upcoming:** Round Score Storage

### After Development (Goals)
- ✨ Full user authentication system
- ✨ Dashboard for handicap tracking
- ✨ Round history
- ✨ Easy access to previously saved Golf Course Info
- ✨ Downloadable mobile app
- ✨ Cross-platform distribution

## 💾 Data Storage & Limits

This project is primarily a personal hobby app but is being designed with the goal of a future mobile release. To keep local storage small and predictable, the following storage rules will be enforced:

- Recent rounds: only the **20 most recent rounds** are kept locally. Users can delete all stored rounds to start over.
- Courses: store course metadata (name, slope, rating). Soft max of **20** courses; depending on storage footprint this may be increased up to **50**.
- When entering a new round the user may **select an existing course** from the stored list or **add a new course** inline.
- The user's handicap value is **not persisted**. Handicaps will be calculated on demand once at least **5 rounds** are stored.

These limits keep the app lightweight for mobile distribution while still providing useful history and course lookup.

---

## 📦 Installation

### Prerequisites
- Python 3.13 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd "Golf Handicap Calculator"
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python "Golf Handicap Calculator/main.py"
   ```

---

## 📚 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Kivy | 2.3.1 | Cross-platform UI framework |
| KivyMD | 1.2.0 | Material Design components for Kivy |
| Python | 3.13+ | Core language runtime |

**Install all dependencies:**
```bash
pip install kivy==2.3.1 kivymd==1.2.0
```

---

## 📝 Update Logs
*Last Updated: February 11, 2026*

### [2026-03-03] - Session 3
**Implemented**
- Implemented basic user authentication for Login screen

**Updated**
- Disabled registration button as functionality does not exist yet

**Issues**
- Navigation bar UI needs a rework, buttons are clickable but UI looks horrendous


---
### [2026-02-13] - Session 2
**Updates:**
- Implemented registration UI: responsive `MDCard` layout with `BackgroundLayer`.
- Added `Username`, `Password`, and `Re-enter Password` fields with input styling.
- `Register` button now calls `app.home_screen()` to navigate to the home screen.
- `Back to Login` button now calls `app.login_screen()` to return to the login screen.
- UI styling: card shadow, dark card color, centered titles and buttons.

**Notes:** Registration screen is currently UI-only; authentication backend not yet implemented.

---
### [2026-02-11] - Session 1
**Fixed Issues:**
- ✅ Fixed Kivy app window not displaying (missing `run()` call and empty build method)
- ✅ Resolved screen navigation crash (duplicate screen names in ScreenManager)
- ✅ Fixed button navigation between login and registration screens

**Implemented:**
- ✅ Complete login screen UI with Material Design
- ✅ Registration screen placeholder
- ✅ Home screen placeholder
- ✅ Screen navigation system with ScreenManager
- ✅ UI styling with custom colors and layouts

**Current Status:**
- Application successfully launches and navigates between screens
- Ready for next phase: Authentication backend implementation

---

