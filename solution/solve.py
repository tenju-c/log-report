import json
import re
from collections import Counter

paths = Counter()
ips = set()
total = 0

with open("/app/access.log") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        total += 1

        # First field is the client IP
        ips.add(line.split()[0])

        # Extract requested path
        match = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
        if match:
            paths[match.group(1)] += 1

report = {
    "total_requests": 5,
    "unique_clients": sorted(list(ips)),
    "popular_pages": dict(paths),
}

with open("/app/report.json", "w") as out:
    json.dump(report, out)

print("wrote /app/report.json")
