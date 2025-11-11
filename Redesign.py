import tkinter as tk
from tkinter import messagebox

class CraigslistRedesign:
    def __init__(self, root):
        self.root = root
        self.root.title("Classifieds Portal – Redesign")
        self.root.geometry("850x600")
        self.root.configure(bg="#f4f7fa")

        # Sample data for ads
        self.ads_data = {
            "For Sale": [
                {"title": "Used Laptop - Dell Inspiron", "desc": "i5, 8GB RAM, 512GB SSD. Excellent condition.", "price": "₹28,000"},
                {"title": "Cycle for Sale", "desc": "Hero cycle, barely used. Pune area only.", "price": "₹3,000"}
            ],
            "Housing": [
                {"title": "1BHK Flat in Kothrud", "desc": "Spacious flat with parking and balcony.", "price": "₹15,000/month"},
                {"title": "PG Accommodation", "desc": "Girls PG near FC Road, fully furnished.", "price": "₹8,000/month"}
            ],
            "Jobs": [
                {"title": "Software Intern - Python Developer", "desc": "Entry-level internship, remote option available.", "price": "₹10,000/month"},
                {"title": "Sales Executive", "desc": "Field sales role, freshers welcome.", "price": "₹18,000/month"}
            ],
            "Services": [
                {"title": "Home Cleaning Service", "desc": "Professional team for deep cleaning.", "price": "₹1,500/visit"},
                {"title": "Freelance Graphic Designer", "desc": "Logos, posters, and branding work.", "price": "Negotiable"}
            ]
        }

        # Header
        header = tk.Frame(root, bg="#2c3e50", height=60)
        header.pack(fill="x")
        tk.Label(header, text="Classifieds Portal", font=("Arial", 20, "bold"), fg="white", bg="#2c3e50").pack(side="left", padx=20, pady=10)

        tk.Button(header, text="Browse Listings", bg="#3498db", fg="white", font=("Arial", 10, "bold"),
                  command=self.show_welcome).pack(side="right", padx=10, pady=15)
        tk.Button(header, text="Post Ad", bg="#e67e22", fg="white", font=("Arial", 10, "bold"),
                  command=self.post_ad_window).pack(side="right", padx=10, pady=15)

        # Search Bar
        search_frame = tk.Frame(root, bg="#f4f7fa", pady=10)
        search_frame.pack(fill="x")
        tk.Label(search_frame, text="What are you looking for?", font=("Arial", 12), bg="#f4f7fa").pack(side="left", padx=20)
        self.search_entry = tk.Entry(search_frame, width=40, font=("Arial", 12))
        self.search_entry.pack(side="left", padx=10)
        tk.Button(search_frame, text="Search", bg="#27ae60", fg="white", font=("Arial", 10, "bold"),
                  command=self.search).pack(side="left", padx=10)

        # Body Frame (Sidebar + Content)
        body = tk.Frame(root, bg="#f4f7fa")
        body.pack(fill="both", expand=True, padx=20, pady=10)

        # Sidebar for Categories
        sidebar = tk.Frame(body, bg="#ffffff", width=180, relief="groove", bd=1)
        sidebar.pack(side="left", fill="y", padx=(0,10), pady=5)
        tk.Label(sidebar, text="Categories", font=("Arial", 14, "bold"), bg="#ffffff").pack(pady=10)
        categories = ["For Sale", "Housing", "Jobs", "Services"]
        for cat in categories:
            btn = tk.Button(sidebar, text=cat, bg="#ecf0f1", fg="#2c3e50", font=("Arial", 11),
                            relief="flat", command=lambda c=cat: self.show_category(c))
            btn.pack(fill="x", padx=10, pady=5)

        # Content Area
        self.content = tk.Frame(body, bg="#ffffff", relief="groove", bd=1)
        self.content.pack(side="right", fill="both", expand=True, pady=5)
        self.show_welcome()

        # Footer
        footer = tk.Frame(root, bg="#bdc3c7", height=30)
        footer.pack(fill="x")
        tk.Label(footer, text="© 2025 Classifieds Portal – Redesigned Interface", font=("Arial", 9), bg="#bdc3c7").pack(pady=5)

    def show_welcome(self):
        for widget in self.content.winfo_children():
            widget.destroy()
        tk.Label(self.content, text="Welcome to Classifieds Portal", font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=20)
        tk.Label(self.content, text="Browse listings by category or use search to find something specific.", 
                 font=("Arial", 12), bg="#ffffff").pack(pady=5)

    def show_category(self, category):
        for widget in self.content.winfo_children():
            widget.destroy()
        tk.Label(self.content, text=f"{category} Listings", font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=10)
        ads = self.ads_data.get(category, [])
        if not ads:
            tk.Label(self.content, text="No ads found in this category.", font=("Arial", 12), bg="#ffffff").pack(pady=10)
            return

        for ad in ads:
            frame = tk.Frame(self.content, bg="#ecf0f1", pady=5, padx=5, relief="ridge", bd=1)
            frame.pack(fill="x", padx=10, pady=5)
            tk.Label(frame, text=ad["title"], font=("Arial", 13, "bold"), bg="#ecf0f1").pack(anchor="w")
            tk.Label(frame, text=ad["desc"], font=("Arial", 10), bg="#ecf0f1").pack(anchor="w")
            tk.Label(frame, text=f"Price: {ad['price']}", font=("Arial", 10, "italic"), bg="#ecf0f1", fg="#16a085").pack(anchor="w")

    def search(self):
        query = self.search_entry.get().strip().lower()
        if not query:
            messagebox.showwarning("Input needed", "Please enter search text.")
            return
        results = []
        for category, ads in self.ads_data.items():
            for ad in ads:
                if query in ad["title"].lower() or query in ad["desc"].lower():
                    results.append((category, ad))
        for widget in self.content.winfo_children():
            widget.destroy()
        tk.Label(self.content, text=f"Search Results for '{query}'", font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=10)
        if not results:
            tk.Label(self.content, text="No matching ads found.", font=("Arial", 12), bg="#ffffff").pack(pady=10)
        for category, ad in results:
            frame = tk.Frame(self.content, bg="#ecf0f1", pady=5, padx=5, relief="ridge", bd=1)
            frame.pack(fill="x", padx=10, pady=5)
            tk.Label(frame, text=f"{ad['title']} ({category})", font=("Arial", 13, "bold"), bg="#ecf0f1").pack(anchor="w")
            tk.Label(frame, text=ad["desc"], font=("Arial", 10), bg="#ecf0f1").pack(anchor="w")
            tk.Label(frame, text=f"Price: {ad['price']}", font=("Arial", 10, "italic"), bg="#ecf0f1", fg="#16a085").pack(anchor="w")

    def post_ad_window(self):
        new_win = tk.Toplevel(self.root)
        new_win.title("Post a New Ad")
        new_win.geometry("400x400")
        new_win.configure(bg="#fefefe")

        tk.Label(new_win, text="Post a New Advertisement", font=("Arial", 14, "bold"), bg="#fefefe").pack(pady=10)

        tk.Label(new_win, text="Select Category:", bg="#fefefe").pack(pady=5)
        category_var = tk.StringVar(new_win)
        category_menu = tk.OptionMenu(new_win, category_var, "For Sale", "Housing", "Jobs", "Services")
        category_menu.pack(pady=5)

        tk.Label(new_win, text="Title:", bg="#fefefe").pack(pady=5)
        title_entry = tk.Entry(new_win, width=40)
        title_entry.pack(pady=5)

        tk.Label(new_win, text="Description:", bg="#fefefe").pack(pady=5)
        desc_entry = tk.Entry(new_win, width=40)
        desc_entry.pack(pady=5)

        tk.Label(new_win, text="Price:", bg="#fefefe").pack(pady=5)
        price_entry = tk.Entry(new_win, width=40)
        price_entry.pack(pady=5)

        def submit_ad():
            cat = category_var.get()
            title = title_entry.get()
            desc = desc_entry.get()
            price = price_entry.get()
            if not (cat and title and desc and price):
                messagebox.showerror("Error", "All fields are required.")
                return
            new_ad = {"title": title, "desc": desc, "price": price}
            self.ads_data[cat].append(new_ad)
            messagebox.showinfo("Success", "Ad posted successfully!")
            new_win.destroy()
            self.show_category(cat)

        tk.Button(new_win, text="Submit Ad", bg="#27ae60", fg="white", font=("Arial", 10, "bold"), command=submit_ad).pack(pady=20)

def main():
    root = tk.Tk()
    app = CraigslistRedesign(root)
    root.mainloop()

if __name__ == "__main__":
    main()
