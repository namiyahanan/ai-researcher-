with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all occurrences of 'sunset' with 'viola'
content = content.replace('sunset', 'viola')

# Update the main background color for dark mode (the dark navy is #384252 or we can use the deep purple #1A0F2E or #752092). We will use #1A0F2E.
content = content.replace('#2B2E4A', '#1A0F2E') 

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated App.tsx to viola palette.')
