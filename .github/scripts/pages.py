import re
import os
import subprocess

# Step 1: Read the content of index.md
with open('../../index.md', 'r', encoding='utf-8') as file:
    index_content = file.read()

# Step 2: Remove the block ---
index_content = re.sub(r'---\nlayout: page\nhide_title: true\nhide: true\n---\n', '', index_content)

# Step 3: Get the repository name using Git
try:
    repo_name = subprocess.check_output(['git', 'config', '--get', 'remote.origin.url']).decode('utf-8').strip()
    repo_name = repo_name.split('/')[-1].replace('.git', '')
except subprocess.CalledProcessError:
    repo_name = 'not found repository name'

# Step 4: Replace the content of the ### Web Flasher block
index_content = re.sub(r'(### Web Flasher\n)(.*?)(?=\n# |\n## |\n### |\n#### |\n##### )', 
                       rf'\1\nGo to [xyzroe.cc/{repo_name}](https://xyzroe.cc/{repo_name}).\n', 
                       index_content, flags=re.DOTALL)

# Step 5: Check if the file README.md exists
if os.path.exists('../../README.md'):
    # Step 6: Delete the file if it exists
    os.remove('../../README.md')
    
# Step 6: Create a list to store the content of README.md and add the title
readme_content = []
readme_content.append(f"# {repo_name}\n")

# Step 7: Add the modified content from index.md to README.md
readme_content.append(index_content)

# Step 8: Save the changes to README.md
with open('../../README.md', 'w', encoding='utf-8') as file:
    file.writelines(readme_content)
