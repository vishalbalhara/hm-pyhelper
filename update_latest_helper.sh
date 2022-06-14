#! /bin/bash
hm_pyhelper=$(git rev-parse --short HEAD)

cd ../hm-diag || exit
sed -i -e "s/zip\/.*$/zip\/${hm_pyhelper}/g" requirements.txt
git add -u
git commit -n -m "update pyhelper version"
git push origin
cd - || exit

cd ../hm-config  || exit
sed -i -e "s/zip\/.*$/zip\/${hm_pyhelper}/g" requirements.txt
git add -u
git commit -n -m "update pyhelper version"
git push origin
cd - || exit

cd ../hm-pktfwd || exit
sed -i -e "s/zip\/.*$/zip\/${hm_pyhelper}/g" requirements.txt
git add -u
git commit -n -m "update pyhelper version"
git push origin
cd - || exit

# cd ../hm-miner || exit
# sed -i -e "s/zip\/.*$/zip\/${hm_pyhelper}/g" requirements.txt
# git add -u
# git commit -n -m "update pyhelper version"
# git push origin
# cd - || exit
