import os
import json

class SSTable:
    def __init__(self, filename):
        # Initialize SSTable with a filename for storage
        self.filename = filename
        self.data = {}

    def load_from_disk(self):
        # Load data from disk if file exists
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.data = json.load(file)

    def write_to_disk(self):
        # Write current data to disk
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def insert(self, key, value):
        # Insert key-value pair into SSTable
        self.data[key] = value

    def delete(self, key):
        # Delete key from SSTable if it exists
        if key in self.data:
            del self.data[key]

    def read(self, key):
        # Read value associated with key from SSTable
        return self.data.get(key, None)

class LSMTree:
    def __init__(self, max_memtable_size=30, max_sstables=3):
        # Initialize LSM Tree with memtable and SSTable parameters
        self.memtable = {}
        self.sstables = []
        self.max_memtable_size = max_memtable_size
        self.max_sstables = max_sstables

    def _compaction(self):
        # Perform compaction: move data from memtable to SSTable
        new_sstable = SSTable(f"sstable_{len(self.sstables)}.json")
        for key, value in self.memtable.items():
            if value is not None:
                new_sstable.insert(key, value)
            else:
                new_sstable.delete(key)
        new_sstable.write_to_disk()
        self.sstables.append(new_sstable)
        self.memtable.clear()

        # Merge SSTables if their count exceeds the limit
        if len(self.sstables) > self.max_sstables:
            self._merge_sstables()

    def _merge_sstables(self):
        # Merge data from multiple SSTables into a single SSTable
        merged_data = {}
        for sstable in self.sstables:
            merged_data.update(sstable.data)

        merged_sstable = SSTable(self.sstables[0].filename)
        merged_sstable.data = merged_data
        merged_sstable.write_to_disk()

        # Remove old SSTables after merging
        for sstable in self.sstables[1:]:
            os.remove(sstable.filename)
        self.sstables = [merged_sstable]

    def _load_sstables(self):
        # Load existing SSTables from disk
        for i in range(self.max_sstables):
            filename = f"sstable_{i}.json"
            if os.path.exists(filename):
                sstable = SSTable(filename)
                sstable.load_from_disk()
                self.sstables.append(sstable)

    def start(self):
        # Load existing data from SSTables at the start
        self._load_sstables()

    def insert(self, key, value):
        # Insert key-value pair into LSM Tree
        self.memtable[key] = value
        if len(self.memtable) >= self.max_memtable_size:
            self._compaction()

    def bulk_insert(self, key_value_pairs):
        # Bulk insert multiple key-value pairs
        for key, value in key_value_pairs:
            self.insert(key, value)

    def read(self, key):
        # Read value associated with key from LSM Tree
        if key in self.memtable:
            return self.memtable[key]

        for sstable in reversed(self.sstables):
            value = sstable.read(key)
            if value is not None:
                return value

        return None

    def iterate_keys(self):
        # Iterate over all keys in the LSM Tree
        keys = set(self.memtable.keys())
        for sstable in self.sstables:
            keys.update(sstable.data.keys())
        return keys

    def update(self, key, value):
        # Update value associated with key in LSM Tree
        self.insert(key, value)

    def delete(self, key):
        # Delete key from LSM Tree
        self.memtable[key] = None
        if len(self.memtable) >= self.max_memtable_size:
            self._compaction()

# Expanded Usage Examples
lsm = LSMTree()
lsm.start()  # Start the LSM Tree and load existing data

# Bulk Insertions Example
bulk_data = [("keyA", "valueA"), ("keyB", "valueB"), ("keyC", "valueC")]
lsm.bulk_insert(bulk_data)

# Iterate Over Keys Example
all_keys = lsm.iterate_keys()
print("All Keys:", all_keys)

# Regular Operations
lsm.insert("key1", "value1")
print(lsm.read("key1"))  # Outputs: value1
lsm.update("key1", "updated_value1")
print(lsm.read("key1"))  # Outputs: updated_value1
lsm.delete("key1")
print(lsm.read("key1"))  # Outputs: None

# After Restart
lsm = LSMTree()
lsm.start()
print(lsm.read("keyA"))  # Outputs: valueA or None (depends on compaction)
