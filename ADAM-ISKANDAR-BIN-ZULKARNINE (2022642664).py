import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Sambung ke database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="panda_filem_rigester"
)

mycursor = mydb.cursor()

# hantar data 
def hantar_data():
    accepted = accept_var.get()

    if accepted == "Terima":
        try:
            # terima data
            tajuk_filem = tajuk_filem_entry.get()
            durasi = durasi_entry.get()
            tarikh = tarikh_entry.get()

            had_umur = had_umur_combobox.get()
            negara = negara_combobox.get()
            jenis = jenis_text.get("1.0", "end-1c")
            pelakon = pelakon_entry.get("1.0", "end-1c")
            pengarah_filem = pengarah_text.get("1.0", "end-1c")
            studio_prodaksi = studio_text.get("1.0", "end-1c")
            sinopsis_filem = sinopsis_text.get("1.0", "end-1c")

            print("Tajuk Filem:", tajuk_filem, "Durasi:", durasi, "Tarikh:", tarikh)
            print("Umur:", had_umur, "Negara:", negara, "Jenis:", jenis)
            print("# Pelakon:", pelakon, "# Pengarah Filem:", pengarah_filem, "# Studio Prodaksi:", studio_prodaksi)
            print("Sinopsis Filem:", sinopsis_filem)
            print("------------------------------------------")

            # perkiraan
            jumlah_kutipan_Malaysia = float(kutipan_Malaysia_entry.get())
            jumlah_kutipan_luar = float(kutipan_luar_entry.get())
            RM = jumlah_kutipan_Malaysia + jumlah_kutipan_luar
            tk.messagebox.showinfo("Hasil Kutipan", f"Jumlah Kutipan Filem(RM): {jumlah_kutipan_Malaysia + jumlah_kutipan_luar}")

            print("Revenue data inserted into the 'kutipan' table.")
            print("------------------------------------------")
            print("Jumlah Kutipan Malaysia: ", jumlah_kutipan_Malaysia, "Jumlah Kutipan Luar: ", jumlah_kutipan_luar)
            print("Total Revenue (RM):", RM)
            print("------------------------------------------")

            sql = ("INSERT INTO panda_filem (tajuk_filem, durasi, tarikh, had_umur, negara, jenis, pelakon, pengarah_filem, studio_prodaksi, sinopsis_filem, jumlah_kutipan_Malaysia, jumlah_kutipan_luar) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            val = (tajuk_filem, durasi, tarikh, had_umur, negara, jenis, pelakon, pengarah_filem,studio_prodaksi, sinopsis_filem, jumlah_kutipan_Malaysia, jumlah_kutipan_luar)
           
            mycursor.execute(sql, val)
            mydb.commit()


        except Exception as e:
            tk.messagebox.showerror(title="Error", message=f"An error occurred: {str(e)}")

    else:
        tk.messagebox.showwarning(title="Error", message="Anda belum menerima 'Terma dan Syarat.'")

# tunjuk jumlah kutipan filem
def tunjuk_kutipan_data():
    try:
        jumlah_kutipan_Malaysia = float(kutipan_Malaysia_entry.get())
        jumlah_kutipan_luar = float(kutipan_luar_entry.get())
        RM = jumlah_kutipan_Malaysia + jumlah_kutipan_luar
        tk.messagebox.showinfo("Hasil Kutipan", f"Jumlah Kutipan Filem(RM): {jumlah_kutipan_Malaysia + jumlah_kutipan_luar}")

        print("Revenue data inserted into the 'kutipan' table.")
        print("------------------------------------------")
        print("Jumlah Kutipan Malaysia: ", jumlah_kutipan_Malaysia, "Jumlah Kutipan Luar: ", jumlah_kutipan_luar)
        print("Total Revenue (RM):", RM)
        print("------------------------------------------")

    except ValueError:
        tk.messagebox.showerror(title="Error", message="Please enter valid numerical values for kutipan.")
    except Exception as e:
        tk.messagebox.showerror(title="Error", message=f"An error occurred: {str(e)}")


#Tkinter GUI
root = tk.Tk()
root['bg'] = '#3B9C9C'
root.geometry("800x1200")
root.title("Panda Filem")
root.iconbitmap(r'c:\Users\zul\Downloads\panda.ico')


main_label = tk.Label(root, fg="#3c096c", text="SELAMAT DATANG KE PANDA FILEM!", font=("Algerian", 20), bg="#3B9C9C")
main_label.pack()

sec_label = tk.Label(root, fg='#5a189a',text="MASUKKAN FILEM YANG INGIN DIDAFTAR!", font=("Algerian", 20), bg="#3B9C9C")
sec_label.pack()

frame = tk.Frame(root)
frame.pack()
frame = tk.Frame(root, bg='#5F9EA0')
frame.pack()

# Simpan maklumat filem
user_info_frame = tk.LabelFrame(frame, text="Maklumat Filem", font=('Algerian', 10,), bg='#3B9C9C')
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

tajuk_filem = tk.Label(user_info_frame, text="Tajuk Filem",font=('Algerian', 10,), bg='#FFFFFF')
tajuk_filem.grid(row=0, column=0)
durasi = tk.Label(user_info_frame, text="Durasi",font=('Algerian', 10,), bg='#FFFFFF')
durasi.grid(row=0, column=1)
tarikh = tk.Label(user_info_frame, text="Tarikh",font=('Algerian', 10,), bg='#FFFFFF')
tarikh.grid(row=0, column=2)


tajuk_filem_entry = tk.Entry(user_info_frame)
durasi_entry = tk.Entry(user_info_frame)
tarikh_entry = tk.Entry(user_info_frame)
tajuk_filem_entry.grid(row=1, column=0)
durasi_entry.grid(row=1, column=1)
tarikh_entry.grid(row=1, column=2)


jenis= tk.Label(user_info_frame, text="Jenis",font=('Algerian', 10,), bg='#FFFFFF')
jenis_text = tk.Text(user_info_frame, height=3, width=20)
jenis.grid(row=2, column=0)
jenis_text.grid(row=3, column=0)


had_umur= tk.Label(user_info_frame, text="Had Umur",font=('Algerian', 10,), bg='#FFFFFF')
had_umur_combobox = ttk.Combobox(user_info_frame, values=["", "U", "P12", "13", "16", "18", "21+"])
had_umur.grid(row=2, column=1)
had_umur_combobox.grid(row=3, column=1)

negara = tk.Label(user_info_frame, text="Negara",font=('Algerian', 10,), bg='#FFFFFF')
negara_combobox = ttk.Combobox(user_info_frame,
                               values=["Malaysia", "Indonesia", "Thailand", "Vietnam", 
                                       "USA", "Turkiye", "India", "United Kingdom",])
negara.grid(row=2, column=2)
negara_combobox.grid(row=3, column=2)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=30, pady=5)

