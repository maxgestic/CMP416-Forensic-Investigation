echo "Start"
while read p; do
	echo "${p}"
	cat combined/condone.jpg combined/${p}.jpg | /Users/maximilianring/.iterm2/imgcat -W 50
done <left_words.txt
