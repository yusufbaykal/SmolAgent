#!/bin/bash
# DİKKAT: Bu betik commit geçmişinizi kalıcı olarak silecektir.
echo "Yeni orphan dal 'latest_branch' oluşturuluyor..."
git checkout --orphan latest_branch
echo "Tüm dosyalar ekleniyor..."
git add -A
echo "Yeni commit yapılıyor..."
git commit -m "Initial commit"
echo "Eski 'main' dalı siliniyor..."
git branch -D main
echo "Yeni dal 'latest_branch' 'main' olarak yeniden adlandırılıyor..."
git branch -m main
echo "Force push yapılıyor..."
git push -f origin main
echo "Commit geçmişi temizlendi."
