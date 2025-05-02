import pandas

def tokenize(s):
    tokens = []
    token = ''
    for c in s:
        if c == '(' or c == ')':
            if token:
                tokens.append(token)
                token = ''
            tokens.append(c)
        elif c.isspace():
            if token:
                tokens.append(token)
                token = ''
        else:
            token += c
    if token:
        tokens.append(token)
    return tokens

def parse_tree(tokens):
    def helper():
        token = next(tokens)
        if token != '(':
            raise ValueError("Expected '('")
        label = int(next(tokens))
        children = []
        while True:
            token = next(tokens)
            if token == '(':
                # Put back the '(' and recursively parse
                tokens_stack.insert(0, token)
                children.append(helper())
            elif token == ')':
                return (label, children)
            else:
                children.append(token)
    tokens_stack = list(tokens)
    return helper()

def extract_phrases(node):
    label, children = node
    if all(isinstance(c, str) for c in children):
        phrase = ' '.join(children)
        return [(phrase, label)]
    else:
        phrases = []
        phrase_parts = []
        for child in children:
            if isinstance(child, tuple):
                child_phrases = extract_phrases(child)
                phrases.extend(child_phrases)
                phrase_parts.append(' '.join([w for w, _ in child_phrases if ' ' not in w or w.count(' ') == 0]))
            else:
                phrase_parts.append(child)
        phrase = ' '.join(phrase_parts)
        phrases.append((phrase, label))
        return phrases

train_trees = pd.read_csv("train.txt", header=None, names=["text"])
with open("train_modified.txt", "w", encoding="utf-8") as fout:
#train_tree is a tree in the file train.txt
    for train_tree in train_trees["text"]:
      train_tree = str(train_tree).strip()
      if not train_tree:
        continue
      tokens = tokenize(train_tree)
      parsed_tree = parse_tree(iter(tokens))
      phrases = extract_phrases(parsed_tree)
    
      for phrase, label in phrases:
          fout.write(f"{label}\t{phrase}\n")

dev_trees = pd.read_csv("dev.txt", header=None, names=["text"])
with open("dev_modified.txt", "w", encoding="utf-8") as fout:
#dev_tree is a tree in the file train.txt
    for dev_tree in dev_trees["text"]:
      dev_tree = str(dev_tree).strip()
      if not dev_tree:
        continue
      tokens = tokenize(dev_tree)
      parsed_tree = parse_tree(iter(tokens))
      phrases = extract_phrases(parsed_tree)
    
      for phrase, label in phrases:
          fout.write(f"{label}\t{phrase}\n")

test_trees = pd.read_csv("test.txt", header=None, names=["text"])
with open("test_modified.txt", "w", encoding="utf-8") as fout:
#test_tree is a tree in the file train.txt
    for test_tree in test_trees["text"]:
      test_tree = str(test_tree).strip()
      if not testn_tree:
        continue
      tokens = tokenize(test_tree)
      parsed_tree = parse_tree(iter(tokens))
      phrases = extract_phrases(parsed_tree)
    
      for phrase, label in phrases:
          fout.write(f"{label}\t{phrase}\n")