# simpan maklumat prodaksi filem
prodaksi = tk.LabelFrame(frame, text="Prodaksi Filem", font=('Algerian', 10,), bg='#3B9C9C')
prodaksi.grid(row=1, column=0, sticky="news", padx=20, pady=10)


pelakon = tk.Label(prodaksi, text=" Pelakon",font=('Algerian', 10,), bg='#FFFFFF')
pelakon_entry = tk.Text(prodaksi, height=3, width=20)
pelakon.grid(row=1, column=0)
pelakon_entry.grid(row=2, column=0)

pengarah_filem = tk.Label(prodaksi, text=" Pengarah",font=('Algerian', 10,), bg='#FFFFFF')
pengarah_text = tk.Text(prodaksi, height=3, width=20)
pengarah_filem.grid(row=1, column=1)
pengarah_text.grid(row=2, column=1)

studio_prodaksi = tk.Label(prodaksi, text="Studio Prodaksi",font=('Algerian', 10,), bg='#FFFFFF')
studio_text = tk.Text(prodaksi, height=3, width=30)
studio_prodaksi.grid(row=1, column=2)
studio_text.grid(row=2, column=2)

sinopsis_filem = tk.LabelFrame(frame, text="Sinopsis Filem", font=('Algerian', 10,), bg='#3B9C9C')
sinopsis_text = tk.Text(sinopsis_filem, height=3, width=74)
sinopsis_filem.grid(row=3, column=0)
sinopsis_text.grid(row=0, column=0, sticky="news", padx=20, pady=10)


# jumlah kutipan filem
jumlah_kutipan_filem = tk.LabelFrame(frame, text="Jumlah Kutipan Filem", font=('Algerian', 10,), bg='#3B9C9C')
jumlah_kutipan_filem.grid(row=5, column=0, sticky="news", padx=20, pady=10)

jumlah_kutipan_Malaysia = tk.Label(jumlah_kutipan_filem, text="Jumlah Kutipan dalam Malaysia  (Rm): ",
                                          font=('Algerian', 10,), bg='#3B9C9C')
kutipan_Malaysia_entry = tk.Entry(jumlah_kutipan_filem)
jumlah_kutipan_Malaysia.grid(row=0, column=0)
kutipan_Malaysia_entry.grid(row=0, column=1)

jumlah_kutipan_luar = tk.Label(jumlah_kutipan_filem, text="Jumlah Kutipan diLuar Negara (Rm): ",
                                      font=('Algerian', 10,), bg='#3B9C9C')
kutipan_luar_entry = tk.Entry(jumlah_kutipan_filem)
jumlah_kutipan_luar.grid(row=2, column=0)
kutipan_luar_entry.grid(row=2, column=1)

kutipan_button = tk.Button(jumlah_kutipan_filem, text="Papar Kutipan", command=tunjuk_kutipan_data, font=('Algerian', 10,), bg='#3B9C9C')
kutipan_button.grid(row=3, column=0, columnspan=2, pady=5)
result_label = tk.Label(jumlah_kutipan_filem, text='')

for widget in prodaksi.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# terima terma dan syarat
terma_frame = tk.LabelFrame(frame, text="Terma dan Syarat", font=('Algerian', 10),  bg='#3B9C9C')
terma_frame.grid(row=6, column=0, sticky="news", padx=20, pady=10)

accept_var = tk.StringVar(value="Not Accepted")
terma_check = tk.Checkbutton(terma_frame, text="Saya menerima dan faham segala 'Terma dan Syarat'.", 
                             variable=accept_var, onvalue="Terima", offvalue="Tidak Terima", bg='#3B9C9C')
terma_check.grid(row=0, column=0)

# butang tunjuk hasil
button = tk.Button(frame, text="Masukkan Data", command=hantar_data, bg='#3B9C9C')
button.grid(row=8, column=0, sticky="news", padx=20, pady=10)

root.mainloop()