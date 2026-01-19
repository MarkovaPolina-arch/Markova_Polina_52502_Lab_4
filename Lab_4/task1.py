import json
# TODO решите задачу
def task() -> float:
    json_content = """[
  {
    "score": 0.0009456152645028281,
    "weight": 1
  },
  {
    "score": 0.00020640167757499364,
    "weight": 1
  },
  {
    "score": 0,
    "weight": 1
  },
  {
    "score": 1.6557065217391307,
    "weight": 1
  },
  {
    "score": 0,
    "weight": 1
  },
  {
    "score": 0.6066065217391303,
    "weight": 1
  },
  {
    "score": 0.03126181644071977,
    "weight": 1
  },
  {
    "score": 0.001253973281817707,
    "weight": 1
  }
]"""
    data = json.loads(json_content)
    total = sum(item["score"] * item["weight"] for item in data)
    return round(total, 3)

print(task())
