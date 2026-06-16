with open('src/App.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace body background logic
content = content.replace('theme === "dark" ? "#030712" : "#FAFAFA"', 'theme === "dark" ? "#2B2E4A" : "#FFFFFF"')
content = content.replace('theme === "dark" ? "bg-[#030712]"', 'theme === "dark" ? "bg-[#2B2E4A]"')
content = content.replace('bg-[#FAFAFA]', 'bg-white')

# Replacing arbitrary indigo values first!
content = content.replace('shadow-indigo-900', 'shadow-sunset-800')
content = content.replace('bg-indigo-900', 'bg-sunset-800')
content = content.replace('border-indigo-900', 'border-sunset-800')
content = content.replace('text-indigo-900', 'text-sunset-800')

content = content.replace('shadow-indigo-700', 'shadow-sunset-600')
content = content.replace('bg-indigo-700', 'bg-sunset-600')
content = content.replace('border-indigo-700', 'border-sunset-600')
content = content.replace('text-indigo-700', 'text-sunset-600')

content = content.replace('shadow-indigo-600', 'shadow-sunset-600')
content = content.replace('bg-indigo-600', 'bg-sunset-600')
content = content.replace('border-indigo-600', 'border-sunset-600')
content = content.replace('text-indigo-600', 'text-sunset-600')

content = content.replace('shadow-indigo-500', 'shadow-sunset-400')
content = content.replace('bg-indigo-500', 'bg-sunset-400')
content = content.replace('border-indigo-500', 'border-sunset-400')
content = content.replace('text-indigo-500', 'text-sunset-400')

content = content.replace('shadow-indigo-400', 'shadow-sunset-400')
content = content.replace('bg-indigo-400', 'bg-sunset-400')
content = content.replace('border-indigo-400', 'border-sunset-400')
content = content.replace('text-indigo-400', 'text-sunset-400')

content = content.replace('shadow-indigo-300', 'shadow-sunset-200')
content = content.replace('bg-indigo-300', 'bg-sunset-200')
content = content.replace('border-indigo-300', 'border-sunset-200')
content = content.replace('text-indigo-300', 'text-sunset-200')

content = content.replace('shadow-indigo-200', 'shadow-sunset-200')
content = content.replace('bg-indigo-200', 'bg-sunset-200')
content = content.replace('border-indigo-200', 'border-sunset-200')
content = content.replace('text-indigo-200', 'text-sunset-200')

content = content.replace('shadow-indigo-100', 'shadow-sunset-200')
content = content.replace('bg-indigo-100', 'bg-sunset-bg')
content = content.replace('border-indigo-100', 'border-sunset-bg')
content = content.replace('text-indigo-100', 'text-sunset-bg')

content = content.replace('shadow-indigo-50', 'shadow-sunset-bg')
content = content.replace('bg-indigo-50', 'bg-sunset-bg')
content = content.replace('border-indigo-50', 'border-sunset-bg')
content = content.replace('text-indigo-50', 'text-sunset-bg')

# Also replace RGBA shadows with specific hex translations
content = content.replace('rgba(79,70,229', 'rgba(246,70,104')
content = content.replace('rgba(79, 70, 229', 'rgba(246, 70, 104')

with open('src/App.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print('done')
