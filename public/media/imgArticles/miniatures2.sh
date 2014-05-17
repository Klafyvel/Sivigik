for image in `ls *.png *.jpg *.jpeg *.gif 2> /dev/null`
do
	convert $image -thumbnail '64x64>' $image
done
