# Nama: Della Agustin
# NIM : 2007973

class Warna:
  def intro(self):
    print("Warna merupakan kesan yang diperoleh mata dari cahaya yang dipantulkan oleh benda-benda yang dikenainya.")
  def jenis(self):
    print("Umumnya, warna dibagi menjadi tiga jenis, yaitu warna primer, warna sekunder, dan warna tersier.")

class Biru(Warna):
  def jenis(self):
    print("Warna biru tergolong ke dalam jenis warna primer.")

class Jingga(Warna):
  def jenis(self):
    print("Warna jingga tergolong ke dalam jenis warna sekunder.")

class Cokelat(Warna):
  def jenis(self):
    print("Warna cokelat tergolong ke dalam jenis warna tersier.")

obj_warna = Warna()
obj_biru = Biru()
obj_jingga = Jingga()
obj_cokelat = Cokelat()

obj_warna.intro()
obj_warna.jenis()

obj_biru.jenis()

obj_jingga.jenis()

obj_cokelat.jenis()