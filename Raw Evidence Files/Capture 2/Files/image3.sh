echo "Start"
cd image3
while read p; do
	echo "${p}"
	cat condone.jpg American.jpg web-based.jpg rights.jpg constructing.jpg security.jpg terrorism.jpg NSA.jpg Watergate.jpg corrupt.jpg human.jpg behind.jpg ${p} doors.jpg | /Users/maximilianring/.iterm2/imgcat -W 50
done <../image3_words.txt
