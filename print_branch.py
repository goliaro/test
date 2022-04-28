import os

print(os.getenv("GITHUB_SHA"))
print()
print()
print(os.getenv("GITHUB_CONTEXT"))
print()
print()
print(os.getenv("github.event.after"))
