import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import os


class HarshilClickerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Harshil Clicker")
        self.root.geometry("420x600")

        # CORE STATS
        self.cholesterol = 0
        self.click_power = 1
        self.multiplier = 1

        # FOOD SYSTEM (CPS)
        self.foods = {
            "Burger": {"count": 0, "cps": 0.1, "cost": 10},
            "Fries": {"count": 0, "cps": 0.5, "cost": 50},
            "Pizza": {"count": 0, "cps": 1, "cost": 100},
            "Ice Cream": {"count": 0, "cps": 3, "cost": 250},
        }

        self.harshil_image = None

        self.create_widgets()
        self.load_default_image()

        # START GAME LOOP
        self.game_loop()

    # ---------------- UI ----------------
    def create_widgets(self):
        self.score_label = ttk.Label(self.root, text="Cholesterol: 0", font=("Arial", 16))
        self.score_label.pack(pady=10)

        # CLICK IMAGE BUTTON
        self.click_button = tk.Button(self.root, text="Click Harshil", command=self.click)
        self.click_button.pack(pady=15)

        self.cps_label = ttk.Label(self.root, text="CPS: 0", font=("Arial", 12))
        self.cps_label.pack()

        # SHOP
        self.food_frame = ttk.LabelFrame(self.root, text="Food Shop")
        self.food_frame.pack(pady=10, fill="x", padx=10)

        self.refresh_shop()

        ttk.Button(self.root, text="Upload Harshil Image", command=self.load_image).pack(pady=10)

        self.doctor_button = ttk.Button(self.root, text="Doctor Visit (Reset for bonus)", command=self.doctor_visit)
        self.doctor_button.pack(pady=10)

        self.bonus_label = ttk.Label(self.root, text="Multiplier: x1")
        self.bonus_label.pack()

    def refresh_shop(self):
        """ONLY update shop when needed"""
        for widget in self.food_frame.winfo_children():
            widget.destroy()

        for food, data in self.foods.items():
            text = f"{food} | Owned: {data['count']} | +{data['cps']} CPS | Cost: {int(data['cost'])}"

            btn = ttk.Button(
                self.food_frame,
                text=text,
                command=lambda f=food: self.buy_food(f)
            )
            btn.pack(fill="x", padx=5, pady=2)

    # ---------------- GAME LOGIC ----------------
    def click(self):
        self.cholesterol += self.click_power * self.multiplier
        self.update_ui()

    def get_total_cps(self):
        total = 0
        for data in self.foods.values():
            total += data["count"] * data["cps"]
        return total * self.multiplier

    def game_loop(self):
        cps = self.get_total_cps()
        self.cholesterol += cps / 10

        self.update_ui()
        self.root.after(100, self.game_loop)

    def update_ui(self):
        self.score_label.config(text=f"Cholesterol: {int(self.cholesterol)}")
        self.cps_label.config(text=f"CPS: {round(self.get_total_cps(), 2)}")

    def buy_food(self, food):
        data = self.foods[food]

        # Float-safe comparison
        if self.cholesterol >= data["cost"] - 0.0001:
            self.cholesterol -= data["cost"]
            data["count"] += 1

            # scaling cost
            data["cost"] *= 1.15

            self.refresh_shop()
            self.update_ui()
        else:
            print("Not enough cholesterol")

    def doctor_visit(self):
        if self.cholesterol >= 100:
            self.cholesterol = 0
            self.click_power = 1
            self.multiplier += 1

            for food in self.foods:
                self.foods[food]["count"] = 0
                self.foods[food]["cost"] = max(10, self.foods[food]["cost"] / 2)

            self.bonus_label.config(text=f"Multiplier: x{self.multiplier}")
            self.refresh_shop()
            self.update_ui()

    # ---------------- IMAGE ----------------
    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif")]
        )
        if file_path:
            self.set_image(file_path)

    def load_default_image(self):
        # FIXED: proper indentation + structure
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, "harshil.png")

        if os.path.exists(image_path):
            self.set_image(image_path)
        else:
            print("harshil.png not found in:", base_dir)

    def set_image(self, path):
        img = Image.open(path)
        img = img.resize((200, 200))
        self.harshil_image = ImageTk.PhotoImage(img)

        self.click_button.config(image=self.harshil_image, text="", command=self.click)


# RUN (ONLY ONCE - removed duplicates)
if __name__ == "__main__":
    root = tk.Tk()
    app = HarshilClickerApp(root)
    root.mainloop()