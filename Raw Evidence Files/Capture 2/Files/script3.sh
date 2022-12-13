echo "Start"
cd Combined
while read p; do
	echo "${p}"
	cat there.jpg their.jpg a.jpg ${p}.jpg but.jpg communism.jpg nor.jpg because.jpg unconstitutional.jpg secretive.jpg secret.jpg | /Users/maximilianring/.iterm2/imgcat -W 50
done <../left_words.txt
