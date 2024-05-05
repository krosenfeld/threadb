# threadb

## Example usage:

```python
from threadb import Threadb
from openai import OpenAI
client = OpenAI()
thread = client.beta.threads.create()

db = Threadb()
db.add_thread(thread.id)
print(db.get_all_threads())
print(db.find_thread_by_id(thread.id))
db.remove_thread_by_id(thread.id)
db.close()
```