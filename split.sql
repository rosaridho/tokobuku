delete from Kategori_agama;
insert into Kategori_agama select id,gambar,judul,penulis,publisher,ketersediaan,harga,hargadiskon,kategori from Home_buku where kategori = "agama";

delete from Kategori_nonfiksi;
insert into Kategori_nonfiksi select id,gambar,judul,penulis,publisher,ketersediaan,harga,hargadiskon,kategori from Home_buku where kategori = "nonfiksi";

delete from Kategori_romance;
insert into Kategori_romance select id,gambar,judul,penulis,publisher,ketersediaan,harga,hargadiskon,kategori from Home_buku where kategori = "romance";

delete from Kategori_sastra;
insert into Kategori_sastra select id,gambar,judul,penulis,publisher,ketersediaan,harga,hargadiskon,kategori from Home_buku where kategori = "sastra";

delete from Kategori_teknik;
insert into Kategori_teknik select id,gambar,judul,penulis,publisher,ketersediaan,harga,hargadiskon,kategori from Home_buku where kategori = "teknik";