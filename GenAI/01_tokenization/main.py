import tiktoken

enc  = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Vishal Waman"
tokens = enc.encode(text)

# Tokens :  [25216, 3274, 0, 3673, 1308, 382, 119951, 280, 486, 7601]
print("Tokens : ",tokens)

decoded = enc.decode([25216, 3274, 0, 3673, 1308, 382, 119951, 280, 486, 7601])
print("Decoded : ", decoded)