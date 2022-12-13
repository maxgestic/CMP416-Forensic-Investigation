# Brief 
Our intelligence has warned us of suspected bribery in an international competition. Our suspect has downloaded files, and we have been tipped that the files may contain a list of potential names/aliases of actors in this corruption case that is paramount for our investigation. We need to know the details of the **usernames**, how they were hidden, and how you were able to recover them. Details of any other files or noise in  the capture are of no interest to us and need not be reported in any significant detail.

# Aims
- Find Usernames
- Detail how they are hidden
- Detail how I found them

# Findings
- AOL is being used
	- User `k_nc6zxdc5` Maybe
	- snowedinedward@aol.com - Edward Snowden
	- User `u3i05wUXwi` wikiofleaks@aol.com - `wikiofleaks` - Julian Assange
- Documents.zip was downloaded via SMB
	- Contains multiple Folders
		- `Enter the WuTang`
			- [[track6.docx]]
			- [[track10.docx]]
		- `Actual Documents`
			- [[GoT Spoilers.docx]]
			- [[NorthKorea.docx]]
			- [[PiD.docx]]
		- `Chess Boxing`
			- [[NK.jpg]]
			- [[Rules 1..docx]]
			- [[Rules 2.docx]]
			- [[Rules 3.docx]]
			- [[Rules 4.docx]]
			- [[Rules 5.docx]]
			- [[Rules 6.docx]]
			- [[Rules 7.docx]]
		- `More Documents`
			- [[BillOfRights.txt]]
			- [[NorthKorea.jpeg]]
		- [[untitled folder.zip]]
- Other findings:
	- When running strings on [[NorthKorea.jpeg]] it revealed an embedded python script [[broken.py]] output of strings: [[Strings NorthKorea.jpeg output.png]]. After renaming the file to NorthKorea.zip and using `unzip` on it, I was able to extract [[broken.py]]
	- None of the other images had any hidden strings and no hidden zip archives

# Summary
There were to users that were in contact with each other via the AOL email service, the first user was Edward Snowden (snowedinedward@aol.com) and the second was Julian Assange (wikiofleaks@aol.com). Mr Snowden sent a message stating that he had a pcap he wanted Mr Assange to look though, Mr Assange responded that he would do so [[Message 1]] and also asked if Mr Snowden had any further documents to send. Mr Snowden replied that he will send though more documents when able, and Mr Assange thanked him [[Message 2]].

I was able to find an SMB download of a file called `Documents.zip` in the PCAP file, once reconstructed and unzipped it revealed a folder structure with a multitude of folders. In the Directory, `Enter the WuTang`, there was a file called [[track6.docx]] that had a base 64 encoded list of usernames.

In addition, I was able to recreate the python script which seems to take a Text file and a string and then encodes the string using the text document as a key. The file used probably was the [[BillOfRights.txt]] found in the same folder as [[NorthKorea.jpeg]] which contained [[broken.py]].
