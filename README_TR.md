# LSM Tree ve SSTable Uygulaması

## Genel Bakış
Bu proje, Python'da temel bir Log-Structured Merge (LSM) Tree ve Sorted String Table (SSTable) uygulamasını gerçekleştirir. LSM Tree'lerin ve SSTable'ların, CRUD işlemlerini ve sıkıştırmayı (compaction) destekleyerek verimli anahtar-değer depolaması için nasıl kullanılabileceğini göstermek üzere tasarlanmış basit ancak işlevsel bir gösterimdir.

## Özellikler ve Kullanım

### `SSTable` Sınıfı
- **Amaç**: Anahtar-değer çiftlerini diske dayalı olarak yönetir.
- **Fonksiyonlar**:
  - `insert(key, value)`: Bir anahtar-değer çifti saklar.
  - `delete(key)`: Bir anahtar-değer çiftini kaldırır.
  - `read(key)`: Belirli bir anahtar için değeri getirir.
  - `load_from_disk()`: Depolama dosyasından verileri yükler.
  - `write_to_disk()`: Verileri depolama dosyasına yazar.

### `LSMTree` Sınıfı
- **Amaç**: Hızlı yazma için bir memtable ve verimli depolama ve alım için SSTable'ları yönetir.
- **Fonksiyonlar**:
  - `insert(key, value)`: Memtable'a bir anahtar-değer çifti ekler veya günceller. Gerekirse sıkıştırmayı tetikler.
  - `bulk_insert(key_value_pairs)`: Birden fazla anahtar-değer çiftinin toplu eklenmesini sağlar.
  - `read(key)`: Belirli bir anahtar için değeri memtable veya SSTable'lardan getirir.
  - `iterate_keys()`: LSM Tree'deki tüm anahtarların bir setini döndürür.
  - `update(key, value)`: Varolan bir anahtarın değerini günceller.
  - `delete(key)`: Bir anahtarı silmek için işaretler.
  - `start()`: LSM Tree'yi başlatır ve mevcut SSTable'ları yükler.
  - `_compaction()`: Memtable'dan SSTable'a veri taşıyan dahili fonksiyon.
  - `_merge_sstables()`: Birden fazla SSTable'ı tek bir SSTable ile birleştirir.
  - `_load_sstables()`: Mevcut SSTable'ları diskten yükler.

### Kullanım Senaryoları
1. **Başlangıç Kurulumu**: LSM Tree'yi başlatmak için `start()` kullanın.
2. **Veri Ekleme**: Tek girişler için `insert()` veya çoklu girişler için `bulk_insert()` kullanın.
3. **Veri Okuma**: Belirli bir anahtar için değeri almak için `read()` kullanın.
4. **Veri Güncelleme**: Varolan bir anahtarın değerini değiştirmek için `update()` kullanın.
5. **Veri Silme**: Bir anahtar-değer çiftini kaldırmak için `delete()` kullanın.
6. **Anahtarları İterasyon**: Tüm anahtarların bir setini almak için `iterate_keys()` kullanın.

## Kurulum
Bu projeyi çalıştırmak için ekstra kütüphanelere ihtiyaç yoktur. Repoyu klonlayıp Python scriptini çalıştırmanız yeterlidir.

```bash
git clone https://github.com/UmutKorkmaz/Python-LSM-SSTable-KeyValueStore
cd ./Python-LSM-SSTable-KeyValueStore
python main.py
```


[Türkçe sürüm için buraya tıklayın](README_TR.md)
