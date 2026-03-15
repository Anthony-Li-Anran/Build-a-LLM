from importlib.metadata import version
import tiktoken

print("tokenizer version:", version("tiktoken"))

tokenizer = tiktoken.get_encoding("gpt2")
text = (
    "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
    "of someunknownPlace."
)
intergers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
print(intergers)
strings = tokenizer.decode(intergers)
print(strings)

test = ("Akwirw ier")
ips = tokenizer.encode(test, allowed_special={"<|endoftext|>"})
print(ips)
words = tokenizer.decode(ips)
print(words)

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

enc_text = tokenizer.encode(raw_text)
print(len(enc_text))

