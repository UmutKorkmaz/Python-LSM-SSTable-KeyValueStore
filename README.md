# LSM Tree and SSTable Implementation

## Overview
This project implements a basic Log-Structured Merge (LSM) Tree and Sorted String Table (SSTable) in Python. It is designed to provide a simple yet functional demonstration of how LSM Trees and SSTables can be used for efficient key-value storage, supporting CRUD operations and compaction.

## Features and Usage

### `SSTable` Class
- **Purpose**: Manages disk-based storage for key-value pairs.
- **Functions**:
  - `insert(key, value)`: Stores a key-value pair.
  - `delete(key)`: Removes a key-value pair.
  - `read(key)`: Retrieves the value for a given key.
  - `load_from_disk()`: Loads data from the storage file.
  - `write_to_disk()`: Writes data to the storage file.

### `LSMTree` Class
- **Purpose**: Provides a memtable for fast writes and manages SSTables for efficient storage and retrieval.
- **Functions**:
  - `insert(key, value)`: Inserts or updates a key-value pair in the memtable. Triggers compaction if necessary.
  - `bulk_insert(key_value_pairs)`: Allows bulk insertion of multiple key-value pairs.
  - `read(key)`: Retrieves a value for a given key from the memtable or SSTables.
  - `iterate_keys()`: Returns a set of all keys in the LSM Tree.
  - `update(key, value)`: Updates the value for an existing key.
  - `delete(key)`: Marks a key for deletion.
  - `start()`: Initializes the LSM Tree and loads existing SSTables.
  - `_compaction()`: Internal function to move data from memtable to SSTable.
  - `_merge_sstables()`: Merges multiple SSTables into one.
  - `_load_sstables()`: Loads existing SSTables from disk.

### Usage Scenarios
1. **Initial Setup**: Use `start()` to initialize the LSM Tree.
2. **Inserting Data**: Use `insert()` for individual entries or `bulk_insert()` for multiple entries.
3. **Reading Data**: Use `read()` to retrieve the value for a specific key.
4. **Updating Data**: Use `update()` to change the value of an existing key.
5. **Deleting Data**: Use `delete()` to remove a key-value pair.
6. **Iterating Over Keys**: Use `iterate_keys()` to get a set of all keys.

## Installation
No additional libraries are required to run this project. Simply clone the repository and run the Python script.

```bash
git clone https://github.com/UmutKorkmaz/Python-LSM-SSTable-KeyValueStore
cd ./Python-LSM-SSTable-KeyValueStore
python main.py
```

[Türkçe sürüm için buraya tıklayın](README_TR.md)
