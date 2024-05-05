# threadb

## Example usage:

```python
db = ThreadDatabase()
db.add_thread('123', 'Example prompt', 'Example response')
print(db.get_all_threads())
print(db.find_thread_by_id('123'))
db.close()
```