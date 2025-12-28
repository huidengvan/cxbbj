echo "# Book 3" 
for FILE in *srt; 

do 
echo "## $FILE" ;
echo "" ;
cat "$FILE"; 
done
