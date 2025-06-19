#!/bin/bash

cd ~/Aura-systems || exit

# Show changes before committing
echo "\n🔍 Git Diff Preview:\n----------------------"
git status

echo "\n🧠 Files changed since last commit:\n"
git diff --name-only

read -p $'\n✨ Proceed with commit? (y/n): ' confirm
if [[ "$confirm" != "y" ]]; then
  echo "❌ Commit canceled."
  exit 1
fi

# Emoji Preset Menu
echo "\n🎨 Choose a commit emoji prefix:"
echo "1) 🧿 HUD Update"
echo "2) 📜 Codex Change"
echo "3) ✨ Feature Add"
echo "4) 🛠 Fix"
echo "5) 🌀 General Sync"
read -p "Enter number: " emoji_option

case $emoji_option in
  1) prefix="🧿 HUD Update";;
  2) prefix="📜 Codex Change";;
  3) prefix="✨ Feature Add";;
  4) prefix="🛠 Fix";;
  5) prefix="🌀 General Sync";;
  *) prefix="🔁 Update";;
esac

read -p "\n📝 Describe your commit: " message

final_msg="$prefix — $message"

git add .
git commit -m "$final_msg"
git push origin main

# Log to vault
now=$(date '+%Y-%m-%d %H:%M:%S')
echo "[$now] $final_msg" >> vault.log

echo -e "\n✅ Commit pushed & logged to vault.log as: \"$final_msg\""

