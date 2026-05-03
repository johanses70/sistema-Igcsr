import tkinter as tk
from tkinter import messagebox, simpledialog


# =========================
# CLASS Usuario (LOGIN)
# =========================
class Usuario:
    def __init__(self):
        self._usuario = "programacion"
        self._password = "programacion"

    def validar(self, usuario_ingresado, password_ingresada):
        return (usuario_ingresado.lower() == self._usuario and
                password_ingresada == self._password)


# =========================
# CLASS BicicletaTaller
# =========================
class BicicletaTaller:
    def __init__(self, serial, costo_por_hora):
        self._serial = serial
        self._hora_ingreso = None
        self._costo_por_hora = costo_por_hora

    def registrar_ingreso(self, hora):
        self._hora_ingreso = hora

    def calcular_total(self, hora_salida):
        if self._hora_ingreso is None:
            return None
        if hora_salida <= self._hora_ingreso:
            return None
        tiempo = hora_salida - self._hora_ingreso
        return tiempo * self._costo_por_hora

    def obtener_serial(self):
        return self._serial

    def obtener_hora_ingreso(self):
        return self._hora_ingreso


# =========================
# MAIN APPLICATION
# =========================
class SistemaTaller:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.usuario = Usuario()
        self.bicicletas = []
        self.login_screen()

    # ---------------------
    # LOGIN SCREEN
    # ---------------------
    def login_screen(self):
        self.clear_window()

        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Username").pack()
        self.entry_user = tk.Entry(self.root)
        self.entry_user.pack()

        tk.Label(self.root, text="Password").pack()
        self.entry_pass = tk.Entry(self.root, show="*")
        self.entry_pass.pack()

        tk.Button(self.root, text="Login", command=self.validar_login).pack(pady=10)

    def validar_login(self):
        user = self.entry_user.get().strip()
        password = self.entry_pass.get().strip()

        if self.usuario.validar(user, password):
            self.main_screen()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    # ---------------------
    # MAIN SCREEN
    # ---------------------
    def main_screen(self):
        self.clear_window()
        self.root.title("Bike Workshop System")

        tk.Label(self.root, text="Bike Workshop Control System",
                 font=("Arial", 14)).pack(pady=10)

        tk.Button(self.root, text="Register Bike Entry",
                  command=self.registrar_bicicleta).pack(pady=5)

        tk.Button(self.root, text="Register Bike Exit",
                  command=self.registrar_salida).pack(pady=5)

        tk.Button(self.root, text="Show Registered Bikes",
                  command=self.mostrar_bicicletas).pack(pady=5)

    # ---------------------
    # REGISTER ENTRY
    # ---------------------
    def registrar_bicicleta(self):
        serial = simpledialog.askstring("Input", "Enter bike serial:")
        if not serial:
            messagebox.showerror("Error", "Serial cannot be empty")
            return

        # Validar serial duplicado
        for bici in self.bicicletas:
            if bici.obtener_serial() == serial:
                messagebox.showerror("Error", "Serial already exists")
                return

        try:
            hora = float(simpledialog.askstring("Input", "Enter entry time (hour):"))
            costo = float(simpledialog.askstring("Input", "Enter cost per hour:"))
        except:
            messagebox.showerror("Error", "Invalid numeric input")
            return

        if hora < 0 or costo <= 0:
            messagebox.showerror("Error", "Time and cost must be positive numbers")
            return

        bicicleta = BicicletaTaller(serial, costo)
        bicicleta.registrar_ingreso(hora)
        self.bicicletas.append(bicicleta)

        messagebox.showinfo("Success", "Bike registered successfully")

    # ---------------------
    # REGISTER EXIT
    # ---------------------
    def registrar_salida(self):
        serial = simpledialog.askstring("Input", "Enter bike serial for exit:")
        if not serial:
            messagebox.showerror("Error", "Serial cannot be empty")
            return

        for bici in self.bicicletas:
            if bici.obtener_serial() == serial:
                try:
                    hora_salida = float(simpledialog.askstring("Input", "Enter exit time (hour):"))
                except:
                    messagebox.showerror("Error", "Invalid numeric input")
                    return

                total = bici.calcular_total(hora_salida)

                if total is None:
                    messagebox.showerror("Error", "Exit time must be greater than entry time")
                    return

                messagebox.showinfo("Total Cost",
                                    f"Total service cost: ${total:.2f}")

                self.bicicletas.remove(bici)
                return

        messagebox.showerror("Error", "Bike not found")

    # ---------------------
    # SHOW BIKES
    # ---------------------
    def mostrar_bicicletas(self):
        if not self.bicicletas:
            messagebox.showinfo("Info", "No bikes registered")
            return

        info = ""
        for bici in self.bicicletas:
            info += f"Serial: {bici.obtener_serial()} | Entry Hour: {bici.obtener_hora_ingreso()}\n"

        messagebox.showinfo("Registered Bikes", info)

    # ---------------------
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# =========================
# RUN PROGRAM
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaTaller(root)
    root.mainloop()