import os

SENTENCE = "Unreplied is an AI app that reads your 12,000 unread emails and writes each sender a personalized apology haiku in iambic pentameter, then deletes it unread so your guilt stays perfectly preserved."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")

if __name__ == "__main__":
    main()
